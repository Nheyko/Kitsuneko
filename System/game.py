import pygame

from Collision.collision import Collision
from Controls.keyboard import Keyboard
from Sprite.rectangle import Rectangle
from Screen.window import Window
from Sprite.polygon import Polygon
from Sound.music import Music
from Sprite.sprite import Sprite
from Map.map import Map
from Entity.character import Character

fps = 60

class Game:

    def __init__(self):

        # Initialisation de la fenêtre principale
        self.window = Window()

        # Initialisation du moteur de musique
        self.music = Music()

        # Création d'un personnage
        self.character = Character()

        # Création d'un groupe de sprite
        self.character_group = pygame.sprite.Group()

        # Ajout du sprite de mon personnage dans le groupe
        self.character_group.add(self.character.get_sprite())
        self.character_group.add(self.character.get_collider_sprite())

        # Création de la carte
        url = 'Assets/Maps/starting_village.tmx'
        self.map = Map(self.window, url, 4)
        self.map.set_map_layer_zoom(self.window)

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
        self.map_surface = pygame.Surface((self.map.get_width(), self.map.get_height()), pygame.SRCALPHA)
        self.map_surface.set_alpha(100)

        # Création d'un nouvel objet Sprite
        self.map_surface_sprite = Sprite()

        self.colliders = []

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
                

        # Converti la surface en Sprite pour pouvoir afficher les colliders
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
        self.character.get_collider_sprite().set_position(character_position.x + ((self.character.get_sprite().get_sprite_width() - self.character.get_sprite().get_sprite_width() * 0.5) / 2), character_position.y + (self.character.get_sprite().get_sprite_height() / 2))

        # Synchronise la position du rect avec la position du joueur pour éviter d'éventuel bugs
        self.character.get_sprite().update_position()
        self.character.get_collider_sprite().update_position()

    # Debug function
    def show_coordinate(self):

        print("CharaX = ", self.character.get_sprite().get_position().x)
        print("CharaY = ", self.character.get_sprite().get_position().y)

        print("CharaColyX = ", self.character.get_collider_sprite().get_position().x)
        print("CharaColyY = ", self.character.get_collider_sprite().get_position().y)
    
    # Debug function
    def debug(self):

        if self.antispam == True and pygame.time.get_ticks() - self.starttime >= 500:
            self.antispam = False

        if self.keyboard_input.is_letter_key_pressed():
            if(self.map.is_debug_layer_activated() == False and self.antispam == False):
                self.starttime = pygame.time.get_ticks()
                self.map.add_sprite(self.map_surface_sprite)
                self.show_coordinate()
                self.character.get_collider_sprite().set_collider_surface_alpha(100)
                self.antispam = True
            
            elif self.map.is_debug_layer_activated() == True and self.antispam == False:
                self.map.remove_sprite(self.map_surface_sprite)
                self.starttime = pygame.time.get_ticks()
                self.show_coordinate()
                self.character.get_collider_sprite().set_collider_surface_alpha(0)
                self.antispam = True
    
    def update(self):

         # Met à jour la position du joueur quand il se déplace
        self.character.get_sprite().update_position()
        self.character.get_collider_sprite().update_position()

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

            self.debug()
            self.collision.motor(self.keyboard_input, self.character, self.colliders, self.map)
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(fps)

        pygame.quit()