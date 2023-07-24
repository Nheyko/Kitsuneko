import pygame

from System.collision import Collision
from Controls.input import Input
from Screen.window import Window
from System.polygon import Polygon
from World.map import Map
from Entity.character import Character

screen_width = 800
screen_height = 600
fps = 60

class Game:

    def __init__(self):

        # Initialisation des objets
        self.window = Window(screen_width,screen_height)

        self.character = Character()
        self.character_list = []
        self.character_list.append(self.character)

        self.map = Map(self.window)
        self.map_surface = pygame.Surface((self.map.width(), self.map.height()), pygame.SRCALPHA)
        self.map.add_sprites(self.character_list)

        self.polygons = Polygon(self.map_surface)
        
        self.collision = Collision()
        self.collider_objects = self.collision.get_all_collider_objects(self.map.get_tmx_data())
        self.collision.draw_colliders_on_surface(self.map_surface, self.collider_objects)
        self.map.add_sprites(self.character_list)

        self.input = Input()

        # Obtention de la position du joueur par les données du tmx enregistré dans la carte
        character_position = self.map.get_tmx_data().get_object_by_name("player")

        # Définit la position du joueur sur la carte
        self.character.get_sprite().set_position(character_position.x, character_position.y)

    def update(self):
         # Met à jour la position du joueur quand il se déplace
        self.character.get_sprite().update_position()

        # centre la carte sur la position du joueur
        self.map.get_map().center(self.character.get_sprite().get_rect().center)

        # met à jour la carte et la dessine
        self.map.get_map().draw(self.window.get_screen())

        pygame.display.flip()

    def run(self):

        clock = pygame.time.Clock()

        # Boucle du jeu
        running = True
        flag = False

        while running:

            # wait 2000 milliseconds before executing this 
            if flag == True and pygame.time.get_ticks() - starttime >= 500:
                flag = False

            # if self.input.direction_of(self.input.key_pressed()):
            if pygame.key.get_pressed():

                if self.input.is_direction_key_pressed():
                
                    # isCollision = self.collision.detect_collision(self.character_list, self.get_all_collision)
                    # if(isCollision != True):
                        self.character.get_sprite().save_location()
                        self.character.get_sprite().move(self.character.get_move_speed(), self.input.direction_of(self.input.key_pressed()))

                    # else:
                    #     self.character.get_sprite().move_back()
                if self.input.is_letter_key_pressed():
                        if(self.map.is_debug_layer_activated() == False and flag == False):
                            starttime = pygame.time.get_ticks()
                            self.map.add_surface(self.polygons)
                            flag = True
                        
                        elif self.map.is_debug_layer_activated() == True and flag == False:
                            self.map.remove_surface(self.polygons)
                            starttime = pygame.time.get_ticks()
                            flag = True



            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(fps)

        pygame.quit()