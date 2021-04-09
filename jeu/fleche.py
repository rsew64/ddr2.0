import random

import pygame
from pygame.math import Vector2, Vector3


class Fleches:
    def __init__ (self):
        self.orientation = random.randint(1, 1)
        self.nom = ""
        self.taille = Vector2(100, 75)
        self.position = Vector2(1, 100)
        self.couleur = Vector3(random.randint (1,255), random.randint (1,255), random.randint (1,255))
        self.pt1 = Vector2()
        self.pt2 = Vector2()
        self.pt3 = Vector2()
        self.pt4 = Vector2()
        self.pt5 = Vector2()
        self.pt6 = Vector2()
        self.pt7 = Vector2()

    def afficher(self,core):
            if self.orientation == 1 :
                self.nom="haut"

            if self.orientation == 2 :
                self.nom="bas"

            if self.orientation == 3 :
                self.nom="droite"

            if self.orientation == 4 :
                self.nom="gauche"

            if self.nom == "haut" :
                self.position.x = 50
                self.pt1 = self.position
                self.pt2 = Vector2(self.pt1.x + 1/3 * self.taille.y, self.pt1.y)
                self.pt3 = Vector2(self.pt2.x, self.pt2.y - 2 / 3 * self.taille.x)
                self.pt4 = Vector2(self.pt3.x + 1/3 * self.taille.y, self.pt3.y)
                self.pt5 = Vector2(self.pt4.x - 1/2 * self.taille.y, self.pt1.y - self.taille.x)
                self.pt6 = Vector2(self.pt4.x - self.taille.y, self.pt4.y)
                self.pt7 = Vector2(self.pt6.x + 1/3 * self.taille.y, self.pt6.y)

            if self.nom == "bas" :
                self.position.x = 250
                self.pt1 = self.position
                self.pt2 = Vector2(self.pt1.x - 1 / 3 * self.taille.y, self.pt1.y)
                self.pt3 = Vector2(self.pt2.x, self.pt2.y + 2 / 3 * self.taille.x)
                self.pt4 = Vector2(self.pt3.x - 1 / 3 * self.taille.y, self.pt3.y)
                self.pt5 = Vector2(self.pt4.x + 1 / 2 * self.taille.y, self.pt1.y + self.taille.x)
                self.pt6 = Vector2(self.pt4.x + self.taille.y, self.pt4.y)
                self.pt7 = Vector2(self.pt6.x - 1 / 3 * self.taille.y, self.pt6.y)

            if self.nom == "droite" :
                self.position.x = 350
                self.pt1 = self.position
                self.pt2 = Vector2(self.pt1.x, self.pt1.y - 1 / 3 * self.taille.y)
                self.pt3 = Vector2(self.pt2.x + 2 / 3 * self.taille.x, self.pt2.y)
                self.pt4 = Vector2(self.pt3.x, self.pt3.y - 1 / 3 * self.taille.y)
                self.pt5 = Vector2(self.pt1.x + self.taille.x, self.pt4.y + 1 / 2 * self.taille.y)
                self.pt6 = Vector2(self.pt4.x, self.pt4.y + self.taille.y)
                self.pt7 = Vector2(self.pt6.x, self.pt6.y - 1 / 3 * self.taille.y)

            if self.nom == "gauche" :
                self.position.x = 550 + self.taille.x
                self.pt1 = self.position
                self.pt2 = Vector2(self.pt1.x, self.pt1.y + 1 / 3 * self.taille.y)
                self.pt3 = Vector2(self.pt2.x - 2 / 3 * self.taille.x, self.pt2.y)
                self.pt4 = Vector2(self.pt3.x, self.pt3.y + 1 / 3 * self.taille.y)
                self.pt5 = Vector2(self.pt1.x - self.taille.x, self.pt4.y - 1 / 2 * self.taille.y)
                self.pt6 = Vector2(self.pt4.x, self.pt4.y - self.taille.y)
                self.pt7 = Vector2(self.pt6.x, self.pt6.y + 1 / 3 * self.taille.y)

            pygame.draw.polygon(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)),((self.pt1), (self.pt2), (self.pt3), (self.pt4), (self.pt5), (self.pt6), (self.pt7)))


