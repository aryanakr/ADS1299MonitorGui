#include <SPI.h>
#include <WiFi.h>

/*
 * Pin Setting:
 * MOSI[DIN] = 23
 * MISO [DOUT] = 19
 * SCLK = 18
 * CS = 5
 * DRDY = 27
 */
 
//wifi credentials
const char* ssid = "BTHub6-5PW3";
const char* password = "H4LMrTrhDpcN";

//Server Credentials
const char* host = "192.168.1.64";
const int port = 6005;
WiFiClient client;

//SPI Command Definition Byte Assignments (Datasheet, pg. 35)
#define _WAKEUP 0x02 // Wake-up from standby mode
#define _STANDBY 0x04 // Enter Standby mode
#define _RESET 0x06 // Reset the device
#define _START 0x08 // Start and restart (synchronize) conversions
#define _STOP 0x0A // Stop conversion
#define _RDATAC 0x10 // Enable Read Data Continuous mode (default mode at power-up)
#define _SDATAC 0x11 // Stop Read Data Continuous mode
#define _RDATA 0x12 // Read data by command; supports multiple read back

#define _RREG 0x20 // (also = 00100000) is the first opcode that the address must be added to for RREG communication
#define _WREG 0x40 // 01000000 in binary (Datasheet, pg. 35)

//Register Addresses
#define ID 0x00
#define CONFIG1 0x01
#define CONFIG2 0x02
#define CONFIG3 0x03
#define LOFF 0x04
#define CH1SET 0x05
#define CH2SET 0x06
#define CH3SET 0x07
#define CH4SET 0x08
#define CH5SET 0x09
#define CH6SET 0x0A
#define CH7SET 0x0B
#define CH8SET 0x0C
#define BIAS_SENSP 0x0D
#define BIAS_SENSN 0x0E
#define LOFF_SENSP 0x0F
#define LOFF_SENSN 0x10
#define LOFF_FLIP 0x11
#define LOFF_STATP 0x12
#define LOFF_STATN 0x13
#define GPIO 0x14
#define MISC1 0x15
#define MISC2 0x16
#define CONFIG4 0x17

byte Value = 0xA9; 
// The variable to store the value of incoming byte. Setting a predefined value so that if there is no data transferred, it shows a predefined value on oscilloscope.

const int DRDY = 27;
const int tCLK = 0.000666;

enum comStates{
  UNAVAILABLE,
  DISCONNECTED,
  COMMAND_READY,
  REG_SETUP,
  DATA_OUT
};

comStates deviceState;

void setup() {

  Serial.begin(115200);

  deviceState = UNAVAILABLE;
  
  pinMode(SS, OUTPUT);
  pinMode(DRDY,INPUT);
  
  SPI.begin(SCK,MISO,MOSI,SS);
  SPI.beginTransaction(SPISettings(1500000, MSBFIRST, SPI_MODE1)); // 1.5 MHz
  digitalWrite(SS, LOW); // Chip Select LOW

  //connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }

  // Print ESP32 Local IP Address
  Serial.println(WiFi.localIP());
  
  //Connect to Gui Server
  deviceState = DISCONNECTED;
  Serial.println("");
  Serial.println("WiFi connected with IP address: ");
  Serial.println(WiFi.localIP());
  while(true){
    Serial.print("connecting to ");
    Serial.print(host);
    Serial.print(":");
    Serial.println(port);
    if (!client.connect(host, port)) {
        Serial.println("connection failed");
        continue;
    }
      break;
      delay(500);
  }

  RESET();
  
}

bool deviceIDReturned = false;
bool isDataLogging = false;
bool closed = false;

void loop() {

  if(deviceIDReturned == false){
    
    getDeviceID(); //Funciton to return Device ID
    
    //prints dashed line to separate serial print sections
    Serial.println("----------------------------------------------");
    
    //Read ADS1299 Register at address 0x00 (see Datasheet pg. 35 for more info on SPI commands)
    RREG(0x00);
    Serial.println("----------------------------------------------");

    //Initial Registers Setup
    while(1){
      if(readServer() == "setreg"){
        deviceState = REG_SETUP;
        Serial.print("Start Initial Registers Setup");
        client.print("rdy");
        updateRegisters();
        break;
      }
    }
    //PRINT ALL REGISTERS... Read 0x17 addresses starting from address 0x00 (these numbers can be replaced by binary or integer values)
    RREG(0x00, 0x17);

    deviceIDReturned = true;
    deviceState = COMMAND_READY;
    Serial.print("imout");
  }
  
  //Main Device Controll
  while(!closed){
    if(deviceState == COMMAND_READY){
      Serial.println("Wait for command");
      delay(500);
      String cmd = readServer();
      if(cmd == "setreg"){
        deviceState = REG_SETUP;
      }
      if(cmd == "datalog"){
        deviceState = DATA_OUT;
      }
      if(cmd == "close"){
        deviceState = DISCONNECTED;
      }
    }
    if(deviceState == REG_SETUP){
      Serial.println("start setting registers");
      client.print("rdy");
      updateRegisters();
      deviceState = COMMAND_READY;
    }
    if(deviceState == DATA_OUT){
      if(!isDataLogging){
        START();
        isDataLogging = true;
        delay(1000);
      }
      updateData();
    }
    if(deviceState == DISCONNECTED){
      closed = true;
      while(client.available()){
        Serial.println("behind pipeline");
        readServer();
      }
      client.stop();
    }
  }

  //end of execution
  Serial.println("Connection Closed! Reset Needed!");
  
}

void updateRegisters(){
  Serial.println("Start update registers");

  updateRegFromServer(CONFIG1); //update config1
  updateRegFromServer(CONFIG2); //update config2
  updateRegFromServer(CONFIG3); //upadate config3
  updateRegFromServer(LOFF); //update loff
  updateRegFromServer(CH1SET); //update ch1set
  updateRegFromServer(CH2SET); //update ch2set
  updateRegFromServer(CH3SET); //update ch3set
  updateRegFromServer(CH4SET); //update ch4set
  updateRegFromServer(CH5SET); //update ch5set
  updateRegFromServer(CH6SET); //update ch6set
  updateRegFromServer(CH7SET); //update ch7set
  updateRegFromServer(CH8SET); //update ch8set
  updateRegFromServer(BIAS_SENSP); //update bias_sensp
  updateRegFromServer(BIAS_SENSN); //update bias_sensn
  updateRegFromServer(LOFF_SENSP); //update loff_sensp
  updateRegFromServer(LOFF_SENSN); //update loff_sensn
  updateRegFromServer(LOFF_FLIP); //update loff_flip
  updateRegFromServer(MISC1); //update misc1
  updateRegFromServer(MISC2); //update misc2
  updateRegFromServer(GPIO); //update gpio
  updateRegFromServer(CONFIG4); //update config4

  //send finish massage
  client.print("done");

  Serial.println("Updated Registers:");

  //print updated registers
  Serial.println("-------------------------------------------");
  RREG(0x00, 0x17);
}

void updateRegFromServer(byte _address){
  String addressStr = getRegisterName(_address);
  client.print(addressStr);
  while(!client.available()){
    Serial.println("waiting for " + addressStr + " data");
    delay(200);
  }
  int currd = 0;
  currd = strtol( readServer().c_str(), NULL, 2 );
  WREG(_address, currd);
}

String readServer(){
  if (client.available()) {
    uint8_t data[30]; 
    int len = client.read(data, 30);
    if(len < 30){
        data[len] = '\0';  
    }else {
        data[30] = '\0';
    }    
    Serial.print("client sent: :");            
    Serial.println((char *)data);
    return String((char *)data);
  }
  return "na";
}

//--------------------------------------------------------------------------------------------------
//ADS1299 Control Methods

int outputCount = 0;

void updateData(){
  if(readServer() == "stopdata"){
    deviceState = COMMAND_READY;
    isDataLogging = false;
    STOP();
    return;
  }
  String cycleData;
  
  char timeBuffer[8];
  if(outputCount >= 99999999)
    outputCount = 0;
  sprintf(timeBuffer,"%8d",outputCount);
  cycleData = "t"+String(timeBuffer)+", ";

  if(digitalRead(DRDY) == LOW){
      digitalWrite(SS, LOW);
      long output[9];
      long dataPacket;

      for(int i = 0; i<9; i++){
          for(int j = 0; j<3; j++){
              byte dataByte = SPI.transfer(0x00);
              dataPacket = (dataPacket<<8) | dataByte;
          }
          output[i] = dataPacket;
          dataPacket = 0;
      }

      digitalWrite(SS, HIGH);

      for (int i=0;i<9; i++) {
          char dataBuffer[8];
          sprintf(dataBuffer,"%8d",output[i]);
          cycleData += dataBuffer;
          if(i!=8)
            cycleData += ", ";   
      }
      
      Serial.println(cycleData);
      client.print(cycleData);   
      outputCount++;
  }else{
    Serial.println("DRDY HIGH");
    client.print("drdyhigh");
  }
}

void WAKEUP() {
    digitalWrite(SS, LOW); //Low to communicate
    SPI.transfer(_WAKEUP);
    digitalWrite(SS, HIGH); //High to end communication
    delay(4.0*tCLK);  //must way at least 4 tCLK cycles before sending another command (Datasheet, pg. 35)
}
void STANDBY() {
    digitalWrite(SS, LOW);
    SPI.transfer(_STANDBY);
    digitalWrite(SS, HIGH);
}
void RESET() {
    digitalWrite(SS, LOW);
    SPI.transfer(_RESET);
    delay(10);
//    delay(18.0*tCLK); //must wait 18 tCLK cycles to execute this command (Datasheet, pg. 35)
    digitalWrite(SS, HIGH);
}
void START() {
    digitalWrite(SS, LOW);
    SPI.transfer(_START);
    digitalWrite(SS, HIGH);
}
void STOP() {
    digitalWrite(SS, LOW);
    SPI.transfer(_STOP);
    digitalWrite(SS, HIGH);
}
//Data Read Commands
void RDATAC() {
    digitalWrite(SS, LOW);
    SPI.transfer(_RDATAC);
    digitalWrite(SS, HIGH);
}
void SDATAC() {
    digitalWrite(SS, LOW);
    SPI.transfer(_SDATAC);
    digitalWrite(SS, HIGH);
}
void RDATA() {
    digitalWrite(SS, LOW);
    SPI.transfer(_RDATA);
    digitalWrite(SS, HIGH);
}

//Register Read/Write Commands
void getDeviceID() {
    digitalWrite(SS, LOW); //Low to communicated
    SPI.transfer(_SDATAC); //SDATAC
    SPI.transfer(_RREG); //RREG
    SPI.transfer(0x00); //Asking for 1 byte
    byte data = SPI.transfer(0x00); // byte to read (hopefully 0b???11110)
    SPI.transfer(_RDATAC); //turn read data continuous back on
    digitalWrite(SS, HIGH); //Low to communicated
    Serial.println(data, BIN);
}

void RREG(byte _address) {
    byte opcode1 = _RREG + _address; //001rrrrr; _RREG = 00100000 and _address = rrrrr
    digitalWrite(SS, LOW); //Low to communicated
    SPI.transfer(_SDATAC); //SDATAC
    SPI.transfer(opcode1); //RREG
    SPI.transfer(0x00); //opcode2
    byte data = SPI.transfer(0x00); // returned byte should match default of register map unless edited manually (Datasheet, pg.39)
    printRegisterName(_address);
    Serial.print("0x");
    if(_address<16) Serial.print("0");
    Serial.print(_address, HEX);
    Serial.print(", ");
    Serial.print("0x");
    if(data<16) Serial.print("0");
    Serial.print(data, HEX);
    Serial.print(", ");
    for(byte j = 0; j<8; j++){
        Serial.print(bitRead(data, 7-j), BIN);
        if(j!=7) Serial.print(", ");
    }
    SPI.transfer(_RDATAC); //turn read data continuous back on
    digitalWrite(SS, HIGH); //High to end communication
    Serial.println();
}

void RREG(byte _address, byte _numRegistersMinusOne) {
    byte opcode1 = _RREG + _address; //001rrrrr; _RREG = 00100000 and _address = rrrrr
    digitalWrite(SS, LOW); //Low to communicated
    SPI.transfer(_SDATAC); //SDATAC
    SPI.transfer(opcode1); //RREG
    SPI.transfer(_numRegistersMinusOne); //opcode2
    for(byte i = 0; i <= _numRegistersMinusOne; i++){
        byte data = SPI.transfer(0x00); // returned byte should match default of register map unless previously edited manually (Datasheet, pg.39)
        printRegisterName(i);
        Serial.print("0x");
        if(i<16) Serial.print("0"); //lead with 0 if value is between 0x00-0x0F to ensure 2 digit format
        Serial.print(i, HEX);
        Serial.print(", ");
        Serial.print("0x");
        if(data<16) Serial.print("0"); //lead with 0 if value is between 0x00-0x0F to ensure 2 digit format
        Serial.print(data, HEX);
        Serial.print(", ");
        for(byte j = 0; j<8; j++){
            Serial.print(bitRead(data, 7-j), BIN);
            if(j!=7) Serial.print(", ");
        }
        Serial.println();
    }
    SPI.transfer(_RDATAC); //turn read data continuous back on
    digitalWrite(SS, HIGH); //High to end communication
}



void WREG(byte _address, byte _value) {
    byte opcode1 = _WREG + _address; //001rrrrr; _RREG = 00100000 and _address = rrrrr
    digitalWrite(SS, LOW); //Low to communicated
    SPI.transfer(_SDATAC); //SDATAC
    SPI.transfer(opcode1);
    SPI.transfer(0x00);
    SPI.transfer(_value);
    SPI.transfer(_RDATAC);
    digitalWrite(SS, HIGH); //Low to communicated
    Serial.print("Register 0x");
    Serial.print(_address, HEX);
    Serial.println(" modified.");
}

// String-Byte converters for RREG and WREG
void printRegisterName(byte _address) {
    if(_address == ID){
        Serial.print("ID, ");
    }
    else if(_address == CONFIG1){
        Serial.print("CONFIG1, ");
    }
    else if(_address == CONFIG2){
        Serial.print("CONFIG2, ");
    }
    else if(_address == CONFIG3){
        Serial.print("CONFIG3, ");
    }
    else if(_address == LOFF){
        Serial.print("LOFF, ");
    }
    else if(_address == CH1SET){
        Serial.print("CH1SET, ");
    }
    else if(_address == CH2SET){
        Serial.print("CH2SET, ");
    }
    else if(_address == CH3SET){
        Serial.print("CH3SET, ");
    }
    else if(_address == CH4SET){
        Serial.print("CH4SET, ");
    }
    else if(_address == CH5SET){
        Serial.print("CH5SET, ");
    }
    else if(_address == CH6SET){
        Serial.print("CH6SET, ");
    }
    else if(_address == CH7SET){
        Serial.print("CH7SET, ");
    }
    else if(_address == CH8SET){
        Serial.print("CH8SET, ");
    }
    else if(_address == BIAS_SENSP){
        Serial.print("BIAS_SENSP, ");
    }
    else if(_address == BIAS_SENSN){
        Serial.print("BIAS_SENSN, ");
    }
    else if(_address == LOFF_SENSP){
        Serial.print("LOFF_SENSP, ");
    }
    else if(_address == LOFF_SENSN){
        Serial.print("LOFF_SENSN, ");
    }
    else if(_address == LOFF_FLIP){
        Serial.print("LOFF_FLIP, ");
    }
    else if(_address == LOFF_STATP){
        Serial.print("LOFF_STATP, ");
    }
    else if(_address == LOFF_STATN){
        Serial.print("LOFF_STATN, ");
    }
    else if(_address == GPIO){
        Serial.print("GPIO, ");
    }
    else if(_address == MISC1){
        Serial.print("MISC1, ");
    }
    else if(_address == MISC2){
        Serial.print("MISC2, ");
    }
    else if(_address == CONFIG4){
        Serial.print("CONFIG4, ");
    }
}

//Get String name of an address
String getRegisterName(byte _address){
  if(_address == ID){
        return("ID");
    }
    else if(_address == CONFIG1){
        return("CONFIG1");
    }
    else if(_address == CONFIG2){
        return("CONFIG2");
    }
    else if(_address == CONFIG3){
        return("CONFIG3");
    }
    else if(_address == LOFF){
        return("LOFF");
    }
    else if(_address == CH1SET){
        return("CH1SET");
    }
    else if(_address == CH2SET){
        return("CH2SET");
    }
    else if(_address == CH3SET){
        return("CH3SET");
    }
    else if(_address == CH4SET){
        return("CH4SET");
    }
    else if(_address == CH5SET){
        return("CH5SET");
    }
    else if(_address == CH6SET){
        return("CH6SET");
    }
    else if(_address == CH7SET){
        return("CH7SET");
    }
    else if(_address == CH8SET){
        return("CH8SET");
    }
    else if(_address == BIAS_SENSP){
        return("BIAS_SENSP");
    }
    else if(_address == BIAS_SENSN){
        return("BIAS_SENSN");
    }
    else if(_address == LOFF_SENSP){
        return("LOFF_SENSP");
    }
    else if(_address == LOFF_SENSN){
        return("LOFF_SENSN");
    }
    else if(_address == LOFF_FLIP){
        return("LOFF_FLIP");
    }
    else if(_address == LOFF_STATP){
        return("LOFF_STATP");
    }
    else if(_address == LOFF_STATN){
        return("LOFF_STATN");
    }
    else if(_address == GPIO){
        return("GPIO");
    }
    else if(_address == MISC1){
        return("MISC1");
    }
    else if(_address == MISC2){
        return("MISC2");
    }
    else if(_address == CONFIG4){
        return("CONFIG4");
    }
}
