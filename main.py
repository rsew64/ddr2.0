

import pygame
import core
from jeu.fleche import Fleches
from jeu.gestion import Gestion
from jeu.musique import Musique

fleches = Fleches()
musique = Musique()
gestion = Gestion()
drops = []

pygame.font.init()
police = pygame.font.SysFont('Arial', 50)
text = 'You Lose'
texte = police.render(text, True, (255, 0, 0))

def setup():
    print("Setup START---------")
    core.fps = 50
    core.WINDOW_SIZE = [900, 1000]
    for i in range(0, 4):
        drops.append(fleches)
    print("Setup END-----------")

def run():
    gestion.afficher(core)
    show()
    update()



def update():
    vitesse = 1
    for fleches in drops:
        fleches.position.y += vitesse


    if fleches.nom == "haut" and fleches.position.y > gestion.pt1.y:
        core.screen.blit(texte, (50, 50))

    if fleches.nom == "bas" and fleches.position.y > gestion.pt8.y:
        core.screen.blit(texte, (50, 50))

    if fleches.nom == "droite" and fleches.position.y > gestion.pt15.y:
        core.screen.blit(texte, (50, 50))

    if fleches.nom == "gauche" and fleches.position.y > gestion.pt22.y:
        core.screen.blit(texte, (50, 50))

def show():
    for fleches in drops:
        fleches.afficher(core)

if __name__ == '__main__':
    core.main(setup, run)

if fleches.nom == "haut" and core.getkeyPressValue() == 1073741906:
    print("break")
    ok = False