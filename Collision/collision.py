import pygame

from Sprite.direction import Direction

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []
        self.is_polygon = False

    def add_collider_objects(self, objects):
        for obj in objects:
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:
                    self.collider_objects.append(obj)

    def check_if_polygon(self, collider):
        if collider.get_sprite().get_type() == 'polygon':
            self.set_is_polygon(True)
        else:
            self.set_is_polygon(False)
    
    def set_is_polygon(self, bool):
        self.is_polygon = bool

    def get_is_polygon(self):
        return self.is_polygon

    def check_collision(self, character, colliders, direction, check_pixels_x = 0, check_pixels_y = 0):

        if check_pixels_x == 0:
            check_pixels_x = character.get_move_speed()

        if check_pixels_y == 0:
            check_pixels_y = character.get_move_speed()

        for collider in colliders:

            if direction == Direction.UP:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), (character.get_collider_sprite().get_position().x - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.UP_LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.UP_RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.DOWN:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), (character.get_collider_sprite().get_position().x - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.DOWN_LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.DOWN_RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - collider.get_sprite().get_position().y))):
                    self.check_if_polygon(collider)
                    return True
                
            if direction == Direction.RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - collider.get_sprite().get_position().y))):
                    self.check_if_polygon(collider)
                    return True
                
        return False

    def draw_colliders_on_surface(self, map_surface):
        for collider in self.collider_objects:
            if collider.type == 'polygon':
                points = [(point.x, point.y) for point in collider.points]
                pygame.draw.polygon(map_surface, 'red', points)
            elif collider.type == 'rectangle':
                rect = pygame.Rect(collider.x, collider.y, collider.width, collider.height)
                pygame.draw.rect(map_surface, 'red', rect)
    
    def get_collider_objects(self):
        return self.collider_objects