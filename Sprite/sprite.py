import pygame
from pygame.locals import *
from Collision.collider import Collider

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

        self.name = ""
        self.type = ""

        self.animator = Animation()
        self.collider = Collider()
        self.position = Coordinate()

        self.direction = Direction.NONE

        self.image = pygame.Surface((0,0))
        self.rect = self.image.get_rect()

    def set_character_sprite(self, url):

        self.sprite_sheet = self.slice_sprite_sheet(url)
        self.sprites = self.turn_image_into_sprites(self.sprite_sheet)

        self.image = self.sprites[0]
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position.set_coordinate(0,0)
        self.collider.set_mask(self.image)

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

    def set_collider_sprite(self):
        surface = pygame.Surface((sprite_width * 0.5, sprite_width / 2))
        self.set_image(surface)
        surface.fill((255,255,255))
        surface.set_alpha(0)
        self.rect = self.image.get_rect()
        self.set_collider(surface)

    def move_collider(self, speed, Direction):

        match Direction:
            case Direction.UP:
                self.set_position(self.position.x, self.position.y - speed)

            case Direction.UP_LEFT:
                self.set_position(self.position.x - speed, self.position.y - speed)

            case Direction.UP_RIGHT:
                self.set_position(self.position.x + speed, self.position.y - speed)

            case Direction.DOWN:
                self.set_position(self.position.x, self.position.y + speed)

            case Direction.DOWN_LEFT:
                self.set_position(self.position.x - speed, self.position.y + speed)

            case Direction.DOWN_RIGHT:
                self.set_position(self.position.x + speed, self.position.y + speed)
                    
            case Direction.LEFT:
                self.set_position(self.position.x - speed, self.position.y)

            case Direction.RIGHT:
                self.set_position(self.position.x + speed, self.position.y)

            case _:
                pass

    def move(self, speed, Direction, previous_direction, change_direction = True):

        match Direction:
            case Direction.UP:
                self.set_position(self.position.x, self.position.y - speed)
                if change_direction:
                    self.change_direction(self.images, Direction.UP)

            case Direction.UP_LEFT:
                self.set_position(self.position.x - speed, self.position.y - speed)
                if previous_direction == Direction.LEFT:
                    self.change_direction(self.images, Direction.LEFT)
                else:
                    self.change_direction(self.images, Direction.UP)

            case Direction.UP_RIGHT:
                self.set_position(self.position.x + speed, self.position.y - speed)
                if previous_direction == Direction.RIGHT:
                    self.change_direction(self.images, Direction.RIGHT)
                else:
                    self.change_direction(self.images, Direction.UP)

            case Direction.DOWN:
                self.set_position(self.position.x, self.position.y + speed)
                if change_direction:
                    self.change_direction(self.images, Direction.DOWN)

            case Direction.DOWN_LEFT:
                self.set_position(self.position.x - speed, self.position.y + speed)
                if previous_direction == Direction.LEFT:
                    self.change_direction(self.images, Direction.LEFT)
                else:
                    self.change_direction(self.images, Direction.DOWN)

            case Direction.DOWN_RIGHT:
                self.set_position(self.position.x + speed, self.position.y + speed)
                if previous_direction == Direction.RIGHT:
                    self.change_direction(self.images, Direction.RIGHT)
                else:
                    self.change_direction(self.images, Direction.DOWN)
                    
            case Direction.LEFT:
                self.set_position(self.position.x - speed, self.position.y)
                if change_direction:
                    self.change_direction(self.images, Direction.LEFT)

            case Direction.RIGHT:
                self.set_position(self.position.x + speed, self.position.y)
                if change_direction:
                    self.change_direction(self.images, Direction.RIGHT)
            case _:
                pass

    def update_position(self):
        self.rect.topleft = self.position.get_coordinate()
    
    def change_direction(self, images, Direction):
        image = self.animator.change_direction(images, Direction)
        image.set_colorkey([0,0,0])
        self.rect.topleft = self.position.get_coordinate()
        self.set_image(image)
        self.set_direction(Direction)
        self.collider.set_mask(self.image)
    
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

    def set_position(self, x, y):
        self.position.set_coordinate(x, y)
    
    def get_rect(self):
        return self.rect
    
    def set_rect(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

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
        return self.collider.get_mask()
    
    def set_collider(self, surface):
        self.collider.set_mask(surface)

    def get_collider(self):
        return self.collider.get_mask()
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction

    def get_images(self):
        return self.images
    
    def get_sprite_width(self):
        return sprite_width
    
    def get_sprite_height(self):
        return sprite_height

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
    
