# iot_temperatureMonitoring
This project uses an Arduino and a DHT11 sensor to measure temperature and send the data to a server via WiFi.

Features

Reads temperature data using a DHT11 sensor.
Connects to WiFi and sends temperature data to a specified server.
Sends data in JSON format for easy integration with web services.
Components Used

Arduino (ESP8266, ESP32, or any board with WiFi capability).
DHT11 Temperature and Humidity Sensor.
10kΩ Pull-up resistor for the data pin.
How It Works

The DHT11 sensor measures the temperature.
The Arduino reads the temperature data.
The board connects to a WiFi network.
The temperature is sent to a server as a JSON payload.
Hardware Setup

Pin on DHT11	Connects to
VCC	3.3V or 5V
DATA	Pin D2 (Digital)
GND	GND
Circuit Diagram:
(Attach a simple schematic or use a diagram from Wokwi)

Installation and Usage

1. Clone this repository
git clone https://github.com/yourusername/dht11-temperature-monitor.git
2. Install required libraries
Make sure the following libraries are installed in the Arduino IDE:

DHT by Adafruit
WiFi (pre-installed in most boards like ESP32/ESP8266)
HTTPClient (included with ESP32/ESP8266)
3. Update the code
Replace Your_Network_Name and Your_Password in the code with your WiFi credentials.
Set the serverName to your server's URL.
4. Upload the code
Connect your board to the computer.
Select the correct board and port in Arduino IDE.
Upload the code.
Sample Server Response

The data is sent as JSON:

{
  "temperature": 25.6
}
Make sure your server is ready to handle POST requests with this format.

Future Enhancements

Add support for DHT22.
Include humidity readings.
Add error recovery for failed network connections.
