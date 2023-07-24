from Sprite.sprite import Sprite

class Character:

    def __init__(self):
        url = 'Assets/Sprites/Characters/player.png'
        self.sprite = Sprite(url)
        self.move_speed = 2

    def get_sprite(self):
        return self.sprite
    
    def set_sprite(self, new_sprite_url):
        self.sprite = new_sprite_url
    
    def get_move_speed(self):
        return self.move_speed
    
    def set_move_speed(self, speed):
        self.move_speed = speed