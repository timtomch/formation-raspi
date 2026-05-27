import time
import board
import busio
from adafruit_ads1x15 import AnalogIn, ADS1015, ads1x15

# Ouverture du bus I2C sur les pins SCL et SDA par défaut
i2c = busio.I2C(board.SCL, board.SDA)

# Initialisation d'un objet ADC via le bus I2C
ads = ADS1015(i2c)

# Initialisation des canaux
canal0 = AnalogIn(ads, ads1x15.Pin.A0)
canal1 = AnalogIn(ads, ads1x15.Pin.A1)
canal2 = AnalogIn(ads, ads1x15.Pin.A2)
canal3 = AnalogIn(ads, ads1x15.Pin.A3)

print("{:>5}\t{:>5}\t{:>5}\t{:>5}".format('A0', 'A1', 'A2', 'A3'))

while True:
        print("{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}".format(canal0.voltage,canal1.voltage,canal2.voltage,canal3.voltage))
        time.sleep(0.5)