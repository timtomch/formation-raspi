from gpiozero import LED
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import logging

# Définition du fichier de log
logging.basicConfig(filename='humidite.log',level=logging.INFO,format='%(asctime)s %(message)s')

# Intervalle de mesure (en secondes)
intervalle = 30

# Ouverture du bus I2C sur les pins SCL et SDA par défaut
i2c = busio.I2C(board.SCL, board.SDA)

# Initiation d'un objet ADC via le bus I2C
ads = ADS.ADS1015(i2c)

# Initiation des DELs
rouge = LED(23)
verte = LED(24)


# Mesure humidité sur canal 0
senseur = AnalogIn(ads, ADS.P0)

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
        
        logging.info("{:>5.4f}\t{:>5}".format(humidite_mesuree,statut_plante))
        time.sleep(intervalle)