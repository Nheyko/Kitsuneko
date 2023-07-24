import pygame

class Polygon(pygame.sprite.Sprite):

    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = surface
        self.rect = self.image.get_rect() # size and position
