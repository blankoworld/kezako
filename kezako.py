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
from fichier import Fichier

# Déclaration des variables
questions = []
longueur_questions = 0
source = "questions.txt"

# Deboggage
deboggage = False

# Fonction de deboggage
def debug(texte):
  """Affiche la chaîne de caractère reçue si le programme est en mode deboggage"""
  if deboggage == True:
    print(str(texte))

# Fonctions
# Aucune actuellement

fichier = Fichier(source)

debug("Info : Fichier ouvert.")

# Ajout des questions
questions = fichier.contenu

debug("Info : Questions ajoutées.")

# Lecture des questions
longueur_questions = len(questions)

debug("Info : Longueur du tableau : %s éléments" % longueur_questions)

# Choix aléatoire d'une question
nbr_aleatoire = random.randint(0,longueur_questions - 1)

debug("Info : Nombre aléatoire choisi %d." % nbr_aleatoire)

# Affichage de la question
print("Question %d : %s" % (nbr_aleatoire, questions[nbr_aleatoire].split('###')[0]))
