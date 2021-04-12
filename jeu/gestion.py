import pygame

from pygame.math import Vector2

import core
from jeu.fleche import Fleches
from jeu.joueur import Joueur


class Gestion :
    def __init__ (self):
        self.score = 10
        self.appreciation = ""
        self.vitesse = 9.81
        self.mode = 2
        self.musique = ".mp3"
        self.rythme = 70.5
        self.page = 3
        self.nbjoueur = 1
        self.joueurs= Joueur()
        self.fleches= Fleches()
        self.pt1 = Vector2()
        self.pt2 = Vector2()
        self.pt3 = Vector2()
        self.pt4 = Vector2()
        self.pt5 = Vector2()
        self.pt6 = Vector2()
        self.pt7 = Vector2()
        self.pt8 = Vector2()
        self.pt9 = Vector2()
        self.pt10 = Vector2()
        self.pt11 = Vector2()
        self.pt12 = Vector2()
        self.pt13 = Vector2()
        self.pt14 = Vector2()
        self.pt15 = Vector2()
        self.pt16 = Vector2()
        self.pt17 = Vector2()
        self.pt18 = Vector2()
        self.pt19 = Vector2()
        self.pt20 = Vector2()
        self.pt21 = Vector2()
        self.pt22 = Vector2()
        self.pt23 = Vector2()
        self.pt24 = Vector2()
        self.pt25 = Vector2()
        self.pt26 = Vector2()
        self.pt27 = Vector2()
        self.pt28 = Vector2()

    def afficher (self, core):

            # haut
            self.pt1 = Vector2(50, core.WINDOW_SIZE[1]-10)
            self.pt2 = Vector2(self.pt1.x + 1/3 * self.fleches.taille.y, self.pt1.y)
            self.pt3 = Vector2(self.pt2.x, self.pt2.y - 2 / 3 * self.fleches.taille.x)
            self.pt4 = Vector2(self.pt3.x + 1/3 * self.fleches.taille.y, self.pt3.y)
            self.pt5 = Vector2(self.pt4.x - 1/2 * self.fleches.taille.y, self.pt1.y - self.fleches.taille.x)
            self.pt6 = Vector2(self.pt4.x - self.fleches.taille.y, self.pt4.y)
            self.pt7 = Vector2(self.pt6.x + 1/3 * self.fleches.taille.y, self.pt6.y)

            # bas
            self.pt8 = Vector2(self.pt1.x+200, core.WINDOW_SIZE[1]-self.fleches.taille.x-5)
            self.pt9 = Vector2(self.pt8.x - 1 / 3 * self.fleches.taille.y, self.pt8.y)
            self.pt10 = Vector2(self.pt9.x, self.pt9.y + 2 / 3 * self.fleches.taille.x)
            self.pt11 = Vector2(self.pt10.x - 1 / 3 * self.fleches.taille.y, self.pt10.y)
            self.pt12 = Vector2(self.pt11.x + 1 / 2 * self.fleches.taille.y, self.pt8.y + self.fleches.taille.x)
            self.pt13 = Vector2(self.pt11.x + self.fleches.taille.y, self.pt11.y)
            self.pt14 = Vector2(self.pt13.x - 1 / 3 * self.fleches.taille.y, self.pt13.y)

            # droite
            self.pt15 = Vector2(self.pt8.x+100, core.WINDOW_SIZE[1]-((self.fleches.taille.x)/2))
            self.pt16 = Vector2(self.pt15.x, self.pt15.y - 1 / 3 * self.fleches.taille.y)
            self.pt17 = Vector2(self.pt16.x + 2 / 3 * self.fleches.taille.x, self.pt16.y)
            self.pt18 = Vector2(self.pt17.x, self.pt17.y - 1 / 3 * self.fleches.taille.y)
            self.pt19 = Vector2(self.pt15.x + self.fleches.taille.x, self.pt18.y + 1 / 2 * self.fleches.taille.y)
            self.pt20 = Vector2(self.pt18.x, self.pt18.y + self.fleches.taille.y)
            self.pt21 = Vector2(self.pt20.x, self.pt20.y - 1 / 3 * self.fleches.taille.y)

            # gauche
            self.pt22 = Vector2(self.pt15.x + 200 + self.fleches.taille.x, core.WINDOW_SIZE[1]-((self.fleches.taille.x + 40)/2))
            self.pt23 = Vector2(self.pt22.x, self.pt22.y + 1 / 3 * self.fleches.taille.y)
            self.pt24 = Vector2(self.pt23.x - 2 / 3 * self.fleches.taille.x, self.pt23.y)
            self.pt25 = Vector2(self.pt24.x, self.pt24.y + 1 / 3 * self.fleches.taille.y)
            self.pt26 = Vector2(self.pt22.x - self.fleches.taille.x, self.pt25.y - 1 / 2 * self.fleches.taille.y)
            self.pt27 = Vector2(self.pt25.x, self.pt25.y - self.fleches.taille.y)
            self.pt28 = Vector2(self.pt27.x, self.pt27.y + 1 / 3 * self.fleches.taille.y)

            pygame.draw.rect(core.screen, (100, 100, 100), (1, core.WINDOW_SIZE[1]-(self.fleches.taille.x + 22), core.WINDOW_SIZE[0]-2,(self.fleches.taille.x + 20)))
            pygame.draw.polygon(core.screen, (0, 0, 0), (self.pt1, self.pt2, self.pt3, self.pt4, self.pt5, self.pt6, self.pt7))
            pygame.draw.polygon(core.screen, (0, 0, 0),(self.pt8, self.pt9, self.pt10, self.pt11, self.pt12, self.pt13, self.pt14))
            pygame.draw.polygon(core.screen, (0, 0, 0),(self.pt15, self.pt16, self.pt17, self.pt18, self.pt19, self.pt20, self.pt21))
            pygame.draw.polygon(core.screen, (0, 0, 0),(self.pt22, self.pt23, self.pt24, self.pt25, self.pt26, self.pt27, self.pt28))

    def naviguer (self):
        pass

    pass

