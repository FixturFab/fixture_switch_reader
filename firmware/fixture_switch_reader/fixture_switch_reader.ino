// Fixture Switch Reader
// SparkFun Micro Pro (3.3V) based USB IO Reader
//
// Connect using a serial terminal at 115200 BAUD
// Fixture Firmware Version
int FW_VER = 1;
// Pin Definitions
int STATUS_LED = 7;
int INGUN_PIN = 4;
// Global Variables
int sw_close = 0;
char buffer[256];
String command;
void setup()
{
  // Set switch pin as an input
  pinMode(INGUN_PIN, INPUT);
  // Set LED as an output
  pinMode(STATUS_LED, OUTPUT);
  // Open a USB serial port 
  Serial.begin(115200);
}
void loop() {
  // Read switch state and set the status LED
  sw_close = digitalRead(INGUN_PIN);
  digitalWrite(STATUS_LED, !sw_close);
  // Read and process available serial commands
  if(Serial.available()) {
    command = Serial.readStringUntil('\n');
    if(command.equals("read_switch")) {
      Serial.println(sw_close);
    }
    else if(command.equals("version")) {
      sprintf(buffer, "FixturFab Inc.\nFixture Switch Reader\nFW version: %d", FW_VER);
      Serial.println(buffer);
    }
    else {
      Serial.println("invalid command");
    }
  }
}
