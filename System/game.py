import pygame

from Collision.collision import Collision
from Controls.keyboard import Keyboard
from Screen.window import Window
from Map.polygon import Polygon
from Sound.music import Music
from Sprite.direction import Direction
from Sprite.sprite import Sprite
from Map.map import Map
from Entity.character import Character

screen_width = 800
screen_height = 600
fps = 60

class Game:

    def __init__(self):

        # Initialisation de la fenêtre principale
        self.window = Window(screen_width,screen_height)

        # Initialisation du moteur de musique
        self.music = Music()

        # Création d'un personnage
        self.character = Character()

        # Création d'un groupe de sprite
        self.character_group = pygame.sprite.Group()

        # Ajout du sprite de mon personnage dans le groupe
        self.character_group.add(self.character.get_sprite())

        # Création de la carte
        self.map = Map(self.window)

        # Ajout des Sprites des personnages sur la carte
        self.map.add_sprites(self.character_group)

        # Cherche tout les objets du layer object dans Tmx_data et les enregistre dans un tableau
        self.map.search_all_objects()

        # On récupère le tableau
        self.map_objects = self.map.get_map_objects()

        # Création du moteur de collision
        self.collision = Collision()

        # On ajoute dans le tableau de l'objet tout les objects qui ont la propriété "collision"
        self.collision.add_collider_objects(self.map_objects)

        # On récupère le tableau de collider
        self.collider_objects = self.collision.get_collider_objects()

        # Création d'une nouvelle surface
        self.map_surface = pygame.Surface((self.map.width(), self.map.height()), pygame.SRCALPHA)

        # Création d'un nouvel objet Sprite
        self.map_surface_sprite = Sprite()

        self.polygons = []

        # Ajout de tous mes objets qui possede des collisions et un sprite dans mon groupe d'objet
        for collider_object in self.collider_objects:
            if collider_object.type == 'polygon':
                polygon = Polygon()
                polygon.create_polygon(collider_object)
                self.polygons.append(polygon)

        # Converti la surface en Sprite pour pouvoir afficher les polygones
        self.map_surface_sprite.convert_surface_to_sprite(self.map_surface)

        # Déssine tous les objets qui sont des colliders sur la surface self.map_surface
        # Permet de les afficher avec map.add_surface plus tard
        self.collision.draw_colliders_on_surface(self.map_surface)

        # Création de l'objet qui permet de gérer les entrées clavier
        self.keyboard_input = Keyboard()

        # Obtention de la position du joueur par les données du tmx enregistré dans la carte
        character_position = self.map.get_tmx_data().get_object_by_name("player")

        # Définit la position du joueur sur la carte | Position rect.topleft
        self.character.get_sprite().set_position(character_position.x, character_position.y)
        
        # Synchronise la position du rect avec la position du joueur pour éviter d'éventuel bugs
        self.character.get_sprite().update_position()

    def collision_motor(self):

        # wait 2000 milliseconds before executing this 
        if self.antispam == True and pygame.time.get_ticks() - self.starttime >= 500:
            self.antispam = False

        if pygame.key.get_pressed():
            if self.keyboard_input.is_direction_key_pressed():
                isCollision = self.collision.check_collision(self.character, self.polygons, self.keyboard_input.direction_of(self.keyboard_input.key_pressed()))
                
                if isCollision == False:
                    self.character.get_sprite().move(self.character.get_move_speed(), self.keyboard_input.direction_of(self.keyboard_input.key_pressed()), self.character.get_sprite().get_direction())
                
                elif isCollision == True and self.character.get_sprite().get_direction() == Direction.UP:

                    if self.collision.check_collision(self.character, self.polygons, Direction.LEFT) and self.keyboard_input.key_pressed() == 3:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.LEFT)

                    elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) and self.keyboard_input.key_pressed() == 4:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.RIGHT)

                    if self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_LEFT:
                        
                        if self.collision.check_collision(self.character, self.polygons, Direction.UP) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction(), False)

                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction(), False)

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_RIGHT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction(), False)
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction(), False)

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_LEFT):
                        
                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction())
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction())

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_RIGHT):
                        
                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction())
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction())

                elif isCollision == True and self.character.get_sprite().get_direction() == Direction.DOWN:

                    if self.collision.check_collision(self.character, self.polygons, Direction.LEFT) and self.keyboard_input.key_pressed() == 3:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.LEFT)

                    elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) and self.keyboard_input.key_pressed() == 4:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.RIGHT)

                    if self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_LEFT:

                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction(), False)
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction(), False)

                    elif self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_RIGHT:

                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction(), False)
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction(), False)
                        
                    elif self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_LEFT:

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction())
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction())
                        
                    elif self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_RIGHT:

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction())
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction())

                elif isCollision == True and self.character.get_sprite().get_direction() == Direction.LEFT:

                    if self.collision.check_collision(self.character, self.polygons, Direction.UP) and self.keyboard_input.key_pressed() == 1:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.UP)

                    elif self.collision.check_collision(self.character, self.polygons, Direction.DOWN) and self.keyboard_input.key_pressed() == 2:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.DOWN)

                    if self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_LEFT:

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction(), False)

                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction(), False)

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_LEFT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction(), False)
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction(), False)

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_RIGHT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction())
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction())

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_RIGHT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction())
                        
                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT) == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction())

                elif isCollision == True and self.character.get_sprite().get_direction() == Direction.RIGHT:

                    if self.collision.check_collision(self.character, self.polygons, Direction.UP) and self.keyboard_input.key_pressed() == 1:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.UP)

                    elif self.collision.check_collision(self.character, self.polygons, Direction.DOWN) and self.keyboard_input.key_pressed() == 2:
                        self.character.get_sprite().change_direction(self.character.get_sprite().get_images(), Direction.DOWN)

                    if self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_RIGHT:

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction(), False)

                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction(), False)

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_RIGHT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction(), False)

                        elif self.collision.check_collision(self.character, self.polygons, Direction.RIGHT)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.RIGHT, self.character.get_sprite().get_direction(), False)

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.UP_LEFT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.UP)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.UP, self.character.get_sprite().get_direction())

                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction())

                    elif(self.keyboard_input.direction_of(self.keyboard_input.key_pressed()) == Direction.DOWN_LEFT):

                        if self.collision.check_collision(self.character, self.polygons, Direction.DOWN)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.DOWN, self.character.get_sprite().get_direction())

                        elif self.collision.check_collision(self.character, self.polygons, Direction.LEFT)  == False:
                            self.character.get_sprite().move(self.character.get_move_speed(), Direction.LEFT, self.character.get_sprite().get_direction())

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

            self.collision_motor()
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(fps)

        pygame.quit()