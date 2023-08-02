import pygame

from Sprite.sprite import Sprite

class Rectangle:

    def __init__(self) -> None:
        self.sprite = Sprite()

    def create_rectangle(self, rectangle_object):
        surface = pygame.Surface((rectangle_object.width, rectangle_object.height))
        self.sprite.set_rect(rectangle_object.x, rectangle_object.y, rectangle_object.width, rectangle_object.height)
        pygame.draw.rect(surface, 'black', self.sprite.get_rect())
        self.sprite.set_image(surface)
        self.sprite.set_position(rectangle_object.x, rectangle_object.y)
        self.sprite.set_name(rectangle_object.name)
        self.sprite.set_type(rectangle_object.type)
        self.sprite.set_collider(surface)

    def get_sprite(self):
        return self.sprite