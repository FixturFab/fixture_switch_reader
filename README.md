# Fixture Switch Reader 

![Fixture Switch Reader](./images/assembled%20reader.jpg)

Project files for a USB Fixture Switch Reader using a SparkFun Pro Micro and a
Ingun FB-ABF-V-I-MA2xxx Inductive Switch. 

The Ingun FB-ABF-V-I-MA2xxx Inductive Switch is an inductive sensor which is
used to detect when a MA2xxx series manual test fixture is closed. 

FixturFab uses these switches to determine when a fixtures has been closed and
then automatically start a test run. The switch is powered by 12V, and also has 
a output of 12V when the fixture is closed. 

To interface this to a test system, an SparkFun Pro Micro is used to read the 
output of the sensor, and then relay that information to the test system over a
USB serial port. 


## Project Structure

The project is split into three main folders: 

- firmware
    - Arduino project and sketch for the SparkFun Pro Micro 
- hardware
    - Kicad schematic of the prototyped circuit 
    - Images of the perf board layout 
    - CAD files for the 3D printed enclosure 
- software 
    - Python module for communicating with the device
    
## Firmware 

Arduino 1.8.12 was used to build and program the sketch. 

The sketch reads the state of the switch input, sets the status LED, and then 
processes any available serial commands. The following serial commands are 
supported: 

- version 
    - Return device information and firmware version 
- read_switch
    - Return the current switch state 
    - 0: Fixture Open 
    - 1: Fixture Closed
    
The serial port is setup to use a BAUD rate of 115200. 
    
## Hardware 

![Perfboard Prototype](./images/top%20of%20perfboard%20with%20pro%20micro.jpg)

A SparkFun Pro Micro was used to control this project. To build the circuit, 
perfboard and through-hole components were used. 

A Kicad schematic is available for the circuit layout. There are also pictures 
of the top and bottom of the perfboard. 

### Circuit Design and Layout 

We had a SparkFun Pro Micro (3.3V) available for this project. This device has
ATmega32u4 processor which is capable of USB communication, allowing for a USB 
serial port to be easily created. 

To interface the 12V output of the Inductive switch, a voltage divider is used. 

2 LEDs are also on the board, one connected to VCC of the processor, and the 
other is a status LED that is controlled by the processor. 

A Kicad schematic is included and shows how the circuit was prototyped, along 
with several images of the perf board layout. 

### Enclosure Design 

Fusion360 was used to design the enclosure. The enclosure consists of 2 pieces
that sandwich the protoyped device. The enclosure is held together using 
M3 heat-set inserts and fasteners. 

The STL and STEP files for the enclosure are included along with the Fusion360 
design file.  

## Software

Python 3+ is required for the provided software module. To get started, install
the required dependencies: 

```bash 
cd software/fixture_io
pip install -r requirements.text
```

To create a `FixtureSwitch` class, simple provide the serial port that the
device shows up as, for example: 

- Windows: "COM1"
- MAC: "cu.usbmodem146101"
- Linux: "/dev/ttyACM0"

```python
from fixture_io import FixtureSwitch
fixture_switch = FixtureSwitch("/dev/ttyACM0")

print(fixture_switch.get_info())
print(fixture_switch.read_switch())
```

The following API commands are available: 

- get_info()
    - Get the company, device, and firmware version from the device
- read_switch()
    - Read the switch state 
    - 0: Fixture Open 
    - 1: Fixture Closed
