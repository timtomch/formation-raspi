from gpiozero import LED
import time
import board
import busio
from adafruit_ads1x15 import AnalogIn, ADS1015, ads1x15
import logging
import os

# Définition du fichier de log
logging.basicConfig(filename=os.path.expanduser('~/humidite.log'),level=logging.INFO,format='%(asctime)s\t%(message)s')

# Intervalle de mesure (en secondes)
intervalle = 30

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

# Variable de statut
statut_plante = 'ok'

while True:
        humidite_mesuree = senseur.voltage
        
        if humidite_mesuree >= trop_sec:
            statut_plante = 'sec'
            verte.off()
            rouge.on()
        elif humidite_mesuree <= trop_humide:
            statut_plante = 'humide'
            verte.off()
            rouge.blink(0.2,2)
        else:
            statut_plante = 'ok'
            rouge.off()
            verte.on()
        
        logging.info("{:>5.4f}\t{:}".format(humidite_mesuree,statut_plante))
        time.sleep(intervalle)