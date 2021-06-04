#include<Wire.h>
int led = D7;
int buzzer = D6;

void setup() {
    Wire.begin(0x8);
    Wire.onReceive(receiveEvent);
    
    pinMode(led, OUTPUT);
    pinMode(buzzer, OUTPUT);
    digitalWrite(buzzer, LOW);
    digitalWrite(led, LOW);
}

void receiveEvent(int i){
    while(Wire.available()){
        char c = Wire.read();
        digitalWrite(led, c);
        digitalWrite(buzzer, c);
    }
}

void loop() {
    delay(1000);
}
