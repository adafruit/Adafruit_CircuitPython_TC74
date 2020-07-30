import time
import board
import busio
import adafruit_tc74
i2c = busio.I2C(board.SCL, board.SDA)

tc = adafruit_tc74.TC74(i2c)

while True:
    print(f"Temperature: {tc.temperature} C")
    time.sleep(0.5)
