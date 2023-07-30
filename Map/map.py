import pytmx
import pyscroll

class Map:

    def __init__(self, window):

        # Chargement de la carte
        self.tmx_data = pytmx.util_pygame.load_pygame('Assets/Maps/Starting village.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, window.get_screen().get_size())
        self.map = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=3)
        self.debug_layer = False
        self.map_objects = []
        self.map_layer.zoom = 1

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
    
    def width(self):
        return self.tmx_data.width * self.tmx_data.tilewidth
    
    def height(self):
        return self.tmx_data.height * self.tmx_data.tileheight
    
    def get_tmx_data(self):
        return self.tmx_data
    
    def search_all_objects(self):
        obstacle_layer = self.tmx_data.get_layer_by_name('obstacle')
        for obstacle in obstacle_layer:
            self.map_objects.append(obstacle)

        player_layer = self.tmx_data.get_layer_by_name('player')
        for player in player_layer:
            self.map_objects.append(player)

        tp_layer = self.tmx_data.get_layer_by_name('tp')
        for tp in tp_layer:
            self.map_objects.append(tp)

    def get_map_objects(self):
        return self.map_objects
    
    def get_map_layer_zoom(self):
        return self.map_layer.zoom
    
    def set_map_layer_zoom(self, screen):

        if screen.get_screen_width() == 800 and screen.get_screen_height() == 600:
            self.map_layer.zoom = 1.2
        elif screen.get_screen_width() == 1024 and screen.get_screen_height() == 768:
            self.map_layer.zoom = 1.5
        if screen.get_screen_width() == 1600 and screen.get_screen_height() == 900:
            self.map_layer.zoom = 1.8
            