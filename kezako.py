#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Déclaration des variables
questions = []
longueur_questions = 0
fichier = "questions.txt"

# Deboggage
deboggage = False

# Fonction de deboggage
def debug(texte):
  """Affiche la chaîne de caractère reçue si le programme est en mode deboggage"""
  if deboggage == True:
    print(str(texte))

# Fonctions

# Lecture du fichier
f = open(fichier, "r")

debug("Info : Fichier ouvert.")

# Ajout des questions
questions = f.readlines()

debug("Info : Questions ajoutées.")

# Fermeture du fichier
f.close()

debug("Info : Fichier fermé.")

# Lecture des questions
longueur_questions = len(questions)

debug("Info : Longueur du tableau : %s éléments" % longueur_questions)

# Choix aléatoire d'une question
nbr_aleatoire = random.randint(0,longueur_questions - 1)

debug("Info : Nombre aléatoire choisi %d." % nbr_aleatoire)

# Affichage de la question
print("Question %d : %s" % (nbr_aleatoire, questions[nbr_aleatoire]))
