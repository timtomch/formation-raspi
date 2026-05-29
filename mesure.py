from gpiozero import LED
import time
import board
import busio
from adafruit_ads1x15 import AnalogIn, ADS1015, ads1x15

# Ouverture du bus I2C sur les pins SCL et SDA par défaut
i2c = busio.I2C(board.SCL, board.SDA)

# Initialisation d'un objet ADC via le bus I2C
ads = ADS1015(i2c)

# Initialisation des DELs
rouge = LED(23)
verte = LED(24)


# Mesure humidité sur canal 0
senseur = AnalogIn(ads, ads1x15.Pin.A0)

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