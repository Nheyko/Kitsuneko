import pygame

class Window :

    def __init__(self):
        # Création de la fenêtre du jeu

        self.screen_width = 800
        self.screen_height = 600

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Kitsuneko")

        # Définir le logo du jeu
        # pygame.display.set_icon(self.player.get())

    def get_screen(self) :
        return self.screen

    def get_screen_width(self):
        return self.screen_width
    
    def get_screen_height(self):
        return self.screen_height
    
    def set_screen_width(self, width):
        self.screen_width = width
    
    def set_screen_width(self, height):
        self.screen_height = height
