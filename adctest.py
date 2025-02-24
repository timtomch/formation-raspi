import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Ouverture du bus I2C sur les pins SCL et SDA par défaut
i2c = busio.I2C(board.SCL, board.SDA)

# Initialisation d'un objet ADC via le bus I2C
ads = ADS.ADS1015(i2c)

# Initialisation des canaux
canal0 = AnalogIn(ads, ADS.P0)
canal1 = AnalogIn(ads, ADS.P1)
canal2 = AnalogIn(ads, ADS.P2)
canal3 = AnalogIn(ads, ADS.P3)

print("{:>5}\t{:>5}\t{:>5}\t{:>5}".format('A0', 'A1', 'A2', 'A3'))

while True:
        print("{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}".format(canal0.voltage,canal1.voltage,canal2.voltage,canal3.voltage))
        time.sleep(0.5)