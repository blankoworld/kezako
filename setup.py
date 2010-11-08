#!/usr/bin/env python

from distutils.core import setup

setup(name = 'kezako',
      description = "Outil qui pose des questions suivant un fichier texte donné et renvoie les réponses respectives en fin de traitement.", 
      author = "Olivier DOSSMANN",
      author_email = "olivier@dossmann.net",
      url = "http://git.dossmann.net/?p=projets/kezako",
      version = '0.5.1',
      py_modules = ['fichier', 'configuration', 'quiz', 'kezako'],
      scripts = ['preferences.cfg','questions.txt', 'LISMOI'],
)

