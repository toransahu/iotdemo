#include <Wire.h>
#include <math.h>

//this is the slave address at which the arduino would be available for I2C comm
int SLAVE_ADDRESS = 0x04;
int ledPin = 13;//since we want to blink the led at this port when the data is being sampled
int shPin= A0;//this is the pin at which the arduino is taking in input from hygrometer
int tempPin = A1;
int lightPin = A2;


void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(processRequest);
  Wire.onRequest(sendAnalogReading);
}
void loop(){
}
//this n is the number of bytes read from the master
void processRequest(int n){
  //this is the upload status to the cloud as communicated by master board
  int uploadStatus = Wire.read();
  OnBoardLED(uploadStatus);
}

void OnBoardLED(int value){
  if(value==200){
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
}
double Thermistor(int rawVoltValue){
  double Temp;
  Temp = log(((10230000/rawVoltValue)-10000));
  Temp = 1/(0.001129148+(0.000234125+(0.0000000876741 *Temp *Temp))*Temp);
  Temp = Temp-272.15;
  return Temp;
}
double Temp(int value)
{
	//this helps us get the real temparature from the milivolt reading that we have
	double temper;
  	temper = ((double)value /1023)*5000;
  	temper = (double)temper /10;
  	return temper;
}
void sendAnalogReading(){
  int reading  = analogRead(shPin);
  //Serial.println(reading);
  int lowvalue = 553 ; 
  int highvalue =1023; //this is when soil is completely dry and arid
  reading = reading>=highvalue ? highvalue : reading <=lowvalue ? lowvalue :reading; //normalizing the reading between 80-185
  //getting the scaled reading in percentage
  double moistcent = (double)(highvalue-reading)/(highvalue-lowvalue);
  //Serial.println(moistcent);
  //sending the percent moiture to the master back
  byte package[10];
  package[0] = (int)(moistcent*100);
  
  //now here we read the temprature as well...
  package[1] = (int)Temp(analogRead(tempPin));
  package[2]= (int)analogRead(tempPin);
  
  Wire.write(package, 10);
}
