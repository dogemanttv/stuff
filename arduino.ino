int Xval = 0;
int Yval = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Xval = analogRead(A2);  // X
  Yval = analogRead(A1);  // Y
  Serial.println("X: " + String(Xval) + " Y: " + String(Yval));

  /*
  if (Yval <= 10) {
    Serial.println("W");
  }    
  if (Yval >= 670) {
    Serial.println("S");
  }    
  if (Xval <= 10) {
    Serial.println("D");
  }    
  if (Xval >= 670) {
    Serial.println("A");
  }    
  */
}

