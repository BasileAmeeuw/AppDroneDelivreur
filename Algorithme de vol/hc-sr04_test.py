import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D14, echo_pin=board.D15)

while True:
    try:
        print(sonar.distance)
    except:
        print("Retrying!")
    time.sleep(0.5)