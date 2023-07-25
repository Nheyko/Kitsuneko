import pygame
from pygame.locals import *

from Sprite.animation import Animation
from Sprite.coordinate import Coordinate
from Sprite.direction import Direction
from collections import defaultdict

from PIL import Image

sprite_width = 32
sprite_height = 32

class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.animator = Animation()
        self.position = Coordinate()
        self.image = pygame.Surface((0,0))
        self.rect = self.image.get_rect()
        self.old_position = self.position.get_coordinate().copy()

    def set_character_sprite(self, url):

        self.sprite_sheet = self.slice_sprite_sheet(url)
        self.sprites = self.turn_image_into_sprites(self.sprite_sheet)

        self.image = self.sprites[0]
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()

        self.images = {
            Direction.DOWN: self.sprites[0],
            Direction.DOWN_LEFT: self.sprites[0],
            Direction.DOWN_RIGHT: self.sprites[0],
            Direction.LEFT: self.sprites[1],
            Direction.RIGHT: self.sprites[2],
            Direction.UP: self.sprites[3],
            Direction.UP_LEFT: self.sprites[3],
            Direction.UP_RIGHT: self.sprites[3],
        }

    def move(self, speed, Direction):

        match Direction:
            case Direction.UP:
                self.set_position(self.position.x, self.position.y - speed)
                self.change_direction(self.images, Direction.UP)
            case Direction.UP_LEFT:
                self.set_position(self.position.x - speed/2, self.position.y - speed)
                self.change_direction(self.images, Direction.UP)
            case Direction.UP_RIGHT:
                self.set_position(self.position.x + speed/2, self.position.y - speed)
                self.change_direction(self.images, Direction.UP)
            case Direction.DOWN:
                self.set_position(self.position.x, self.position.y + speed)
                self.change_direction(self.images, Direction.DOWN)
            case Direction.DOWN_LEFT:
                self.set_position(self.position.x - speed/2, self.position.y + speed)
                self.change_direction(self.images, Direction.DOWN)
            case Direction.DOWN_RIGHT:
                self.set_position(self.position.x + speed/2, self.position.y + speed)
                self.change_direction(self.images, Direction.DOWN)
            case Direction.LEFT:
                self.set_position(self.position.x - speed, self.position.y)
                self.change_direction(self.images, Direction.LEFT)
            case Direction.RIGHT:
                self.set_position(self.position.x + speed, self.position.y)
                self.change_direction(self.images, Direction.RIGHT)
            case _:
                pass

    def move_back(self):
        self.position.set_coordinate(self.old_position[0], self.old_position[1])
        self.rect.topleft = self.position.get_coordinate()
        self.collider.midbottom = self.rect.midbottom

    def is_void(self, img):

        by_color = defaultdict(int)
        for pixel in img.getdata():
            by_color[pixel] += 1
            if(pixel != (0,0,0,0)):
                return False
        return True
        
    def slice_sprite_sheet(self, url):
        sprite_sheet = []

        img = Image.open(url)

        width = img.width
        height = img.height
  
        # display width and height
        # print("The height of the image is: ", height)
        # print("The width of the image is: ", width)

        i = 1

        for x in range(0, width, sprite_width):
            sliced_columns = img.crop((x, 0, x + sprite_width, height))

            for y in range(0, height, sprite_height):
                sliced_sprites = sliced_columns.crop((0, y, sprite_width, y + sprite_height))

                if(self.is_void(sliced_sprites) == False):
                    # sliced_sprites.save('Assets/Sprites/Characters/img' + str(i) + '.png')
                    sprite_sheet.append(sliced_sprites)
                    i+=1

        img.close()
        return sprite_sheet

    def turn_image_into_sprites(self, sprite_sheet):
        sprites = []

        for sprite in sprite_sheet:
            mode = sprite.mode
            size = sprite.size
            data = sprite.tobytes()

            py_image = pygame.image.fromstring(data, size, mode)
            surface = pygame.Surface([sprite_width,sprite_height])

            surface.blit(py_image, (0,0))
            sprites.append(surface)

        return sprites

    def save_location(self):
        self.old_position = self.position.get_coordinate().copy()

    def set_position(self, x, y):
        self.position.set_coordinate(x, y)

    def update_position(self):
        self.rect.topleft = self.position.get_coordinate()
        # self.collider.midbottom = self.rect.midbottom
    
    def get_rect(self):
        return self.rect
    
    def change_direction(self, images, Direction):
        image = self.animator.change_direction(images, Direction)
        image.set_colorkey([0,0,0])
        self.set_image(image)

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

    def get_position(self):
        return self.position
    
    def convert_surface_to_sprite(self, surface):
        self.image = surface
        self.rect = self.image.get_rect()

    def get_collider(self):
        return self.collider