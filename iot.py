#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>

// تنظیمات سنسور DHT
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// اطلاعات WiFi
const char* ssid = "نام_شبکه";
const char* password = "رمز_عبور";

// آدرس سرور
const char* serverName = "http://your-server.com/temperature";

void setup() {
  Serial.begin(115200);
  dht.begin();

  // اتصال به WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // خواندن دما
  float temperature = dht.readTemperature();
  
  if (isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // ارسال به سرور
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);

    // ارسال داده‌ها
    http.addHeader("Content-Type", "application/json");
    String jsonData = "{\"temperature\": " + String(temperature) + "}";
    int httpResponseCode = http.POST(jsonData);

    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(10000); // ارسال هر 10 ثانیه
}

