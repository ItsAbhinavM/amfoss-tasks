# Procedure

 Here I have used an  _arduino uno r3_ , _breadboard_ , a _photoresistor_ ,an _lcd screen 16x2_ , a _micro server_ , 2 _resistors_ , a _photoresistor_ , a _potentiometer_ and 27 _wires_ to perform this task .
 In this circuit I have connected the lcd ports to the breadboard as well as the arduino , when the intensity of the light reaches a value greater than 300 ( which indicates a tiny level of brightness ) (  if (val > 300){ myServo.write(180); }  )the servo motor moves to 180 degree angle and when the servo motor rotates the lcd display shows CLOSE ( lcd.print("CLOSE"); ) and if the process does not happens i.e the light intensty does ont crossess 300 then the 
