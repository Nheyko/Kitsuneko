import pytmx
import pyscroll

class Map:

    def __init__(self, window):

        # Chargement de la carte
        self.tmx_data = pytmx.util_pygame.load_pygame('Assets/Maps/Starting Village.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, window.get_screen().get_size())
        self.map = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=3)
        self.debug_layer = False
        self.map_objects = []
        # self.map_layer.zoom = 2

    def add_sprites(self, sprites):
        for sprite in sprites:
            self.map.add(sprite.get_sprite())

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
        object_layer = self.tmx_data.get_layer_by_name('objects')
        for obj in object_layer:
            self.map_objects.append(obj)

    def get_map_objects(self):
        return self.map_objects