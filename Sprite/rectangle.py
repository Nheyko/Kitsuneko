import pygame

from Sprite.sprite import Sprite

class Rectangle():

    def __init__(self, rectangle_object) -> None:
        self.sprite = Sprite()

        surface = pygame.Surface((rectangle_object.width, rectangle_object.height))
        self.sprite.set_rect(rectangle_object.x, rectangle_object.y, rectangle_object.width, rectangle_object.height)
        pygame.draw.rect(surface, 'black', self.sprite.get_rect())
        self.sprite.set_image(surface)
        self.sprite.set_position(rectangle_object.x, rectangle_object.y)
        self.sprite.set_name(rectangle_object.name)
        self.sprite.set_type(rectangle_object.type)
        self.sprite.set_collider(surface)
        if 'do_corners_slip' in rectangle_object.properties.keys():
                if rectangle_object.properties['do_corners_slip'] == True:
                    self.sprite.set_do_corners_slip(True)
                else:
                     self.sprite.set_do_corners_slip(False)

    def get_sprite(self):
        return self.sprite