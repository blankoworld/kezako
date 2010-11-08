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

from time import sleep as pause
from configuration import Preferences
from quiz import *

# Déclaration des variables
# Récupération dans le fichier de préférences
pref = Preferences()
source = pref.source                  # Fichier où trouver les questions/réponses
separateur = pref.separation          # Séparateur contenu dans le fichier source
nbre_questions = pref.nbre_quest_pos  # Nombre de questions posées
temps_pause = pref.tps_pause          # Temps de pause entre chaque questions
#+ (en secondes)

# Deboggage
deboggage = True

# Fonctions
# Fonction de deboggage
def debug(texte):
  """Affiche la chaîne de caractère reçue si le programme est en mode 
  deboggage.
  """
  if deboggage == True:
    print(str(texte))

# Début du programme
q = Questionnaire(source, separateur, nbre_questions)

# Affichage des questions
print(" QUESTIONS ".center(80, '='))
for el in q.elements:
  print("Question {} : {}".format(el.numero, el.question))
  # Petite pause
  pause(temps_pause)

# Séparation avec la suite du programme
print("".center(80, '-'))

# Attente d'interaction avec l'utilisateur
input("Appuie sur Entrée dès que tu voudras afficher les réponses correspondantes.")

# Affichage des réponses
print(" REPONSES ".center(80, '='))
for el in q.elements:
  print("Question {} : {}".format(el.numero, el.reponse))

# Séparation avec la suite du programme
print("".center(80, '-'))

# Attente d'interaction avec l'utilisateur pour la fin de programme
input("Appuie sur Entrée pour fermer le programme.")

