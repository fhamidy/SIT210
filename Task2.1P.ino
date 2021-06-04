// ------------
// Blink an LED in Morse
// ------------

int led1 = D6; 
int led2 = D7;

void setup() {
    
	pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);

}

// Function to call dot
void dot(){
    digitalWrite(led1, HIGH);
    delay(300);
    digitalWrite(led1, LOW);
    delay(300);
}

// Function to call line
void line(){
    digitalWrite(led1, HIGH);
    delay(1000);
    digitalWrite(led1, LOW);
    delay(300);
}

// letter A
void alpha(){
    dot();
    line();
}

// letter d
void delta(){
    line();
    dot();
    dot();
}

// letter f
void foxtrot(){
    dot();
    dot();
    line();
    dot();
}

// letter h
void hotel(){
    dot();
    dot();
    dot();
    dot();
}

// letter i
void india(){
    dot();
    dot();
}

//letter m
void mike(){
    line();
    line();
}

// letter r
void romeo(){
    dot();
    line();
    dot();
}

// letter y
void yankee(){
    line();
    dot();
    line();
    line();
}

// A function to inform that blinkin
// for a letter is completed. Can be
// removed later when morse pattern is
// correct.
void test(){
    digitalWrite(led2, HIGH);
    delay(300);
    digitalWrite(led2, LOW);
}

void firstName(){
    foxtrot();
    delay(1000);
    //test();
    alpha(); 
    delay(1000);
    //test();
    romeo();
    delay(1000);
    //test();
    romeo();
    delay(1000);
    //test();
    alpha();
    delay(1000);
    //test();
    hotel();
    delay(3000);
    //test();
}

void lastName(){
    hotel();
    delay(1000);
    //test();
    alpha();
    delay(1000);
    //test();
    mike();
    delay(1000);
    //test();
    india();
    delay(1000);
    //test();
    delta();
    delay(1000);
    //test();
    yankee();
    delay(1000);
    //test();
}
void loop() {
    
    firstName();
    //lastName();
}
