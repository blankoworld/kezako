#!/usr/bin/env python
# -*- coding: utf-8 -*-

# kezako.py

# Copyright (C) 2010 DOSSMANN Olivier
# Auteur : DOSSMANN Olivier
# Courriel : olivier@dossmann.net
#
# Ce logiciel est strictement réservé aux étudiants de la classe de 
#+ terminale Bac Pro du lycée Jean Geiler à Strasbourg pour l'année
#+ 2010/2011 dans le cadre de leurs études.
#
# La licence de ce logiciel évoluera a posteriori.

import random
from time import sleep as pause
from fichier import Fichier

# Déclaration des variables
questions = []            # Les questions
longueur_questions = 0    # Nombre de questions dans KEZAKO
source = 'questions.txt'  # Fichier où trouver les questions/réponses
separateur = '###'        # Séparateur contenu dans le fichier source
nbre_questions = 3        # Nombre de questions posées
temps_pause = 2           # Temps de pause entre chaque question (en secondes)

# Deboggage
deboggage = False

# Fonctions
# Fonction de deboggage
def debug(texte):
  """Affiche la chaîne de caractère reçue si le programme est en mode 
  deboggage
  """
  if deboggage == True:
    print(str(texte))

# Début du programme

fichier = Fichier(source)

# Ajout des questions
questions = fichier.contenu

# Lecture des questions
longueur_questions = len(questions)

# Sortie d'un nombre défini de questions
for i in range(0,nbre_questions):
  # Choix aléatoire d'une question
  nbr_aleatoire = random.randint(0,longueur_questions - 1)

  # Affichage de la question
  print("Question %d : %s" % (nbr_aleatoire, questions[nbr_aleatoire].split(separateur)[0]))

  # Petite pause
  pause(temps_pause)
