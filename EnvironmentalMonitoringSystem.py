import time
import random
import json
from datetime import datetime

class SensorSimulator:
    def __init__(self, min_temp=15, max_temp=35, min_humidity=30, max_humidity=70):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity

    def read_temperature(self):
        # Simulate temperature readings between min_temp and max_temp
        return round(random.uniform(self.min_temp, self.max_temp), 2)

    def read_humidity(self):
        # Simulate humidity readings between min_humidity and max_humidity
        return round(random.uniform(self.min_humidity, self.max_humidity), 2)

class EnvironmentMonitor:
    def __init__(self, sensor, temp_threshold=30, humidity_threshold=60):
        self.sensor = sensor
        self.temp_threshold = temp_threshold
        self.humidity_threshold = humidity_threshold

    def log_data(self, temperature, humidity):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "timestamp": timestamp,
            "temperature": temperature,
            "humidity": humidity
        }
        # Append data to a log file as JSON
        with open("environment_log.json", "a") as log_file:
            log_file.write(json.dumps(data) + "\n")
        print(f"Logged data: {data}")

    def send_alert(self, temperature, humidity):
        if temperature > self.temp_threshold:
            print(f"Alert! High temperature detected: {temperature}°C")
        if humidity > self.humidity_threshold:
            print(f"Alert! High humidity detected: {humidity}%")

    def check_environment(self):
        # Simulate reading from the sensors
        temperature = self.sensor.read_temperature()
        humidity = self.sensor.read_humidity()
        
        # Log the readings
        self.log_data(temperature, humidity)

        # Check if readings exceed thresholds and send an alert
        if temperature > self.temp_threshold or humidity > self.humidity_threshold:
            self.send_alert(temperature, humidity)

# Set up the sensor simulator and monitor
sensor_simulator = SensorSimulator()
environment_monitor = EnvironmentMonitor(sensor_simulator)

# Simulate periodic environment checks
for _ in range(10):  # Number of readings
    environment_monitor.check_environment()
    time.sleep(2)  # Wait for 2 seconds between readings
