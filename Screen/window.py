import pygame

class Window :

    def __init__(self, width, height):
        # Création de la fenêtre du jeu
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Kitsuneko")

        # Définir le logo du jeu
        # pygame.display.set_icon(self.player.get())

    def get_screen(self) :
        return self.screen
