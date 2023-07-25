import pygame
from Collision.collider import Collider

from Collision.collision import Collision
from Controls.keyboard import Keyboard
from Screen.window import Window
from Map.polygon import Polygon
from Sprite.sprite import Sprite
from Map.map import Map
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
        self.map.add_sprites(self.character_list)
        self.map.search_all_objects()
        self.map_objects = self.map.get_map_objects()

        # Création d'une surface pour y intégrer les polygons
        self.map_surface = pygame.Surface((self.map.width(), self.map.height()), pygame.SRCALPHA)

        # Converti map_surface en sprite
        self.map_surface_sprite = Sprite()
        self.map_surface_sprite.convert_surface_to_sprite(self.map_surface)

        self.polygon = Polygon()
        self.polygon.add_polygons_in_objects(self.map_objects)
        self.polygons = self.polygon.get()

        self.polygon.transform_polygons_in_surface()
        self.polygon_surfaces = self.polygon.get_polygon_surfaces()

        self.collision = Collision()
        self.collision.add_collider_objects(self.polygons)
        self.colliders_objects = self.collision.get_collider_objects()
        self.collision.draw_colliders_on_surface(self.map_surface, self.colliders_objects)

        self.character_collider = Collider()
        self.character_collider.set_collider(self.character.get_sprite().get_image())
        # self.character_collider.set_image()
        self.polygon_collider = Collider()
        self.polygon_collider.set_collider(self.polygon_surfaces[0])
        # self.polygon_collider.set_image()

        # self.character_mask_image = self.character_collider.get_image()
        # self.polygon_mask_image = self.polygon_collider.get_image()

        self.keyboard_input = Keyboard()

        # Obtention de la position du joueur par les données du tmx enregistré dans la carte
        character_position = self.map.get_tmx_data().get_object_by_name("player")

        # Définit la position du joueur sur la carte
        self.character.get_sprite().set_position(character_position.x, character_position.y)

    def handler(self):
        if pygame.key.get_pressed():

            if self.keyboard_input.is_direction_key_pressed():
            
                # isCollision = self.collision.detect_collision(self.character_list, self.get_all_collision)
                # if(isCollision != True):
                    self.collision.detect_collision(self.character, self.pol)
                    self.character.get_sprite().save_location()
                    self.character.get_sprite().move(self.character.get_move_speed(), self.keyboard_input.direction_of(self.keyboard_input.key_pressed()))

                # else:
                #     self.character.get_sprite().move_back()

            if self.keyboard_input.is_letter_key_pressed():
                    if(self.map.is_debug_layer_activated() == False and self.antispam == False):
                        self.starttime = pygame.time.get_ticks()
                        self.map.add_sprite(self.map_surface_sprite)
                        self.antispam = True
                    
                    elif self.map.is_debug_layer_activated() == True and self.antispam == False:
                        self.map.remove_sprite(self.map_surface_sprite)
                        self.starttime = pygame.time.get_ticks()
                        self.antispam = True

    def update(self):
         # Met à jour la position du joueur quand il se déplace
        self.character.get_sprite().update_position()

        # centre la carte sur la position du joueur
        self.map.get_map().center(self.character.get_sprite().get_rect().center)

        # met à jour la carte et la dessine
        self.map.get_map().draw(self.window.get_screen())

        # self.window.get_screen().blit(self.polygon_mask_image, (0,0))
        # self.window.get_screen().blit(self.character_mask_image, (0,0))

        pygame.display.flip()

    def run(self):

        clock = pygame.time.Clock()
        self.antispam = False

        # Boucle du jeu
        running = True
        while running:

            # wait 2000 milliseconds before executing this 
            if self.antispam == True and pygame.time.get_ticks() - self.starttime >= 500:
                self.antispam = False

            self.handler()
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(fps)

        pygame.quit()