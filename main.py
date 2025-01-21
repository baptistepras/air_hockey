import ratio
import pygame
import importlib
import init


class Bouton:
    def __init__(self, longueur, largeur, position, couleur_fond, arrondi=0, texte=None,
                 police="Polices/NotoSans-Black.ttf", taillepolice=10,
                 couleur_texte=None, fonction=None, compteurFonction=0):
        self.longueur = longueur
        self.largeur = largeur
        self.position = position
        self.couleur_fond = couleur_fond
        self.arrondi = arrondi
        self.texte = texte
        self.police = police
        self.taillepolice = taillepolice
        self.couleur_texte = couleur_texte
        self.fonction = fonction
        self.compteurFonction = compteurFonction
        self.font = pygame.font.Font(self.police, int(self.taillepolice * ratio.ratio))

    def affichage(self):
        if self.texte is None:
            pygame.draw.rect(ratio.interface, self.couleur_fond, (
            int(self.position[0] * ratio.ratio), int(self.position[1] * ratio.ratio), int(self.longueur * ratio.ratio),
            int(self.largeur * ratio.ratio)), 0, int(self.arrondi * ratio.ratio))
        else:
            pygame.draw.rect(ratio.interface, self.couleur_fond, (
            int(self.position[0] * ratio.ratio), int(self.position[1] * ratio.ratio), int(self.longueur * ratio.ratio),
            int(self.largeur * ratio.ratio)), 0, int(self.arrondi * ratio.ratio))
            txt = self.font.render(self.texte, True, self.couleur_texte)
            x, y = txt.get_size()
            ratio.interface.blit(txt, (- x / 2 + (self.longueur / 2 + self.position[0]) * ratio.ratio,
                                       - y / 2 + (self.largeur / 2 + self.position[1]) * ratio.ratio))

    def changerPolice(self):
        self.font = pygame.font.Font(self.police, int(self.taillepolice * ratio.ratio))

    def cliquer(self):
        # Pour chaque itération de rafraichissement
        pos = pygame.mouse.get_pos()
        if self.position[0] * ratio.ratio < pos[0] < (self.position[0] + self.longueur) * ratio.ratio and self.position[
            1] * ratio.ratio < pos[1] < (self.position[1] + self.largeur) * ratio.ratio:
            init.activation.play()
            Lancer(self.compteurFonction, self.fonction, self.texte)
            self.compteurFonction += 1


Titre = Bouton(1000, 70, (0, 0), init.grisfonce, 0, "Air Hockey", "Polices/NotoSans-Black.ttf", 38, init.blanc)
Jouer = Bouton(180, 60, (50, 130), init.orange, 7, "Jouer", "Polices/NotoSans-Black.ttf", 38, init.grisfonce, "Jouer")
Options = Bouton(180, 60, (50, 240), init.orange, 7, "Options", "Polices/NotoSans-Black.ttf", 38, init.grisfonce,
                 "Option")
# Stats = Bouton(180, 60, (50, 240), init.orange, 7, "Stats", "Polices/NotoSans-Black.ttf", 38, init.grisfonce)
# Succes = Bouton(180, 60, (50, 310), init.orange, 7, "Succès", "Polices/NotoSans-Black.ttf", 38, init.grisfonce)
Quitter = Bouton(180, 60, (50, 350), init.orange, 7, "Quitter", "Polices/NotoSans-Black.ttf", 38, init.grisfonce,
                 "Quitter")
liste_boutons = [Titre, Jouer, Options, Quitter]

titre_resolution = Bouton(150, 80, (800, 100), init.grisclair, 7, "Définition", "Polices/NotoSans-Bold.ttf", 30,
                          init.blanc)
taille1 = Bouton(150, 50, (810, 170), init.grissemi, 7, "1440 × 720", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                 "option_sec")
taille2 = Bouton(150, 50, (810, 225), init.grisfonce, 7, "1600 × 800", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                 "option_sec")
taille3 = Bouton(150, 50, (810, 280), init.grisfonce, 7, "2000 × 1000", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                 "option_sec")
taille4 = Bouton(150, 50, (810, 335), init.grisfonce, 7, "2160 × 1080", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                 "option_sec")
taille5 = Bouton(150, 50, (810, 390), init.grisfonce, 7, "3000 × 1500", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                 "option_sec")

titre_difficulte = Bouton(150, 80, (270, 100), init.grisclair, 7, "Difficulté", "Polices/NotoSans-Bold.ttf", 30,
                          init.blanc)
facile = Bouton(150, 50, (270, 170), init.grisfonce, 7, "Facile", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                "option_sec")
moyen = Bouton(150, 50, (270, 225), init.grissemi, 7, "Moyen", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
               "option_sec")
difficile = Bouton(150, 50, (270, 280), init.grisfonce, 7, "Difficile", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                   "option_sec")
expert = Bouton(150, 50, (270, 335), init.grisfonce, 7, "Expert", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
                "option_sec")

titre_temps = Bouton(150, 80, (450, 100), init.grisclair, 7, "Temps", "Polices/NotoSans-Bold.ttf", 30, init.blanc)
court = Bouton(150, 50, (450, 170), init.grissemi, 7, "2 minutes", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
               "option_sec")
long = Bouton(150, 50, (450, 225), init.grisfonce, 7, "5 minutes", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
              "option_sec")
temps_illimite = Bouton(150, 50, (450, 280), init.grisfonce, 7, "temps illimité", "Polices/NotoSans-Thin.ttf", 22,
                        init.blanc, "option_sec")

titre_score = Bouton(150, 80, (630, 100), init.grisclair, 7, "Points", "Polices/NotoSans-Bold.ttf", 30, init.blanc)
petit = Bouton(150, 50, (630, 170), init.grisfonce, 7, "5 points", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
               "option_sec")
grand = Bouton(150, 50, (630, 225), init.grisfonce, 7, "10 points", "Polices/NotoSans-Thin.ttf", 22, init.blanc,
               "option_sec")
score_illimite = Bouton(150, 50, (630, 280), init.grisfonce, 7, "points illimités", "Polices/NotoSans-Thin.ttf", 22,
                        init.blanc, "option_sec")

liste_boutons_optionnels1 = []
liste_boutons_optionnels2 = []
liste_boutons_optionnels3 = []
liste_boutons_optionnels4 = []


def Lancer(Compteur, Action="NONE", texte=None):
    global actualiser, init, jouer, liste_boutons, liste_boutons_optionnels1, liste_boutons_optionnels2, liste_boutons_optionnels3, liste_boutons_optionnels4, taille1, taille2, taille3, taille4, taille5, facile, moyen, difficile, expert, court, long, temps_illimite
    if Action == "Jouer":
        if Compteur == 0:
            import jouer
        else:
            importlib.reload(jouer)
        liste_boutons_optionnels1 = []
        liste_boutons_optionnels2 = []
        liste_boutons_optionnels3 = []
        liste_boutons_optionnels4 = []
    if Action == "Option":
        if Compteur % 2 == 0:
            liste_boutons_optionnels1 = [titre_resolution, taille1, taille2, taille3, taille4, taille5]
            liste_boutons_optionnels2 = [titre_difficulte, facile, moyen, difficile, expert]
            liste_boutons_optionnels3 = [titre_temps, court, long, temps_illimite]
            liste_boutons_optionnels4 = [titre_score, petit, grand, score_illimite]
            reinitialise1()
            if init.Ix == 1440:
                taille1.couleur_fond = init.grissemi
            elif init.Ix == 1600:
                taille2.couleur_fond = init.grissemi
            elif init.Ix == 2000:
                taille3.couleur_fond = init.grissemi
            elif init.Ix == 2160:
                taille4.couleur_fond = init.grissemi
            elif init.Ix == 3000:
                taille5.couleur_fond = init.grissemi
            reinitialise2()
            if ratio.difficulte == 0.7 * ratio.ratio ** 2:
                facile.couleur_fond = init.grissemi
            elif ratio.difficulte == 1 * ratio.ratio ** 2:
                moyen.couleur_fond = init.grissemi
            elif ratio.difficulte == 1.3 * ratio.ratio ** 2:
                difficile.couleur_fond = init.grissemi
            elif ratio.difficulte == 2 * ratio.ratio ** 2:
                expert.couleur_fond = init.grissemi
            reinitialise3()
            if init.temps == 1:
                court.couleur_fond = init.grissemi
            elif init.temps == 4:
                long.couleur_fond = init.grissemi
            elif init.temps == "∞":
                temps_illimite = init.grissemi
            reinitialise4()
            if init.score == 5:
                petit.couleur_fond = init.grissemi
            if init.score == 10:
                grand.couleur_fond = init.grissemi
            if init.score == "∞":
                score_illimite.couleur_fond = init.grissemi
        else:
            liste_boutons_optionnels1 = []
            liste_boutons_optionnels2 = []
            liste_boutons_optionnels3 = []
            liste_boutons_optionnels4 = []

    if Action == "option_sec":
        if texte == "1440 × 720":
            init.Ix = 1440
            reinitialise1()
            taille1.couleur_fond = init.grissemi
            importlib.reload(ratio)
            for bouton in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
                bouton.changerPolice()
        elif texte == "1600 × 800":
            init.Ix = 1600
            reinitialise1()
            taille2.couleur_fond = init.grissemi
            importlib.reload(ratio)
            for bouton in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
                bouton.changerPolice()
        elif texte == "2000 × 1000":
            init.Ix = 2000
            reinitialise1()
            taille3.couleur_fond = init.grissemi
            importlib.reload(ratio)
            for bouton in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
                bouton.changerPolice()
        elif texte == "2160 × 1080":
            init.Ix = 2160
            reinitialise1()
            taille4.couleur_fond = init.grissemi
            importlib.reload(ratio)
            for bouton in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
                bouton.changerPolice()
        elif texte == "3000 × 1500":
            init.Ix = 3000
            reinitialise1()
            taille5.couleur_fond = init.grissemi
            importlib.reload(ratio)
            for bouton in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
                bouton.changerPolice()
        elif texte == "Facile":
            ratio.difficulte = 0.7 * ratio.ratio ** 2
            reinitialise2()
            facile.couleur_fond = init.grissemi
        elif texte == "Moyen":
            ratio.difficulte = 1 * ratio.ratio ** 2
            reinitialise2()
            moyen.couleur_fond = init.grissemi
        elif texte == "Difficile":
            ratio.difficulte = 1.3 * ratio.ratio ** 2
            reinitialise2()
            difficile.couleur_fond = init.grissemi
        elif texte == "Expert":
            ratio.difficulte = 2 * ratio.ratio ** 2
            reinitialise2()
            expert.couleur_fond = init.grissemi
        elif texte == "2 minutes":
            init.temps = 1
            reinitialise3()
            court.couleur_fond = init.grissemi
        elif texte == "5 minutes":
            init.temps = 4
            reinitialise3()
            long.couleur_fond = init.grissemi
        elif texte == "temps illimité":
            init.temps = "∞"
            reinitialise3()
            temps_illimite.couleur_fond = init.grissemi
        elif texte == "5 points":
            init.score = 5
            reinitialise4()
            petit.couleur_fond = init.grissemi
        elif texte == "10 points":
            init.score = 10
            reinitialise4()
            grand.couleur_fond = init.grissemi
        elif texte == "points illimités":
            init.score = "∞"
            reinitialise4()
            score_illimite.couleur_fond = init.grissemi

    if Action == "Quitter":
        actualiser = False
    return True


def reinitialise1():
    global liste_boutons_optionnels1
    for bouton in liste_boutons_optionnels1[1:]:
        bouton.couleur_fond = init.grisfonce


def reinitialise2():
    global liste_boutons_optionnels2
    for bouton in liste_boutons_optionnels2[1:]:
        bouton.couleur_fond = init.grisfonce


def reinitialise3():
    global liste_boutons_optionnels3
    for bouton in liste_boutons_optionnels3[1:]:
        bouton.couleur_fond = init.grisfonce


def reinitialise4():
    global liste_boutons_optionnels4
    for bouton in liste_boutons_optionnels4[1:]:
        bouton.couleur_fond = init.grisfonce


actualiser = True

# Boucle de rafraichissement
while actualiser:
    ratio.interface.fill(init.grisclair)
    if Jouer.compteurFonction >= 1:
        if jouer.rejouer:
            importlib.reload(jouer)
    for i in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
        i.affichage()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Vérifie si une touche est pressée
            for i in liste_boutons + liste_boutons_optionnels1 + liste_boutons_optionnels2 + liste_boutons_optionnels3 + liste_boutons_optionnels4:
                if i.fonction is not None:
                    i.cliquer()
                # Vérifie l'évènement quit
        if event.type == pygame.QUIT:
            actualiser = False

    # Mise à jour de l'interface
    pygame.display.update()
pygame.display.quit()

# Fin du programme
pygame.quit()