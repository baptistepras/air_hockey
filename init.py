import pygame
from math import *
from random import *

# Introduction du programme
noir = (0, 0, 0)
blanc = (255, 255, 255)
vert = (0, 255, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
bleufonce = (0, 0, 155)
orange = (255, 136, 0)
grisclair = (33, 47, 56)
grissemi = (20, 33, 44)
grisfonce = (8, 20, 32)
couleur = [noir, blanc, vert, rouge, bleu]
temps = 1
score = 5

pygame.init()  # Intialisation du module Pygame
pygame.display.set_caption("AIR HOCKEY !")  # Création du nom de la fenêtre
var_jouer = False

Ix = 1440

fin_temps = pygame.mixer.Sound('Sound Effect Air Hockey/Timer 12sec.wav')
activation = pygame.mixer.Sound('Sound Effect Air Hockey/Activation.wav')
ost = pygame.mixer.Sound('Sound Effect Air Hockey/OST 1.wav')
ost2 = pygame.mixer.Sound('Sound Effect Air Hockey/OST 2.wav')
satisfaisant = pygame.mixer.Sound('Sound Effect Air Hockey/Satisfaisant.wav')
echec = pygame.mixer.Sound('Sound Effect Air Hockey/Échec.wav')
defaite = pygame.mixer.Sound('Sound Effect Air Hockey/Défaite cuisante.wav')
victoire = pygame.mixer.Sound('Sound Effect Air Hockey/Bien joué.wav')
egalite = pygame.mixer.Sound('Sound Effect Air Hockey/Bien joué.wav')
nouvelle_partie = pygame.mixer.Sound('Sound Effect Air Hockey/Nouvelle Partie.wav')
frappe = pygame.mixer.Sound('Sound Effect Air Hockey/Frappe.wav')
rebond = pygame.mixer.Sound('Sound Effect Air Hockey/Rebond.wav')