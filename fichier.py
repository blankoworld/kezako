#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fichier.py
#
# Classe qui permet(tra) de lire le contenu d'un fichier en vue de l'utiliser
#+ pour le logiciel KEZAKO http://git.dossmann.net/?p=projets/kezako;a=summary

# Copyright (C) 2010 DOSSMANN Olivier
# Auteur : DOSSMANN Olivier
# Courriel : olivier@dossmann.net
#
# Ce logiciel est strictement réservé aux étudiants de la classe de 
#+ terminale Bac Pro du lycée Jean Geiler à Strasbourg pour l'année
#+ 2010/2011 dans le cadre de leurs études.
#
# La licence de ce logiciel évoluera a posteriori.

from os import path

class Fichier:
  def __init__(self, nom):
    """Constructeur

    <nom> : Nom du fichier à lire
    """
    self.nom = nom
    self.nom_court = path.splitext(nom)[0]
    if self.existant:
        try:
            f = open(nom, 'r')
            self.contenu = f.readlines()
            f.close()
        except:
            print("Erreur de lecture du fichier.")
            self.contenu = {}

  def __str__(self):
    """Affichage d'informations : 

    - Nom du fichier
    - Nom court du fichier (sans extension)
    """
    return "Nom du fichier : %s, Nom court : %s" % (self.nom, self.nom_court)

  def existant(self):
    """Retourne vrai ou faux selon que le fichier existe ou non."""
    if path.exists(self.nom) and path.isfile(self.nom):
      return True
    else:
      return False

