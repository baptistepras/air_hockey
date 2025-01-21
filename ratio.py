import pygame
import init

ratio = init.Ix/1000
Iy = 500 * ratio
friction = 0.002 * ratio  # Friction de l'air du plot (À 0, le plot ne ralentit pas. À 1, le plot n'avance pas)
taux_freinage = 1 - friction  # Inversion du taux de freinage (servant notamment en cas de multiplication de vitesses)
margeCollision = 10 * ratio

interface = pygame.display.set_mode((init.Ix, Iy))  # Création de la fenêtre de Jeu
difficulte = 0.7 * ratio ** 2
vitesse_max = 5 * ratio**2

# Importation des polices
