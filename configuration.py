#!/usr/bin/env python
# -*- coding: utf-8 -*-

# configuration.py
#
# Permet la lecture du fichier preferences.cfg et d'en tirer le contenu

# Copyright (C) 2010 DOSSMANN Olivier
# Auteur : DOSSMANN Olivier
# Courriel : olivier@dossmann.net
#
# Ce logiciel est strictement réservé aux étudiants de la classe de 
#+ terminale Bac Pro du lycée Jean Geiler à Strasbourg pour l'année
#+ 2010/2011 dans le cadre de leurs études.
#
# La licence de ce logiciel évoluera a posteriori.

import configparser

class Preferences:
  nom_fichier = "preferences.cfg"

  def __init__(self):
    """Constructeur"""
    try:
      # Création d'un 'parseur'
      config = configparser.ConfigParser()
      # Ouverture du fichier de configuration
      config.readfp(open(self.nom_fichier))
    except:
      print("Erreur de lecture du fichier preferences.cfg ou fichier manquant.")

    # Récupération des éléments
    # Fichier où trouver les questions/réponses
    try:
      self.source = config.get('Configuration', 'fichier_source')
    except:
      self.source = "questions.txt"
    
    # Séparateur contenu dans le fichier source
    try:
      self.separation = config.get('Configuration', 'texte_de_separation')
    except:
      self.separation = "###"

    # Nombre de questions posées
    try:
      self.nbre_quest_pos = int(config.get('Configuration', 'nombre_de_questions_posees'))
    except:
      self.nbre_quest_pos = 20

    # Temps de pause entre chaque question (en secondes)
    try:
      self.tps_pause = int(config.get('Configuration', 'temps_de_pause_entre_chaque_question'))
    except:
      self.tps_pause = 10

  def __str__(self):
    """Affichage des préférences de l'utilisateur parmi :
    - Fichier à lire pour les questions
    - Texte de séparation entre les questions et réponses
    - Nombre de questions à poser
    - Temps de pause entre chaque question posée
    """
    return "Fichier lu : {}\nTexte de séparation : {}\nNombre de questions posées : {}\nTemps de pause entre chaque question (en secondes) : {}".format(self.source, self.separation, self.nbre_quest_pos, self.tps_pause)

