import pygame

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []

    def add_collider_objects(self, objects):
        for obj in objects:
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:
                    self.collider_objects.append(obj)

    def detect_collision(self, character, collider, collider_objects):
        
        if character.get_sprite().get_collider().overlap(collider.get_mask(), (collider_objects[1].x - character.get_sprite().get_position().x, collider_objects[1].y - character.get_sprite().get_position().y)):
            print("detected")
        else:
            print("not detected")
            
    def draw_colliders_on_surface(self, map_surface, collider_objects):
        for collider in collider_objects:
            points = [(point.x, point.y) for point in collider.points]
            pygame.draw.polygon(map_surface, 'red', points)
    
    def get_collider_objects(self):
        return self.collider_objects