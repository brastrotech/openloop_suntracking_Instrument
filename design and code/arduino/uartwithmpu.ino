/* Get tilt angles on X and Y, and rotation angle on Z
 * Angles are given in degrees
 * 
 * License: MIT
 */

#include "Wire.h"
#include <MPU6050_light.h>
#include <Servo.h>
Servo pitchs;
Servo rolls;
float X,Y,Z,pitch,roll, yaw;
#include <SoftwareSerial.h>
int a0,b0,a,b;
String message ;
SoftwareSerial uart(3, 2);
MPU6050 mpu(Wire);
unsigned long timer = 0;

void setup() {
  Serial.begin(115200);
  uart.begin(115200);
  Wire.begin();
  
  byte status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  while(status!=0){ } // stop everything if could not connect to MPU6050
  
  Serial.println(F("Calculating offsets, do not move MPU6050"));
  delay(1000);
  // mpu.upsideDownMounting = true; // uncomment this line if the MPU6050 is mounted upside-down
  mpu.calcOffsets(); // gyro and accelero
  Serial.println("Done!\n");
  pitchs.attach(9);
  rolls.attach(10);
}

void loop() {
  mpu.update();
  String message = uart.readStringUntil('\n');
  
  
  if((millis()-timer)>1000){ // print data every 10ms
  Serial.print("X : ");
  X = mpu.getAngleX();
  Y = mpu.getAngleY();
  Z = mpu.getAngleZ();
  String message = uart.readStringUntil('\n');
  
  pitch = 180 * atan2(X, sqrt(Y*Y + Z*Z))/PI; // calculate the pitch angle
  pitch = pitch +90; // here 90 is to make the pitch from 0 to 180 insted of -90 to 90 for servo 
  pitch = pitch + b; // set the angle accordingly your elevation here b is elevaion
  
  roll = 180 * atan2(Y, sqrt(X*X + Z*Z))/PI;
  roll = roll + 90; // here 90 is to make the pitch from 0 to 180 insted of -90 to 90 for servo 
  roll = roll + a; // here a is azimuth 
  pitchs.write(pitch);
  rolls.write(roll);
  Serial.println();
  Serial.print(pitch);
  Serial.print(roll);
  
//  roll = atan2(-accelerometer[1],accelerometer[2]);
  
  timer = millis();  
  }
}