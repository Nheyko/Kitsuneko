import pygame

from Sprite.direction import Direction

class Keyboard:

    def __init__(self) -> None:

        self.is_direction_pressed = False
        self.is_letter_pressed = False

    def direction_of(self, key_pressed):
            
            if key_pressed == 'none':
                return Direction.NONE
            if key_pressed == 'up':
                return Direction.UP
            if key_pressed == 'down':
                return Direction.DOWN
            if key_pressed == 'left':
                return Direction.LEFT
            if key_pressed == 'right':
                return Direction.RIGHT
            if key_pressed == 'up_left':
                return Direction.UP_LEFT
            if key_pressed == 'up_right':
                return Direction.UP_RIGHT
            if key_pressed == 'down_left':
                return Direction.DOWN_LEFT
            if key_pressed == 'down_right':
                return Direction.DOWN_RIGHT

    def key_pressed(self):

        pressed = pygame.key.get_pressed()
            
        if pressed[pygame.K_UP]:
            if pressed[pygame.K_LEFT]:
                return 'up_left'
            elif pressed[pygame.K_RIGHT]:
                return 'up_right'
            elif pressed[pygame.K_DOWN]:
                return 'none'
            return 'up'
        
        elif pressed[pygame.K_DOWN]:
            if pressed[pygame.K_LEFT]:
                return 'down_left'
            elif pressed[pygame.K_RIGHT]:
                return 'down_right'
            return 'down'

        elif pressed[pygame.K_LEFT]:
            if pressed[pygame.K_RIGHT]:
                return 'none'
            return 'left'

        elif pressed[pygame.K_RIGHT]:
            return 'right'
        
    def is_direction_key_pressed(self):

        pressed = pygame.key.get_pressed() 

        if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
            self.set_is_direction_key_pressed(True)
        else:
            self.set_is_direction_key_pressed(False)
        return self.is_direction_pressed
    
    def set_is_direction_key_pressed(self, bool):
        self.is_direction_pressed = bool

    def is_letter_key_pressed(self):

        pressed = pygame.key.get_pressed() 

        if pressed[pygame.K_d]:
            self.set_is_letter_key_pressed(True)
            return self.is_letter_pressed
        else:
            self.set_is_letter_key_pressed(False)
            return self.is_letter_pressed
            
    def set_is_letter_key_pressed(self, bool):
        self.is_letter_pressed = bool