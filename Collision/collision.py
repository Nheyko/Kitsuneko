import pygame

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []

    def add_all_collider_objects(self, objects):

        for obj in objects:
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:
                    self.collider_objects.append(obj)
    
    def create_collider(x, y, width, height):
        rect = pygame.Rect(x, y, width, height)
        return rect

    def detect_collision(self, character_objects, collider_objects):
        for character in character_objects:
            if character.get_sprite().get_collider().collideobjects(collider_objects) > -1:
                return True
        pass
            
    def draw_colliders_on_surface(self, map_surface, collider_objects):

        for collider in collider_objects:
            points = [(point.x, point.y) for point in collider.points]
            pygame.draw.polygon(map_surface, 'red', points)
    
    def get(self):
        return self.collider_objects