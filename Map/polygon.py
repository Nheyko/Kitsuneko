import pygame

class Polygon():

    def __init__(self):
        self.polygons = []
        self.polygon_surfaces = []
    
    def add_polygons_in_objects(self, objects):
        for collider_polygon in objects:
            if collider_polygon.type == 'polygon' :
                self.polygons.append(collider_polygon)

    def transform_polygons_in_surface(self):
        for polygon in self.polygons:
            surface = pygame.Surface((polygon.width, polygon.height), pygame.SRCALPHA)
            points = [(point.x, point.y) for point in polygon.points]
            pygame.draw.polygon(surface, 'red', points)
            self.polygon_surfaces.append(surface)

    def get(self):
        return self.polygons
    
    def get_polygon_surfaces(self):
        return self.polygon_surfaces