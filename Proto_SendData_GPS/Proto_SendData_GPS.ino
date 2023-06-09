#include <TinyGPS++.h>
#include <math.h>
#include <Arduino.h>
#include <MKRWAN.h>

#define SECRET_APP_EUI "223B223B223B223B"
#define SECRET_APP_KEY "D5C49ECF01CA9E43D3C2ED644D08DF7F"
#define PI 3.14159265

typedef struct
{
  uint16_t V_HumOut;
  uint16_t V_pHOut;
} Trame_phys;

typedef struct
{
  float X;
  float Y;
} Trame_space;

Trame_phys data;
Trame_space coord;

LoRaModem modem;

static const uint32_t GPSBaud = 9600;

TinyGPSPlus gps;

float originX = 45.76; // pour le moment coordonne de lyon
float originY = 4.836; // a remplacer par input utilisateur

void setup()
{
  Serial.begin(115200);
  Serial1.begin(GPSBaud);

  delay(3000);
  bool lora_on = modem.begin(EU868);
  if (lora_on)
    Serial.println("Démarrage du module LoRaWAN ... OK");
  else
    Serial.println("Démarrage du module LoRaWAN ...Echec");

  delay(3000);
  Serial.print("Mon device EUI est: ");
  Serial.println(modem.deviceEUI());
  Serial.flush();

  bool connected_to_lorawan = modem.joinOTAA(SECRET_APP_EUI, SECRET_APP_KEY);

  if (connected_to_lorawan)
    Serial.println(F("Connexion au réseau LoRaWAN ... Ok"));
  else
    Serial.println(F("Connexion au réseau LoRaWAN ...Echec"));

  Serial.println(F("Mon DevAddr est :"));
  Serial.println(modem.getDevAddr());
}

void loop()
{
  while (Serial1.available() > 0)
    if (gps.encode(Serial1.read())) //checking if NMEA data is received
      displayCoord();

  if (millis() > 5000 && gps.charsProcessed() < 10)
    Serial.println(F("No GPS detected: check wiring."));

  data.V_HumOut = analogRead(A1) / 1024.0 * 2200; // recupere les val de Hum et renvoye sous la forme de V
  data.V_pHOut = analogRead(A1) / 1024.0 * 3000; // recupere les val de pH et renvoye sous la forme de V
  coord.X = gps.location.lat();
  coord.Y = gps.location.lng();

  Serial.print("Please god:");
  Serial.println(data.V_HumOut);

  float delta = Distance(coord.X, coord.Y); // distance euclidienne entre origine et point X.

  SendInfo(delta);

  delay(30000);
}

void displayCoord()
{
  if (gps.location.isValid())
  {
    Serial.print("Latitude: ");
    Serial.println(gps.location.lat(), 6); //print latitude and longitude with 6 decimals
    Serial.print("Longitude: ");
    Serial.println(gps.location.lng(), 6);
  }
  else
  {
    Serial.println("Location: Not Available");
  }
}

void SendInfo(float delta)
{
  float seuil = 5.0;

  if (delta > seuil)
  {
    modem.beginPacket();
    modem.write((byte *)&data, sizeof(data));
    modem.write((byte *)&coord, sizeof(coord));
    int err = modem.endPacket();
    //on change l'origin si on c'est trop eloigne de celle precedente
    originX = coord.X;
    originY = coord.Y;

    if (err > 0)
    {
      Serial.println("Message envoyé correctement");
    }
    else
    {
      Serial.println("Erreur d'envoi :(");
    }
  }
  else
  {
    modem.beginPacket();
    modem.write((byte *)&data, sizeof(data));
    int err = modem.endPacket();
    if (err > 0)
    {
      Serial.println("Message envoyé correctement");
    }
    else
    {
      Serial.println("Erreur d'envoi :(");
    }
  }
}

float Distance(float X, float Y)
{ //Haversine formula
  float R_earth = 6378.14; // Radius of earth in Km
  float d_long = degToRad(X - originX);
  float d_lat = degToRad(Y - originY);
  float a = pow(sin(d_lat / 2), 2) + cos(degToRad(Y)) * cos(degToRad(originY)) * pow(sin(d_long / 2), 2);
  float c = 2 * atan2(sqrt(a), sqrt(1 - a));

  float dist = R_earth * c;
  return dist;
}

float degToRad(float degrees)
{
  float rad = (degrees * PI / 180);
  return rad;
}
