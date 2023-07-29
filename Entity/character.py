from Entity.entity import Entity
from Sprite.sprite import Sprite

class Character(Entity):

    def __init__(self):
        super().__init__()
        url = 'Assets/Sprites/Characters/player.png'
        self.sprite = Sprite()
        self.sprite.set_character_sprite(url)
        self.collider_sprite = Sprite()
        self.move_speed = 3

    def get_sprite(self):
        return self.sprite
    
    def set_sprite(self, new_sprite_url):
        self.sprite = new_sprite_url
    
    def get_move_speed(self):
        return self.move_speed
    
    def set_move_speed(self, speed):
        self.move_speed = speed

    def get_collider_sprite(self):
        return self.collider_sprite
    