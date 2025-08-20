
#include <SoftwareSerial.h>


SoftwareSerial uart(3, 2);

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(115200);
  uart.begin(115200);
 




 Serial.println("done");
}

void loop() {
  
  String message = uart.readStringUntil('\n');
    

  // if the file opened okay, write to it:   
  while (1==1) {
    while (uart.available()) {
    Serial.write(uart.read());}
    //int message = uart.read();
    /*String message = uart.readStringUntil('\n');*/
    //Serial.println(message);
    /*int a = message.substring(0, message.indexOf(',')).toInt();
    int b = message.substring(message.indexOf(',')+1).toInt();
    Serial.println("Received a = " + String(a) + ", b = " + String(b));*/
    //Serial.println(data);
    
   
    
    //Serial.println("take the data successfully");
    delay(1000);
    
  

  }
  }
  
  