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
MPU6050 mpu(Wire);
unsigned long timer = 0;

void setup() {
  Serial.begin(9600);
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
  
  
  if((millis()-timer)>100){ // print data every 10ms
  Serial.print("X : ");
  X = mpu.getAngleX();
  Y = mpu.getAngleY();
  Z = mpu.getAngleZ();
  pitch = 180 * atan2(X, sqrt(Y*Y + Z*Z))/PI;
  pitch = pitch +90;
  roll = 180 * atan2(Y, sqrt(X*X + Z*Z))/PI;
  roll = roll + 90;
  pitchs.write(pitch);
  rolls.write(roll);
  Serial.println();
  Serial.print(pitch);
  Serial.print(roll);
  
//  roll = atan2(-accelerometer[1],accelerometer[2]);
  
  timer = millis();  
  }
}