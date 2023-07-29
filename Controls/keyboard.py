import pygame

from Sprite.direction import Direction

class Keyboard:

    def __init__(self) -> None:

        self.is_direction_pressed = False
        self.is_letter_pressed = False

    def direction_of(self, key_pressed):
            
            if key_pressed == 0:
                return Direction.NONE
            if key_pressed == 1:
                return Direction.UP
            if key_pressed == 2:
                return Direction.DOWN
            if key_pressed == 3:
                return Direction.LEFT
            if key_pressed == 4:
                return Direction.RIGHT
            if key_pressed == 5:
                return Direction.UP_LEFT
            if key_pressed == 6:
                return Direction.UP_RIGHT
            if key_pressed == 7:
                return Direction.DOWN_LEFT
            if key_pressed == 8:
                return Direction.DOWN_RIGHT

    def key_pressed(self):

        pressed = pygame.key.get_pressed()
            
        if pressed[pygame.K_UP]:
            if pressed[pygame.K_LEFT]:
                return 5
            elif pressed[pygame.K_RIGHT]:
                return 6
            elif pressed[pygame.K_DOWN]:
                return 0
            return 1
        
        elif pressed[pygame.K_DOWN]:
            if pressed[pygame.K_LEFT]:
                return 7
            elif pressed[pygame.K_RIGHT]:
                return 8
            return 2

        elif pressed[pygame.K_LEFT]:
            if pressed[pygame.K_RIGHT]:
                return 0
            return 3

        elif pressed[pygame.K_RIGHT]:
            return 4
        
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