import pygame

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []

    def add_collider_objects(self, objects):
        for obj in objects:
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:
                    self.collider_objects.append(obj)

    def detect_collision(self, collider1, collider2):
        if collider1.get_collider().overlap(collider2.get_collider(), (collider1.x, collider1.y)):
            print("detected")
        else:
            print("not detected")
            
    def draw_colliders_on_surface(self, map_surface, collider_objects):

        for collider in collider_objects:
            points = [(point.x, point.y) for point in collider.points]
            pygame.draw.polygon(map_surface, 'red', points)
    
    def get_collider_objects(self):
        return self.collider_objects