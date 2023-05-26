#include <Arduino.h>
#include <MKRWAN.h>

#define SECRET_APP_EUI "223B223B223B223B"
#define SECRET_APP_KEY "D5C49ECF01CA9E43D3C2ED644D08DF7F"


typedef struct
{
uint16_t V_HumOut;

uint16_t V_pHOut;

float CoordX;
float CoordY;
} Trame_t ;

Trame_t ma_trame;

LoRaModem modem;

void setup() {

  Serial.begin(9600);
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

void loop() {

  ma_trame.V_HumOut = analogRead(A1)/1024.0*2200 ;
  ma_trame.V_pHOut = analogRead(A1)/1024.0*3000 ;
  ma_trame.CoordX = 0.0 ;
  ma_trame.CoordY = 0.0 ;
       
  Serial.print("Please god:");
  Serial.println(ma_trame.V_HumOut);

  modem.beginPacket();
  modem.write( (byte* )& ma_trame, sizeof(ma_trame) ) ;
  int err = modem.endPacket();
  if (err > 0) {
    Serial.println("Message envoyé correctement");
  } else {
    Serial.println("Erreur d'envoi :(");
  }

  delay(30000);

}
