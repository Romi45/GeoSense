#include <TinyGPS++.h>

static const uint32_t GPSBaud = 9600;

TinyGPSPlus gps;


void setup()
{
  Serial.begin(115200);
  Serial1.begin(GPSBaud);
}

void loop()
{
  while (Serial1.available() > 0)
    if (gps.encode(Serial1.read()))  //checking if NMEA data is received
      displayInfo();

  if (millis() > 5000 && gps.charsProcessed() < 10)  
    Serial.println(F("No GPS detected: check wiring."));
}

void displayInfo()
{
  if (gps.location.isValid())
  {
    Serial.print("Latitude: ");
    Serial.println(gps.location.lat(),6); //print latitude and longitude with 6 decimals
    Serial.print("Longitude: ");
    Serial.println(gps.location.lng(),6);
  }
  else
  {
    Serial.println("Location: Not Available");
  }
}
