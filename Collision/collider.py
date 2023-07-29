import pygame

class Collider:

    def __init__(self) -> None:
        self.mask = None

    def set_mask(self, surface):
        self.mask = pygame.mask.from_surface(surface)

    def get_mask(self):
        return self.mask