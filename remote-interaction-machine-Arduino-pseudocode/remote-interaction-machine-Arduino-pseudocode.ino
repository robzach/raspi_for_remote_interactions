/*
 * writing Arduino-style code for the remote interaction machine because it's
 * more comfortable and obvious to me, and then once I've figured out the main
 * execution flow I should be able to port it to Python to run on the two remote machines
 * 
 * Robert Zacharias 4-12-17
 */


const int LIGHTGATEPIN = 2;
const int SOLENOIDPIN = 3;

const long BALLWAIT = 500;


long lastReceive = 0;
long lastTransmit = 0;

String URL-to-query = http://appname.heroku.com;

void setup() {
  pinMode(LIGHTGATEPIN, INPUT);
  pinMode(SOLENOIDPIN, OUTPUT);
  digitalWrite(SOLENOIDPIN, LOW);
}

void loop() {
  if (LIGHTGATEPIN == HIGH && (millis() - lastTransmit > 500)) {
    URL-to-query.sendHighMessage;
    lastTransmit = millis();
  }
  
  ballKicker();
  
}

void ballKicker(){
  if (millis() - lastReceive > BALLWAIT){
    int remoteMessage = URL-to-query.query;
    if (remoteMessage){
      digitalWrite(SOLENOIDPIN, HIGH);
      delay(100);
      digitalWrite(SOLENOIDPIN, LOW);
    }
    lastReceive = millis();
  }
}

