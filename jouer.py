import pygame.event
from init import *
from ratio import *

nouvelle_partie.play()
if difficulte == 1 * ratio ** 2:
    ost2.play()
else:
    ost.play()
class Plot:
    def __init__(self, posplotx, posploty, couleur, taille_plot, joueur, mode):
        self.posplotx = posplotx
        self.posploty = posploty
        self.ancPlotX = posplotx
        self.ancPlotY = posploty
        self.couleur = couleur
        self.taille_plot = taille_plot * ratio
        self.joueur = joueur
        self.mode = mode

    def deplacement(self):
        if self.mode == "souris":
            sourisx, sourisy = pygame.mouse.get_pos()

            # Élasticité
            self.posplotx = (sourisx + self.ancPlotX * (20 / ratio**2)) / ((20 / ratio**2) + 1)
            self.posploty = (sourisy + self.ancPlotY * (20 / ratio**2)) / ((20 / ratio**2) + 1)

        elif self.mode == "ia":
            # Déplacement de l'ia
            if Palet1.posX > Ix / 2 - Palet1.taille_palet:
                if self.posplotx > Ix / 7:
                    self.posplotx -= 1 * difficulte
                if self.posploty > Iy // 2 + Palet1.taille_palet:
                    self.posploty -= 1 * difficulte
                if self.posploty < Iy // 2 - Palet1.taille_palet:
                    self.posploty += 1 * difficulte
            elif self.posplotx > Palet1.posX - Palet1.taille_palet:
                self.posplotx -= 1 * difficulte
            elif Palet1.posY - Palet1.taille_palet * 2 < self.posploty < Palet1.posY + Palet1.taille_palet * 2 and Palet1.posX > Iy / 2:
                self.posplotx += 2 * difficulte
            elif Palet1.posY + Palet1.taille_palet * 2 > self.posploty > Palet1.posY - Palet1.taille_palet * 2 and Palet1.posX < Iy / 2:
                self.posplotx += 2 * difficulte
            else:
                self.posplotx = (Palet1.posX + self.ancPlotX * (200 / difficulte)) / (200 / difficulte + 1)
                self.posploty = (Palet1.posY + self.ancPlotY * (200 / difficulte)) / (200 / difficulte + 1)


        # Limitation de jouabilité
        if self.joueur == 1:
            if self.posplotx - self.taille_plot < Ix / 2:
                self.posplotx = Ix / 2 + self.taille_plot
        if self.joueur == 2:
            if self.posplotx + self.taille_plot > Ix / 2:
                self.posplotx = Ix / 2 - self.taille_plot
        pygame.draw.circle(interface, self.couleur, (self.posplotx, self.posploty), self.taille_plot)
        return None

    def set_ancienne_position(self):
        self.ancPlotX = self.posplotx
        self.ancPlotY = self.posploty


class Palet:
    def __init__(self, posX, posY, vitesseX, vitesseY, couleur, taille_palet):
        self.posX = posX
        self.posY = posY
        self.vitesseX = vitesseX
        self.vitesseY = vitesseY
        self.ancVitesseX = vitesseX
        self.ancVitesseY = vitesseY
        self.couleur = couleur
        self.taille_palet = taille_palet * ratio

    def deplacement(self):
        # Collisions bord
        for i in ListeCage:
            if self.posX > Ix - self.taille_palet:
                if not (Iy // 2 - i.taille // 2 + self.taille_palet / 1.9 < self.posY < Iy // 2 + i.taille // 2 - self.taille_palet / 1.9) and self.vitesseX > 0:
                    rebond.play()
                    self.vitesseX *= -1
            if self.posX - self.taille_palet < 0:
                if not (Iy // 2 - i.taille // 2 + self.taille_palet / 1.9 < self.posY < Iy // 2 + i.taille // 2 - self.taille_palet / 1.9) and self.vitesseX < 0:
                    rebond.play()
                    self.vitesseX *= -1
            if self.posY > Iy - self.taille_palet:
                if self.vitesseY > 0:
                    rebond.play()
                    self.vitesseY *= -1
            if self.posY - self.taille_palet < 0:
                if self.vitesseY < 0:
                    rebond.play()
                    self.vitesseY *= -1


        # Freinage du palet
        self.vitesseX *= taux_freinage
        self.vitesseY *= taux_freinage

        # Application de la vitesse
        self.posX += self.vitesseX
        self.posY += self.vitesseY

        if self.vitesseX >= vitesse_max:
            self.vitesseX = vitesse_max
        if self.vitesseX <= -vitesse_max:
            self.vitesseX = -vitesse_max
        if self.vitesseY >= vitesse_max:
            self.vitesseY = vitesse_max
        if self.vitesseY <= -vitesse_max:
            self.vitesseY = -vitesse_max

        # Affichage
        pygame.draw.circle(interface, (255, 150, 0), (self.posX, self.posY), self.taille_palet)

    def set_ancienne_position(self):
        if self.vitesseX != 0:
            self.ancVitesseX = self.vitesseX
        if self.vitesseY != 0:
            self.ancVitesseY = self.vitesseY

class Cage:
    def __init__(self, taille, score, position):
        self.taille = taille * ratio
        self.score = score
        self.position = position


    def but(self, Cage_gagnante):
        if self.position == "gauche":
            # Détection de but dans la cage de gauche
            if Palet1.posX < -Palet1.taille_palet + 5:
                Palet1.vitesseX = 0
                Palet1.vitesseY = 0
                Palet1.posX = Ix / 3
                Palet1.posy = Iy / 2
                satisfaisant.play()
                Cage_gagnante.score += 1
            # Affichage de la cage
            pygame.draw.rect(interface, orange, (0, Iy // 2 - self.taille // 2, 4 * ratio, self.taille))
        if self.position == "droite":
            # Détection de but dans la cage de droite
            if Palet1.posX > Ix + Palet1.taille_palet - 5:
                Palet1.vitesseX = 0
                Palet1.vitesseY = 0
                Palet1.posX = Ix / 1.5
                Palet1.posy = Iy / 2
                echec.play()
                Cage1.score += 1
            # Affichage de la cage
            pygame.draw.rect(interface, orange, (Ix - 4 * ratio, Iy // 2 - self.taille // 2, 5 * ratio, self.taille))



Plot1 = Plot(0, 0, (255, 255, 255), 30, 1, "souris")
Plot2 = Plot(Ix/8, Iy/2, (255, 255, 255), 30, 2, "ia")
Palet1 = Palet(Ix/2, Iy/2, 0, 0, (255, 150, 0), 20)
Cage1 = Cage(120, 0, "gauche")
Cage2 = Cage(120, 0, "droite")
ListePlots = [Plot2, Plot1]
ListePalet = [Palet1]
ListeCage = [Cage2, Cage1]

# Création du chronomètre
chrono = pygame.time.Clock()
depart = pygame.time.get_ticks()
timeout = False
temps_str = '0:00'
temps_restant = temps
compteur = 0
rejouer = False
resultat = False
actualiser = True
actualiser2 = False
minutes = "0"
secondes = "0"
compteur_fin = True
test_minutes = False
# boucle de rafraichissement
while actualiser:
    # Mise à jour des déplacements
    interface.fill(grisfonce)
    # Dessin des lignes du terrain
    pygame.draw.rect(interface, orange, (Ix // 2 - 4 * ratio, 0, 8 * ratio, Iy // 2 - 25 * ratio))
    pygame.draw.rect(interface, orange, (Ix // 2 - 4 * ratio, Iy // 2 + 25 * ratio, 8 * ratio, Iy // 2))
    pygame.draw.circle(interface, orange, (Ix//2, Iy//2), 25 * ratio, int(5 * ratio))
    Plot1.deplacement()
    Plot2.deplacement()
    Palet1.deplacement()
    Cage1.but(Cage2)
    Cage2.but(Cage1)
    # Calcul du temps
    if temps != "∞":
        secondes = (pygame.time.get_ticks() - depart) / 1000
        minutes = str(temps_restant - int(secondes // 60))
        secondes = str(59 - int(secondes % 60))
        if minutes == "0" and secondes == "12" and compteur_fin:
            fin_temps.play()
            compteur_fin = False
        if minutes == "0" and secondes == "0":
            if Cage1.score > Cage2.score:
                resultat = "defaite"
            elif Cage2.score > Cage1.score:
                resultat = "victoire"
            else:
                resultat = "egalite"
            actualiser = False
    else:
        if secondes == "00" and test_minutes:
            test_minutes = False
            minutes = str(int(minutes) + 1)
            secondes = "0"
        elif secondes == "01":
            test_minutes = True
            secondes = str(int((pygame.time.get_ticks() - depart) / 1000) % 60)
        else:
            secondes = str(int((pygame.time.get_ticks() - depart) / 1000) % 60)
    if len(secondes) == 1:
        secondes = '0' + secondes
    if len(minutes) == 1:
        minutes = '0' + minutes
    Affichage_temps = pygame.font.Font("Polices/NotoSans-Black.ttf", int(40 * ratio)).render(minutes + " : " + secondes, True, ((255, 255, 255)))
    interface.blit(Affichage_temps, ((Ix / 2) - (Affichage_temps.get_rect().width / 2), 85 * ratio))

    Affichage_score = pygame.font.Font("Polices/NotoSans-Black.ttf", int(60 * ratio)).render(str(Cage1.score) + " : " + str(Cage2.score), True, ((255, 255, 255)))
    interface.blit(Affichage_score, ((Ix / 2) - (Affichage_score.get_rect().width / 2), 15 * ratio))
    # Détection de la collision
    for plot in ListePlots:
        for palet in ListePalet:
            distanceX = plot.posplotx - palet.posX
            distanceY = plot.posploty - palet.posY
            distance = sqrt((plot.posplotx - palet.posX) ** 2 + (plot.posploty - palet.posY) ** 2)
            if distance < (plot.taille_plot + palet.taille_palet):
                angleCos = acos(distanceY / distance) / pi * 180
                angleSin = asin(distanceX / distance) / pi * 180
                # Calcul d'angle de collision
                if angleSin >= 0:
                    # Premier quartier du cercle (0-90°)
                    if angleCos >= 90:
                        angleReel = angleCos - 90
                    # Quatrième quartier du cercle (270-360°)
                    else:
                        angleReel = 270 + angleCos
                else:
                    # Deuxieme quartier du cercle (90-180°)
                    if angleCos >= 90:
                        angleReel = -angleSin + 90
                    # Troisieme quartier du cercle (180-270°)
                    else:
                        angleReel = 270 - angleCos
                # Calcul d'angle d'attaque
                vecteurX = plot.posplotx - plot.ancPlotX
                vecteurY = plot.posploty - plot.ancPlotY
                forceTotale = sqrt(vecteurX ** 2 + vecteurY ** 2) + (sqrt((palet.vitesseX + palet.vitesseY) ** 2)) / 1.5
                palet.vitesseX = -cos(angleReel / 360 * 2 * pi) * forceTotale * (
                            plot.taille_plot + palet.taille_palet) / distance
                palet.vitesseY = sin(angleReel / 360 * 2 * pi) * forceTotale * (
                            plot.taille_plot + palet.taille_palet) / distance
                print(pygame.mixer.music.get_volume())
                pygame.mixer.music.set_volume(1)
                frappe.play()
                print(pygame.mixer.music.get_volume())

                """
                L'angle Réel est le l'angle duquel le palet a été touché, autrement dit, il s'agit de l'endroit de la surface du
                palet surlequel touche le palet en degrés en sens direct sur un cercle trigonométrique.
                - Les angles Cos et Sin permettent de calculer l'angle Réel.
                - Distance X est la distance entre la souris et le palet en coordonnées X sur l'écran.
                - Distance Y est la distance entre la souris et le palet en coordonnées Y sur l'écran.
                - Distance est la distance réelle calculée à partir de distance X et distance Y entre la souris et le palet et
                est l'hypothénuse du triangle rectangle en Distance X et Distance Y.
                """
    # Pour chaque rafraichissement
    for event in pygame.event.get():
        # Vérifie l'évènement quit
        if event.type == pygame.QUIT:
            actualiser = False
    if score != "∞":
        if Cage1.score >= score:
            resultat = "defaite"
            actualiser = False
        elif Cage2.score >= score:
            resultat = "victoire"
            actualiser = False
    # Mise à jour de l'interface
    pygame.display.update()

    # Sauvegarde des déplacements
    Plot1.set_ancienne_position()
    Plot2.set_ancienne_position()
    Palet1.set_ancienne_position()

if difficulte == 1 * ratio ** 2:
    ost2.stop()
else:
    ost.stop()
Affichage_resultat = None
if resultat == "victoire":
    Affichage_resultat = pygame.font.Font("Polices/NotoSans-Black.ttf", int(40 * ratio)).render("Vous avez gagné", True, blanc)
    victoire.play()
    actualiser2 = True
elif resultat == "egalite":
    Affichage_resultat = pygame.font.Font("Polices/NotoSans-Black.ttf", int(40 * ratio)).render("égalité", True, blanc)
    actualiser2 = True
elif resultat == "defaite":
    Affichage_resultat = pygame.font.Font("Polices/NotoSans-Black.ttf", int(40 * ratio)).render("Vous avez perdu", True, blanc)
    defaite.play()
    actualiser2 = True
Affichage_rejouer = pygame.font.Font("Polices/NotoSans-Black.ttf", int(40 * ratio)).render("Rejouer", True, blanc)
Affichage_retour = pygame.font.Font("Polices/NotoSans-Black.ttf", int(40 * ratio)).render("Retourner au menu", True, blanc)

while actualiser2:
    pygame.draw.rect(interface, grisfonce, (0, 0, Ix, int(Iy)))
    interface.blit(Affichage_resultat, ((Ix / 2) - (Affichage_resultat.get_rect().width / 2), 85 * ratio))
    pygame.draw.rect(interface, orange, ((Ix / 2) - (Affichage_rejouer.get_rect().width / 2), 200 * ratio, Affichage_rejouer.get_rect().width, Affichage_rejouer.get_rect().height), 0, int(7 * ratio))
    interface.blit(Affichage_rejouer, ((Ix / 2) - (Affichage_rejouer.get_rect().width / 2), 200 * ratio))
    pygame.draw.rect(interface, orange, ((Ix / 2) - (Affichage_retour.get_rect().width / 2), 315 * ratio, Affichage_retour.get_rect().width, Affichage_rejouer.get_rect().height), 0, int(7 * ratio))
    interface.blit(Affichage_retour, ((Ix / 2) - (Affichage_retour.get_rect().width / 2), 315 * ratio))


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # Vérifie si une touche est pressée
            pos = pygame.mouse.get_pos()
            if (Ix / 2) - (Affichage_rejouer.get_rect().width / 2) <= pos[0] <= (Ix / 2) + (Affichage_rejouer.get_rect().width / 2) and 200 * ratio <= pos[1] <= 200 * ratio + Affichage_rejouer.get_rect().height:
                rejouer = True
                actualiser2 = False
            elif (Ix / 2) - (Affichage_retour.get_rect().width / 2) <= pos[0] <= (Ix / 2) + (Affichage_retour.get_rect().width / 2) and 315 * ratio <= pos[1] <= 315 * ratio + Affichage_retour.get_rect().height:
                actualiser2 = False
        # Vérifie l'évènement quit
        if event.type == pygame.QUIT:
            actualiser2 = False
    # Mise à jour de l'interface
    pygame.display.update()
fin_temps.stop()