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

        # Création d'un personnage
        self.character = Character()

        # Ajout du collider au personnage
        self.character.get_sprite().set_collider(self.character.get_sprite().get_image())

        # Ajout du personnage dans une liste
        self.character_list = []
        self.character_list.append(self.character)

        # Création de la carte
        self.map = Map(self.window)

        # Ajout des Sprites des personnages sur la carte
        self.map.add_sprites(self.character_list)

        # Cherche tout les objets du layer object dans Tmx_data et les enregistre dans un tableau
        self.map.search_all_objects()

        # On récupère le tableau
        self.map_objects = self.map.get_map_objects()

        # Création d'une nouvelle surface
        self.map_surface = pygame.Surface((self.map.width(), self.map.height()), pygame.SRCALPHA)

        # Création d'un nouvel objet Sprite
        self.map_surface_sprite = Sprite()

        # Création d'un objet Polygon
        self.polygon = Polygon()

        # On ajoute la liste des polygons qui étaient dans objects dans un tableau de l'objet
        self.polygon.add_polygons_in_objects(self.map_objects)

        # On récupère le tableau de polygone dans une variable
        self.polygons = self.polygon.get_polygons()

        # Création du moteur de collision
        self.collision = Collision()

        # On ajoute dans le tableau de l'objet tout les polygones qui étaient des colliders
        self.collision.add_collider_objects(self.polygons)

        # On récupère le tableau de collider
        self.colliders_objects = self.collision.get_collider_objects()

        # Converti la surface en Sprite pour pouvoir afficher les polygones
        self.map_surface_sprite.convert_surface_to_sprite(self.map_surface)

        # Déssine tous les objets qui sont des colliders sur la surface self.map_surface
        # Permet de les afficher avec map.add_surface plus tard
        self.collision.draw_colliders_on_surface(self.map_surface, self.colliders_objects)

        # Crée une surface pour chaque polygon dans le tableau Polygon de l'objet
        self.polygon.transform_polygons_in_surface()

        # On récupère toutes les surfaces des polygones
        self.polygon_surfaces = self.polygon.get_polygon_surfaces()

        # Remplacer ces lignes
        self.polygon_collider = Collider()
        self.polygon_collider.set_mask(self.polygon_surfaces[1])

        # Création de l'objet qui permet de gérer les entrées clavier
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
                    self.collision.detect_collision(self.character, self.polygon_collider, self.colliders_objects)
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

        # met à jour la carte
        self.map.get_map().draw(self.window.get_screen())

        # Met à jour l'écran
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