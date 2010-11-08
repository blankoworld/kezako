#!/usr/bin/env python
# -*- coding: utf-8 -*-

# quiz.py
#
# Copyright (C) 2010 DOSSMANN Olivier
# Auteur : DOSSMANN Olivier
# Courriel : olivier@dossmann.net
#
# Ensemble de classes permettant de gérer le questionnaire.

import random
from fichier import Fichier

class QuestionsReponses:
  """
  Stocke et délivre à la fois les questions et les réponses contenues
  dans un fichier source.
  """

  questions = []
  reponses = []

  def __init__(self, fichier_source, separateur):
    """Constructeur.

    <fichier_source> : Fichier source contenant les questions
    <separateur>     : Texte séparant les questions des réponses
    """
    self.fichier_source = fichier_source
    f = Fichier(fichier_source)
    contenu = f.contenu
    for ligne in contenu:
      elements = ligne.split(separateur)
      question = elements[0].replace('\n', '')
      reponse = elements[1].replace('\n', '')
      self.questions.append(question)
      self.reponses.append(reponse)

  def __str__(self):
    """Affichage d'informations."""
    return "Questions : {}\nRéponses : {}".format(self.questions, self.reponses)

class ElementQuestionReponse:
  """
  Un élément d'un ensemble de questions/réponses.
  Cet élément est composé d'une question et d'une réponse accolée
  """

  def __init__(self, numero, question, reponse):
    """Constructeur.

    <questions> : une liste ordonnée de questions
    <reponses> : une liste des réponses respectives aux questions
    """
    self.numero = numero
    self.question = question
    self.reponse = reponse

  def __str__(self):
    """Affichage d'informations."""
    return "Numéro de la question : {}\nQuestion : {}\nRéponse : {}".format(self.numero, self.question, self.reponse)

class Questionnaire:
  """
  Génère un questionnaire à partir d'un lot de questions et de réponses.
  """

  elements = []

  def __init__(self, fichier_source, separateur, nombre_questions):
    """Contructeur.

    <fichier_source> : fichier contenant les questions et les réponses
    <separateur> : chaîne de caractère séparant les réponses des questions
    <nombre_questions> : nombre de questions à mettre dans le questionnaire
    """

    # Récupération des questions et des réponses
    qr = QuestionsReponses(fichier_source, separateur)

    # Calcul de la taille des questions disponibles
    taille_questions = len(qr.questions)

    # Vérification sur le tirage de questions demandées
    if nombre_questions > taille_questions:
      nombre_questions = taille_questions

    # Ajout des questions et réponses (sous forme d'ElementQuestionReponse) 
    #+ dans un système de lotterie
    i = 0
    lotterie = []
    for question, reponse in zip(qr.questions, qr.reponses):
      el = ElementQuestionReponse(i, question, reponse)
      lotterie.append(el)
      i += 1

    # Sortie d'un nombre défini de questions et de réponses
    for i in range(0,nombre_questions):
      # Recalcul de la capacité, en nombre, de la lotterie
      capacite_lotterie = len(lotterie)

      # Choix aléatoire d'un élément dans la lotterie
      pioche_aleatoire = random.randint(0,capacite_lotterie - 1)

      # Récupération de cet élément et ajout dans le tirage final
      self.elements.append(lotterie[pioche_aleatoire])

      # Suppression de l'élément dans la lotterie
      lotterie.remove(lotterie[pioche_aleatoire])

  def __str__(self):
    """Affichage des éléments issus du tirage de la lotterie."""
    chaine = ""
    for element in elements:
      ligne = "{}\t: {}\t\t{}\n".format(element.numero, element.question, element.reponse)
      chaine += ligne
    return "Elements : \n{}".format(chaine)

