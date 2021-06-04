#define LIGHT_PIN A0  
#define LIGHT_LEVEL_THRESHOLD 800 // light level 
#define THRESHOLD_SENSITIVITY 50 // higher number = lower sensitivity, lower number = higher sensitivity 
void setup() {
 
} 
void loop() { 
   // value decreases as brightness increases 
   int dark = analogRead(LIGHT_PIN); 
   
   if (dark >= LIGHT_LEVEL_THRESHOLD) 
   { 
       Particle.publish("light-level-changed", "dark"); 
       
       // Once dark is triggered, the threshold is temporarily shifted so we dont  have the state between dark and bright 
       while (analogRead(LIGHT_PIN) > LIGHT_LEVEL_THRESHOLD - THRESHOLD_SENSITIVITY); 
   } 
   else 
   { 
       Particle.publish("light-level-changed", "bright"); 
   } 
} 
