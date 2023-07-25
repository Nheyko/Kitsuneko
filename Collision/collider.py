import pygame

class Collider:

    def __init__(self) -> None:
        self.mask = None
        self.image = None

    def set_mask(self, surface):
        self.mask = pygame.mask.from_surface(surface)

    def get_mask(self):
        return self.mask
    
    def set_image(self):
        self.image = self.mask.to_surface()

    def get_image(self):
        return self.image