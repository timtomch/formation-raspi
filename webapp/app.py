from flask import Flask, render_template
from collections import deque

app = Flask(__name__)

def tail(file_path, n):
	with open(file_path, 'rb') as file:
		return deque(file, maxlen=n) 

def lire_donnees():
	fichier = '/home/thomas/humidite.log'
	donnees = tail(fichier,1000)
	temps = []
	humidite = []
	statut = []
	for ligne in donnees:
		ligne = ligne.decode()
		valeurs = ligne.split('\t')
		temps.append(valeurs[0])
		humidite.append(valeurs[1])
		statut.append(valeurs[2])
	return temps, humidite, statut

@app.route('/')
def index():
	temps, humidite, statut = lire_donnees()
	nombre_donnees = len(temps)
	statut_actuel = statut[nombre_donnees-1].strip()
	if statut_actuel == 'ok':
		image = 'plante-heureuse.png'
		message_statut = "Tout va bien!"
	elif statut_actuel == 'sec':
		image = 'plante-seche.png'
		message_statut = "J'ai soif!"
	elif statut_actuel == 'humide':
		image = 'plante-inondee.png'
		message_statut = "Je me noie!"
	else:
		image = ''
		message_statut = "Données manquantes"
	pour_affichage = {
		'derniere_maj': temps[nombre_donnees-1],
		'humidite_actuelle': humidite[nombre_donnees-1],
		'message': message_statut,
		'image': image
	}
	return render_template('index.html', **pour_affichage)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')