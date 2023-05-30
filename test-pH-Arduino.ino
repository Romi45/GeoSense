int pH = 0; // Variable où on stock la valeur du pH

void setup() {
  Serial.begin(9600);  // Initialisons la communication serial
}

void loop() {
  pH = analogRead(A1)/1024.0*3000; // on lit les données du pin A0 et on les adapte
  Serial.print("Valeur analogique : ");
  Serial.println(pH);
  delay(1000);
}
