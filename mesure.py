from gpiozero import LED
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Ouverture du bus I2C sur les pins SCL et SDA par défaut
i2c = busio.I2C(board.SCL, board.SDA)

# Initialisation d'un objet ADC via le bus I2C
ads = ADS.ADS1015(i2c)

# Initialisation des DELs
rouge = LED(23)
verte = LED(24)


# Mesure humidité sur canal 0
senseur = AnalogIn(ads, ADS.P0)

# Valeurs limites
trop_sec = 2.7
trop_humide = 2.0

while True:
        humidite_mesuree = senseur.voltage
        print(humidite_mesuree)
        
        if humidite_mesuree >= trop_sec:
            print('Trop sec')
            verte.off()
            rouge.on()
        elif humidite_mesuree <= trop_humide:
            print('Trop humide')
            verte.off()
            rouge.blink(0.2,2)
        else:
            print('Parfait!')
            rouge.off()
            verte.on()
        
        time.sleep(1)