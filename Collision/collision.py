import pygame

from Sprite.direction import Direction
from Sprite.rectangle import Rectangle
from Sprite.polygon import Polygon

class Collision:

    def __init__(self) -> None:
        self.collider_objects = []
        self.colliders = []
        self.is_polygon = None
        self.is_rectangle = None
        self.is_tp = None
        self.do_corners_slip = False
        self.url = ""

    def set_do_corners_slip(self, bool):
        self.do_corners_slip = bool

    def get_do_corners_slip(self):
        return self.do_corners_slip

    def check_do_corners_slip(self, collider):
        if collider.get_sprite().get_do_corners_slip() == True:
            self.set_do_corners_slip(True)
        else:
            self.set_do_corners_slip(False)

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

    def check_if_rectangle(self, collider):
        if collider.get_sprite().get_type() == 'rectangle':
            self.set_is_rectangle(True)
        else:
            self.set_is_rectangle(False)

    def check_if_tp(self, collider):
        if collider.get_sprite().get_type() == 'tp':
            self.set_is_tp(True)
            self.set_url(collider.get_sprite().get_name())
        else:
            self.set_is_tp(False)
    
    def set_url(self, map_name):
        self.url = "Assets/Maps/" + map_name + ".tmx"

    def get_url(self):
        return self.url

    def set_is_polygon(self, bool):
        self.is_polygon = bool

    def get_is_polygon(self):
        return self.is_polygon

    def set_is_rectangle(self, bool):
        self.is_rectangle = bool

    def get_is_rectangle(self):
        return self.is_rectangle

    def set_is_tp(self, bool):
        self.is_tp_rect = bool

    def get_is_tp(self):
        return self.is_tp_rect

    def check_collision(self, character, colliders, direction, check_pixels_x = 0, check_pixels_y = 0):

        if check_pixels_x == 0:
            check_pixels_x = character.get_move_speed()

        if check_pixels_y == 0:
            check_pixels_y = character.get_move_speed()

        for collider in colliders:

            if direction == Direction.UP:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), (character.get_collider_sprite().get_position().x - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.UP_LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.UP_RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.DOWN:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), (character.get_collider_sprite().get_position().x - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.DOWN_LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.DOWN_RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y + check_pixels_y) - collider.get_sprite().get_position().y)):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.LEFT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x - check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - collider.get_sprite().get_position().y))):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
            if direction == Direction.RIGHT:
                if collider.get_sprite().get_collider().overlap(character.get_collider_sprite().get_collider(), ((character.get_collider_sprite().get_position().x + check_pixels_x) - collider.get_sprite().get_position().x, (character.get_collider_sprite().get_position().y - collider.get_sprite().get_position().y))):
                    self.check_if_polygon(collider)
                    self.check_if_rectangle(collider)
                    self.check_if_tp(collider)
                    self.check_do_corners_slip(collider)
                    return True
                
        return False

    def draw_colliders_on_surface(self, map_surface):

        for collider in self.collider_objects:
            if collider.type == 'polygon':
                points = [(point.x, point.y) for point in collider.points]
                pygame.draw.polygon(map_surface, 'red', points)
            elif collider.type == 'rectangle':
                rect = pygame.Rect(collider.x, collider.y, collider.width, collider.height)
                pygame.draw.rect(map_surface, 'green', rect)
            elif collider.type == 'tp':
                rect = pygame.Rect(collider.x, collider.y, collider.width, collider.height)
                pygame.draw.rect(map_surface, 'blue', rect)
    
    def get_collider_objects(self):
        return self.collider_objects

    def load_colliders(self):

        # Ajout de tous mes objets qui possede des collisions et un sprite dans mon groupe d'objet
        for collider_object in self.collider_objects:

            if collider_object.type == 'polygon':
                polygon = Polygon(collider_object)
                self.colliders.append(polygon)
            elif collider_object.type == 'rectangle':
                rectangle = Rectangle(collider_object)
                self.colliders.append(rectangle)
            elif collider_object.type == 'tp':
                rectangle = Rectangle(collider_object)
                self.colliders.append(rectangle)

    def get_colliders(self):
        return self.colliders

    def clear_colliders(self):
        self.colliders = []

    def clear_collider_objects(self):
        self.collider_objects = []

    def motor(self, keyboard_input, character, character_group, tilewidth, tileheight, map, window):

        if pygame.key.get_pressed():
            if keyboard_input.is_direction_key_pressed():

                is_collision = self.check_collision(character, self.colliders, keyboard_input.direction_of(keyboard_input.key_pressed()))

                if is_collision == False:
                    character.get_sprite().move(character.get_move_speed(), keyboard_input.direction_of(keyboard_input.key_pressed()), character.get_sprite().get_direction())
                    character.get_collider_sprite().move_collider(character.get_move_speed(), keyboard_input.direction_of(keyboard_input.key_pressed()))

                elif is_collision == True:

                    if self.get_is_polygon() == True or self.get_is_rectangle() == True:

                        if character.get_sprite().get_direction() == Direction.UP:

                            # Change de direction si on est contre un mur et qu'on relache une touche
                            if self.check_collision(character, self.colliders, Direction.LEFT) and keyboard_input.key_pressed() == 'left':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.LEFT)

                            elif self.check_collision(character, self.colliders, Direction.RIGHT) and keyboard_input.key_pressed() == 'right':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.RIGHT)

                            # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # Coin Haut Droite
                            if self.check_collision(character, self.colliders, Direction.UP_RIGHT) == True\
                                and self.check_collision(character, self.colliders, Direction.UP_LEFT, tilewidth, tileheight) == False\
                                and self.get_do_corners_slip() == True:
                                
                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)
                            
                            # # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # # Coin Haut Gauche
                            if self.check_collision(character, self.colliders, Direction.UP_LEFT) == True\
                                and self.check_collision(character, self.colliders, Direction.UP_RIGHT, tilewidth, tileheight) == False\
                                    and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)
                            
                            # Permet de slide contre le mur tout en conservant sa direction
                            if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_LEFT:
                                
                                if self.check_collision(character, self.colliders, Direction.UP) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.LEFT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)
                                    
                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_RIGHT):

                                if self.check_collision(character, self.colliders, Direction.UP) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_LEFT):
                                
                                if self.check_collision(character, self.colliders, Direction.DOWN) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.LEFT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_RIGHT):
                                
                                if self.check_collision(character, self.colliders, Direction.DOWN) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                        elif character.get_sprite().get_direction() == Direction.DOWN:
                            
                            # Change de direction si on est contre un mur et qu'on relache une touche
                            if self.check_collision(character, self.colliders, Direction.LEFT) and keyboard_input.key_pressed() == 'left':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.LEFT)

                            elif self.check_collision(character, self.colliders, Direction.RIGHT) and keyboard_input.key_pressed() == 'right':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.RIGHT)

                            # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # Coin Bas Gauche
                            if self.check_collision(character, self.colliders, Direction.DOWN_RIGHT) == True\
                                and self.check_collision(character, self.colliders, Direction.DOWN_LEFT,\
                                tilewidth, tileheight) == False\
                                and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            # # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # # Coin Bas Droite
                            if self.check_collision(character, self.colliders, Direction.DOWN_LEFT) == True\
                                and self.check_collision(character, self.colliders, Direction.DOWN_RIGHT, tilewidth, tileheight) == False\
                                and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                            # Permet de slide contre le mur tout en conservant sa direction
                            if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_LEFT:

                                if self.check_collision(character, self.colliders, Direction.DOWN) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.LEFT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            elif keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_RIGHT:

                                if self.check_collision(character, self.colliders, Direction.DOWN) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                            elif keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_LEFT:

                                if self.check_collision(character, self.colliders, Direction.UP) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.LEFT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            elif keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_RIGHT:

                                if self.check_collision(character, self.colliders, Direction.UP) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                        elif character.get_sprite().get_direction() == Direction.LEFT:

                            if self.check_collision(character, self.colliders, Direction.UP) and keyboard_input.key_pressed() == 'up':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.UP)

                            elif self.check_collision(character, self.colliders, Direction.DOWN) == True and keyboard_input.key_pressed() == 'down':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.DOWN)

                            # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # Coin Bas Gauche
                            if self.check_collision(character, self.colliders, Direction.UP_LEFT) == True\
                            and self.check_collision(character, self.colliders, Direction.DOWN_LEFT, tilewidth, tileheight) == False\
                            and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.LEFT:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                            # # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # # Coin Haut Gauche
                            if self.check_collision(character, self.colliders, Direction.DOWN_LEFT) == True\
                            and self.check_collision(character, self.colliders, Direction.UP_LEFT, tilewidth, tileheight) == False\
                            and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.LEFT:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                            if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_LEFT:

                                if self.check_collision(character, self.colliders, Direction.UP) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.LEFT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_LEFT):

                                if self.check_collision(character, self.colliders, Direction.DOWN) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.LEFT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_RIGHT):

                                if self.check_collision(character, self.colliders, Direction.UP) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_RIGHT):

                                if self.check_collision(character, self.colliders, Direction.DOWN) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT) == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                        elif character.get_sprite().get_direction() == Direction.RIGHT:

                            if self.check_collision(character, self.colliders, Direction.UP) and keyboard_input.key_pressed() == 'up':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.UP)

                            elif self.check_collision(character, self.colliders, Direction.DOWN) and keyboard_input.key_pressed() == 'down':
                                character.get_sprite().change_direction(character.get_sprite().get_images(), Direction.DOWN)

                            # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # Coin Haut Droite
                            if self.check_collision(character, self.colliders, Direction.DOWN_RIGHT) == True\
                            and self.check_collision(character, self.colliders, Direction.UP_RIGHT, tilewidth, tileheight) == False\
                            and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.RIGHT:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                            # # Permet de contourner les coins pour pas se retrouver coincer dedans
                            # # Coin Bas Droite
                            if self.check_collision(character, self.colliders, Direction.UP_RIGHT) == True\
                            and self.check_collision(character, self.colliders, Direction.DOWN_RIGHT, tilewidth, tileheight) == False\
                            and self.get_do_corners_slip() == True:

                                if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.RIGHT:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                            if keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_RIGHT:

                                if self.check_collision(character, self.colliders, Direction.UP)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_RIGHT):

                                if self.check_collision(character, self.colliders, Direction.DOWN)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.RIGHT)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.RIGHT, character.get_sprite().get_direction(), False)
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.RIGHT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.UP_LEFT):

                                if self.check_collision(character, self.colliders, Direction.UP)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.UP, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.UP)

                                elif self.check_collision(character, self.colliders, Direction.LEFT)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                            elif(keyboard_input.direction_of(keyboard_input.key_pressed()) == Direction.DOWN_LEFT):

                                if self.check_collision(character, self.colliders, Direction.DOWN)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.DOWN, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(),  Direction.DOWN)

                                elif self.check_collision(character, self.colliders, Direction.LEFT)  == False:
                                    character.get_sprite().move(character.get_move_speed(), Direction.LEFT, character.get_sprite().get_direction())
                                    character.get_collider_sprite().move_collider(character.get_move_speed(), Direction.LEFT)

                    if self.get_is_tp() == True:
                        map.load_map(window, self.get_url(), character, character_group, self)
