import pygame

from Sprite.direction import Direction

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []

    def add_collider_objects(self, objects):
        for obj in objects:
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:
                    self.collider_objects.append(obj)
        print(self.collider_objects)
    
    # def check_collision(self, character, colliders, direction, map):
    def check_collision(self, character, colliders, direction, check_pixels = 0):

        if check_pixels == 0:
            check_pixels = character.get_move_speed()

        for collider in colliders:
            if direction == Direction.UP:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), (character.get_collider_sprite().get_position().x - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels) - collider.get_sprite().get_position().y)):
                    return True
            if direction == Direction.UP_LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels) - collider.get_sprite().get_position().y)):
                    return True
            if direction == Direction.UP_RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels) - collider.get_sprite().get_position().y)):
                    return True
            if direction == Direction.DOWN:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), (character.get_collider_sprite().get_position().x - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels) - collider.get_sprite().get_position().y)):
                    return True
            if direction == Direction.DOWN_LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels) - collider.get_sprite().get_position().y)):
                    return True
            if direction == Direction.DOWN_RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels) - collider.get_sprite().get_position().y)):
                    return True
            if direction == Direction.LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - collider.get_sprite().get_position().y))):
                    return True
            if direction == Direction.RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - collider.get_sprite().get_position().y))):
                    return True
        return False

    def draw_colliders_on_surface(self, map_surface):
        for collider in self.collider_objects:
            if collider.type == 'polygon':
                points = [(point.x, point.y) for point in collider.points]
                pygame.draw.polygon(map_surface, 'red', points)
    
    def get_collider_objects(self):
        return self.collider_objects