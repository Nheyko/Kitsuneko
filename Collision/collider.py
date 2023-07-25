import pygame

class Collider:

    def __init__(self) -> None:
        self.mask = None
        self.image = None

    def set_collider(self, surface):
        self.mask = pygame.mask.from_surface(surface)

    def get_collider(self):
        return self.mask
    
    def set_image(self):
        self.image = self.mask.to_surface()

    def get_image(self):
        return self.image