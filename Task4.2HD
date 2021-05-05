int RLED = D2;
int GLED = D3;
int YLED = D4;


void setup() {
    pinMode(RLED, OUTPUT);
    pinMode(GLED, OUTPUT);
    pinMode(YLED, OUTPUT);
    
    Particle.function("led",ledToggle);
}

int ledToggle(String cmd){
    if (cmd=="on1"){
        digitalWrite(RLED, HIGH);
        digitalWrite(YLED, LOW);
        digitalWrite(GLED, LOW);
        return 1;
    }
    if (cmd=="on2"){
        digitalWrite(RLED, LOW);
        digitalWrite(YLED, LOW);
        digitalWrite(GLED, HIGH);
        return 0;
    }
    if (cmd=="on3"){
        digitalWrite(RLED, LOW);
        digitalWrite(YLED, HIGH);
        digitalWrite(GLED, LOW);
        return 0;
    }
    else{
        return -1;
    }
    
}

void loop() {
    
}


<!DOCTYPE>
<html lang="en">
	<body>
	<center>
	<br>
	<form action="https://api.particle.io/v1/devices/e00fce68f7676ba003b96aa2/led?access_token=c189b6a50f532ca66ce055f3223b54f6f729540b" method="POST" target="_blank">
		<br>
		<input type ="radio" name="arg" value="on1">Turn red LED on.
		</br>
		<br>
		<input type ="radio" name="arg" value="on2">Turn green LED on.
		</br>
		<br>
		<input type ="radio" name="arg" value="on3">Turn yellow LED on.
		</br>
		<br>
		<input type ="submit" value="Enter">
		</br>
	</form>
	</br>
	</center>
	</body>
</html>
