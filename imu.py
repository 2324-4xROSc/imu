from paho.mqtt import client as mqtt_client
from time import sleep
import mpu6050
import json

broker = '192.168.22.253'
port = 1883
topic = "supercoolcar/imu"
temperature_topic = "supercoolcar/imu-temperature"
client_id = "imu"

# Create a new Mpu6050 object
mpu6050 = mpu6050.mpu6050(0x68)

# Define a function to read the sensor data
def read_sensor_data():
    # Read the accelerometer values
    accelerometer_data = mpu6050.get_accel_data()

    # Read the gyroscope values
    gyroscope_data = mpu6050.get_gyro_data()

    # Read temp
    temperature = mpu6050.get_temp()

    return accelerometer_data, gyroscope_data, temperature

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    while True:
        accelerometer_data, gyroscope_data, temperature = read_sensor_data()
        data = {
            "accelerometer": accelerometer_data,
            "gyro": gyroscope_data
        }

        temperatureData = {
            "temperature": temperature
        }

        msg = json.dumps(data)
        temperature_msg = json.dumps(temperatureData)

        client.publish(topic, msg)
        client.publish(temperature_topic, temperature_msg)

        sleep(2)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()