#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Déclaration des variables
questions = []
longueur_questions = 0

# Deboggage
deboggage = False

# Fonction de deboggage
def debug(texte):
  """Affiche la chaîne de caractère reçue si le programme est en mode deboggage"""
  if deboggage == True:
    print(str(texte))

# Fonctions

# Ajout des questions
questions.append("De quelle couleur est le cheval blanc d'Henri IV ?")
questions.append("Comment se nomme Albert ?")
questions.append("Pourquoi la vie ?")
questions.append("Où as-tu trouvé ce programme ?")
questions.append("Combien de questions peut contenir ce programme ?")

debug("Info : Questions ajoutées.")

# Lecture des questions
longueur_questions = len(questions)

debug("Info : Longueur du tableau : %s éléments" % longueur_questions)

# Choix aléatoire d'une question
nbr_aleatoire = random.randint(0,longueur_questions - 1)

debug("Info : Nombre aléatoire choisi %d." % nbr_aleatoire)

# Affichage de la question
print("Question : %s" % questions[nbr_aleatoire])
