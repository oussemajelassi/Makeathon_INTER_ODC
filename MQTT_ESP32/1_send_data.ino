#include"MPU9250.h"
#include"Wire.h"
//#include"Servo.h"

#include "arduino_secrets.h"
#include <LiveObjects.h>
/******************************************************************************
   USER VARIABLES
 ******************************************************************************/
uint32_t messageRate = 5000  ;   // stores the current data message rate in Milliseconds
unsigned long uptime;   // stores the device uptime (sent as fake sensor data)
unsigned long lastMessageTime = 0;   // stores the time when last data message was sent

/******************************************************************************
   USER PROGRAM
 ******************************************************************************/
MPU9250 IMU(Wire, 0x68);
int s;
   
void setup() {
  // serial to display data
  Serial.begin(115200);
       
  Serial.print("\n*** Live Objects for Arduino MKR boards, revision ");
  Serial.print(SW_REVISION);
  Serial.println(" ***");
  lo.setSecurity(TLS);
  lo.begin(MQTT, TEXT, true);
  lo.connect(); // connects to the network + Live Objects

  
  s = IMU.begin();
 
 
}

void loop() {
  // read the sensor
  if (millis() - lastMessageTime > messageRate) {
    // collect data periodically
    Serial.println("Sampling data");
    uptime = millis();
    IMU.readSensor();

    lo.addToPayload(" Vibration ",IMU.getAccelZ_mss());               // adding 'uptime' value to the current payload
    Serial.println("Sending data to Live Objects");
    lo.sendData();                                   // send the data to Live Objects
    lastMessageTime = millis();
  }
  lo.loop();            
  
 
}
