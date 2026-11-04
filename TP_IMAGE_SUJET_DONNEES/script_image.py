# TP INFO : Programmation impérative : visualisation des images manipulées
# appel depuis le shell : python3 script_image.py
# vérifier votre répertoire de travail


# bibliothèques à importer
import numpy as np               # pour la gestion des tableaux de type array
import matplotlib as mp          # pour travailler avec tout type de figures
import matplotlib.pyplot as plt  # pour tracer des figures
import os                        # pour les fonctionalités dépendantes du système d'explotation (os)


# mémorisation du chemin vers le dossier contenant les données à traiter
# à adapter en fonction de votre home 
PATH = '/Users/ferrane/Documents/ENSEIGNEMENT/SRI-1A/TP_INFO/TP_IMAGE/TP_IMAGE_SUJET_DONNEES/'

# siasir du fichier .dat à traiter
nom_fichier = input('Image à afficher')

# récupération du nom sans l'extension
nom_seul, ext = os.path.splitext(nom_fichier)
print(nom_seul, ext)

# ouverture du fichier .dat (fichier texte) et conversion en array
fichier = open(PATH + nom_fichier, "r")

# lecture de la première ligne contenant la hauteur et la largeur de la matrice
ligne_dim = fichier.readline()
liste_dim = ligne_dim.split()
print('TRACE Dimensions = ', liste_dim)
val_dim = [int(val) for val in liste_dim]
hauteur = val_dim[0]
largeur = val_dim[1]

print('TRACE valeurs dimensions après conversion = ', ligne_dim, ' = ', hauteur, ' x ', largeur)

# définition d'une matrice d'entiers à la bonne dimension
image_lue = np.zeros((hauteur, largeur), dtype=int)

# chargement ligne par ligne de la matrice à partir du fichier texte
for i in range(1,hauteur+1) :
    ligne_fichier = fichier.readline()
    liste_valeur = ligne_fichier.split()
    #print(liste_valeur)
    image_lue[i-1] = [int(val) for val in liste_valeur]

# affichage du contenu de la matrice
print(image_lue)

# fermeture du fichier initialement ouvert
fichier.close()

# affichage de la matrice comme une image en niveaux de gris
plt.imshow(image_lue,cmap='gray')

# sauvegarde au format jpg
plt.savefig(PATH + nom_seul + '.jpg')
print('TRACE image sauvegardée au format jpg : ', PATH + nom_seul + '.jpg')
