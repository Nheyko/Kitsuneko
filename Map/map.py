import pygame
import pytmx
import pyscroll

from Sprite.sprite import Sprite

class Map:

    def __init__(self, window, url, character, character_group, collision):

        self.map_objects = []
        self.debug_layer = False

        self.load_map(window, url, character, character_group, collision)

    def add_sprites(self, sprites):
        for sprite in sprites:
            self.map.add(sprite)

    def remove_sprites(self, sprites):
        for sprite in sprites:
            self.map.remove(sprite.get_sprite())

    def add_sprite(self, sprite):
        self.set_is_debug_layer_activated(True)
        self.map.add(sprite)

    def remove_sprite(self, sprite):
        self.set_is_debug_layer_activated(False)
        self.map.remove(sprite)

    def is_debug_layer_activated(self):
        return self.debug_layer

    def set_is_debug_layer_activated(self, bool):
        self.debug_layer = bool

    def get_map(self):
        return self.map
    
    def get_width(self):
        return self.tmx_data.width * self.tmx_data.tilewidth
    
    def get_height(self):
        return self.tmx_data.height * self.tmx_data.tileheight
    
    def get_tmx_data(self):
        return self.tmx_data
    
    def search_all_objects(self):
        for object in self.tmx_data.objects:
            self.map_objects.append(object)

    def get_map_objects(self):
        return self.map_objects
    
    def get_map_layer_zoom(self):
        return self.map_layer.zoom
    
    def set_map_layer_zoom(self, screen):

        if screen.get_screen_width() == 800 and screen.get_screen_height() == 600:
            self.map_layer.zoom = 1.2
        elif screen.get_screen_width() == 1024 and screen.get_screen_height() == 768:
            self.map_layer.zoom = 1.5
        elif screen.get_screen_width() == 1600 and screen.get_screen_height() == 900:
            self.map_layer.zoom = 1.8

        if self.tmx_data.width == 25 and self.tmx_data.height == 25:
            self.map_layer.zoom = 1.5
    
    def clear_map_objects(self):
        self.map_objects = []

    def get_map_surface_sprite(self):
        return self.map_surface_sprite

    # Le dernier layer doit toujours être celui ou le personnage passe derriè visuellement
    def calculate_max_layer(self, tmx_data):

        # -1 Car ça commence à 0
        number_of_layer = -1

        for _ in tmx_data.visible_tile_layers:
            number_of_layer += 1

        return number_of_layer - 1

    def load_map(self, window, url, character, character_group, collision):

        # Chargement de la carte
        self.tmx_data = pytmx.load_pygame(url)
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, window.get_screen().get_size())
        max_layer = self.calculate_max_layer(self.tmx_data)
        self.map = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=max_layer)
        self.set_map_layer_zoom(window)

        self.map_surface = pygame.Surface((self.get_width(), self.get_height()), pygame.SRCALPHA)
        self.map_surface.set_alpha(100)

        self.map_surface_sprite = Sprite()
        self.map_surface_sprite.convert_surface_to_sprite(self.map_surface)

        # Ajout des Sprites des personnages sur la carte
        self.add_sprites(character_group)

        self.clear_map_objects()
        self.search_all_objects()

        # On ajoute dans le tableau de l'objet tout les objects qui ont la propriété "collision"
        collision.clear_collider_objects()
        collision.add_collider_objects(self.get_map_objects())

        collision.clear_colliders()
        collision.load_colliders()

        collision.draw_colliders_on_surface(self.map_surface)

        # Obtention de la position du joueur par les données du tmx enregistré dans la carte
        character_position = self.get_tmx_data().get_object_by_name("player")

        # Définit la position du joueur sur la carte | Position rect.topleft
        character.get_sprite().set_position(character_position.x, character_position.y)
        character.get_collider_sprite().set_position(character_position.x + ((character.get_sprite().get_sprite_width() - character.get_sprite().get_sprite_width() * 0.5) / 2), character_position.y + (character.get_sprite().get_sprite_height() / 2))

        # Synchronise la position du rect avec la position du joueur pour éviter d'éventuel bugs
        character.get_sprite().update_position()
        character.get_collider_sprite().update_position()
