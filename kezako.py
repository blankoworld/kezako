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
questions = []            # Les questions initiales
longueur_questions = 0    # Nombre de questions dans KEZAKO
source = 'questions.txt'  # Fichier où trouver les questions/réponses
separateur = '###'        # Séparateur contenu dans le fichier source
nbre_questions = 3        # Nombre de questions posées
temps_pause = 2           # Temps de pause entre chaque question (en secondes)
lotterie = []             # Les numéros des questions non-posées
tirage = []               # Liste des numéros tirés
reponses = []             # Ensemble des réponses correspondantes

# Deboggage
deboggage = True

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

# Création d'une lotterie d'éléments contenant les questions non-posées
for i in range(0,longueur_questions - 1):
  # Ajout du numéro dans la lotterie
  lotterie.append(i)

# Affichage des questions
print(" QUESTIONS ".center(80, '='))

# Sortie d'un nombre défini de questions
for i in range(0,nbre_questions):
  # Recalcul de la capacité, en nombre, de la lotterie
  capacite_lotterie = len(lotterie)

  # Choix aléatoire d'un numéro dans la lotterie
  pioche_aleatoire = random.randint(0,capacite_lotterie - 1)

  # Récupération du contenu du numéro
  nbr_aleatoire = lotterie[pioche_aleatoire]

  # Ajout du numéro dans le tirage
  tirage.append(nbr_aleatoire)

  # Affichage de la question
  print("Question %d : %s" % (nbr_aleatoire, questions[nbr_aleatoire].split(separateur)[0]))

  # Suppression de l'élément dans la lotterie
  lotterie.remove(nbr_aleatoire)

  # Petite pause
  pause(temps_pause)

# Recherche des réponses
for i in tirage:
  reponses.append(questions[i].split(separateur)[1])

# Séparation avec la suite du programme
print("".center(80, '-'))

# Attente d'interaction avec l'utilisateur
input("Appuie sur Entrée dès que tu voudras afficher les réponses correspondantes.")

# Affichage des réponses
print(" REPONSES ".center(80, '='))
for nbre,reponse in zip(tirage,reponses):
  print("Question {} : {}".format(nbre, reponse.replace('\n', '')))

