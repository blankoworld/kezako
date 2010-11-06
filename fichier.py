#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fichier.py
#
# Classe qui permet(tra) de lire le contenu d'un fichier en vue de l'utiliser
#+ pour le logiciel KEZAKO http://git.dossmann.net/?p=projets/kezako;a=summary

from os import path

class Fichier:
    def __init__(self, nom):
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
            return "Nom du fichier : %s, Nom court : %s" % (self.nom, self.nom_court)

    def existant(self):
            if path.exists(self.nom) and path.isfile(self.nom):
                return True
            else:
                return False

