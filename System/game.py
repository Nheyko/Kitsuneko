import pygame

from Collision.collision import Collision
from Controls.keyboard import Keyboard
from Screen.window import Window
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

        # Création de l'objet qui permet de gérer les entrées clavier
        self.keyboard_input = Keyboard()

        # Création d'un groupe de sprite
        self.character_group = pygame.sprite.Group()

        # Création du moteur de collision
        self.collision = Collision()

        # Ajout du sprite de mon personnage dans le groupe
        self.character_group.add(self.character.get_sprite())
        self.character_group.add(self.character.get_collider_sprite())

        # Création de la carte
        url = 'Assets/Maps/starting_village.tmx'
        self.map = Map(self.window, url, 4, self.character, self.character_group, self.collision)
        self.map.set_map_layer_zoom(self.window)

        # Debug
        # Création d'une nouvelle surface
        self.map_surface = pygame.Surface((self.map.get_width(), self.map.get_height()), pygame.SRCALPHA)
        self.map_surface.set_alpha(100)

        # Debug
        # Création d'un nouvel objet Sprite
        self.map_surface_sprite = Sprite()

        # Debug
        # Converti la surface en Sprite pour pouvoir afficher les colliders
        self.map_surface_sprite.convert_surface_to_sprite(self.map_surface)

        # Debug
        # Déssine tous les objets qui sont des colliders sur la surface self.map_surface
        # Permet de les afficher avec map.add_surface plus tard
        self.collision.draw_colliders_on_surface(self.map_surface)

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
            self.collision.motor(self.keyboard_input, self.character, self.character_group, self.map.get_tmx_data().tilewidth, self.map.get_tmx_data().tileheight, self.map, self.window)
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(fps)

        pygame.quit()