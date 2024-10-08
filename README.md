# imu

### Requirements

Install python3-smbus:
````bash
sudo apt install python3-smbus
````
Install the mqtt library:
````bash
sudo apt install paho-mqtt
````
Install library to use the mpu6050 IMU with a raspberry pi:
````bash
sudo pip install mpu6050-raspberrypi
````

### Configure
| Key                    | Default                      | Definition                             |
| ---------------------- | ---------------------------- | -------------------------------------- |
| mqtt.broker            | 192.168.22.253               | IP address of mqtt broker              |
| mqtt.port              | 1883                         | port of the mqtt process on the broker |
| mqtt.topic             | supercoolcar/imu             | topic containing data of gyro and acc  |
| mqtt.temperature_topic | supercoolcar/imu-temperature | topic containing the temperature       |
| address                | 0x68                         | i2c address                            |
| sleepTimer             | 2                            | time between each message              |

### Run this project
````bash
sudo python3 imu.py
````
