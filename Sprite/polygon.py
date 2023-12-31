import pygame

from Sprite.sprite import Sprite

class Polygon():

    def __init__(self, polygon_object):
        self.sprite = Sprite()
        self.points = []

        surface = pygame.Surface((polygon_object.width, polygon_object.height), pygame.SRCALPHA)
        self.set_points([(point.x - polygon_object.x, point.y - polygon_object.y) for point in polygon_object.points])
        pygame.draw.polygon(surface, 'black', self.points)
        self.sprite.set_image(surface)
        self.sprite.set_position(polygon_object.x, polygon_object.y)
        self.sprite.set_name(polygon_object.name)
        self.sprite.set_type(polygon_object.type)
        self.sprite.set_collider(surface)
        if 'do_corners_slip' in polygon_object.properties.keys():
                if polygon_object.properties['do_corners_slip'] == True:
                    self.sprite.set_do_corners_slip(True)
                else:
                     self.sprite.set_do_corners_slip(False)

    def get_sprite(self):
        return self.sprite

    def get_points(self):
        return self.points
    
    def set_points(self, points):
        self.points = points