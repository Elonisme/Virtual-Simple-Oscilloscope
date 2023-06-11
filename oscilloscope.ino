double x = 0;
double y = 0;
char myT[6];
char myV[6];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()>0 && Serial.peek() =='b')
    {
      float sensorValue = analogRead(A0);
      float volatage = sensorValue * (5.0 / 1023.0);
      y = volatage;
      Serial.println(x);
      if(y < 0){
        y = y * (-1);
        Serial.println("1");
        Serial.println(y);
      }else{
        Serial.println("0");
        Serial.println(y);
      }
      x++;
    }
}
