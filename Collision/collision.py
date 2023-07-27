import pygame

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []

    def add_collider_objects(self, objects):
        for obj in objects:
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:
                    self.collider_objects.append(obj)

    def detect_collision(self, character, collider_sprite_group):

        # Permet de checker d'abord si on rentre dans un rect pour eviter de tout le temps regarder tout les colliders
        if pygame.sprite.spritecollide(character.get_sprite(), collider_sprite_group, False):
            # Ensuite, check les 2 masks qui sont concerné
            if pygame.sprite.spritecollide(character.get_sprite(), collider_sprite_group, False, pygame.sprite.collide_mask):
                return True
            else:
                return False
        else:
            return False

    def draw_colliders_on_surface(self, map_surface):
        for collider in self.collider_objects:
            if collider.type == 'polygon':
                points = [(point.x, point.y) for point in collider.points]
                pygame.draw.polygon(map_surface, 'red', points)
    
    def get_collider_objects(self):
        return self.collider_objects