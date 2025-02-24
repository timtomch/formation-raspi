from flask import Flask, render_template
from collections import deque
import os

app = Flask(__name__)

# Cette fonction permet de ne prendre que les n dernières lignes d'un fichier
def tail(file_path, n):
	with open(file_path, 'rb') as file:
		return deque(file, maxlen=n) 
        
# Cette fonction lit les données provenant du fichier de log.
def lire_donnees():
	fichier = '~/humidite.log'
    # On utilise la fonction os.path.expanduser pour remplacer le '~' par le chemin d'accès complet.
	donnees = tail(os.path.expanduser(fichier),100)
    # On initialise une série de listes vides qui serviront à contenir les données extraites
	temps = []
	humidite = []
	statut = []
    # On passe au travers de chaque ligne du fichier et on extrait les données
	for ligne in donnees:
        # La fonction decode() sert à convertir les données binaires en texte
		ligne = ligne.decode()
        # On sépare chaque ligne en utilisant la tabulation
		valeurs = ligne.split('\t')
        # Puis on ajoute à chacune des listes les données qu'on a extraites
		temps.append(valeurs[0])
		humidite.append(valeurs[1])
		statut.append(valeurs[2])
	return temps, humidite, statut

@app.route('/')
def index():
    # Appel de la fonction pour lire les données
	temps, humidite, statut = lire_donnees()
    # On calcule la longueur des listes que l'on a obtenu
	nombre_donnees = len(temps)
    # On utilise cette longueur pour obtenir la dernière valeur de statut
    # On utilise la fonction strip() pour ôter d'éventuels espaces superflus
	statut_actuel = statut[nombre_donnees-1].strip()
    # En fonction du statut, choisir une couleur, une image et un message personnalisé
	if statut_actuel == 'ok':
		image = 'plante-heureuse.png'
		message_statut = "Tout va bien!"
		couleur = "#baffc9"
	elif statut_actuel == 'sec':
		image = 'plante-seche.png'
		message_statut = "J'ai soif!"
		couleur = "#ffdfba"
	elif statut_actuel == 'humide':
		image = 'plante-inondee.png'
		message_statut = "Je me noie!"
		couleur = "#bae1ff"
	else:
		image = ''
		message_statut = "Données manquantes"
    # On construit l'objet contenant les données à envoyer au gabarit
	pour_affichage = {
		'derniere_maj': temps[nombre_donnees-1],
		'humidite_actuelle': humidite[nombre_donnees-1],
		'message': message_statut,
		'image': image,
		'couleur': couleur,
        'temps_valeurs': temps,
        'humidite_valeurs': humidite
	}
    # Appel du gabarit. Noter les deux étoiles pour "déballer" l'objet de données.
	return render_template('index.html', **pour_affichage)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')