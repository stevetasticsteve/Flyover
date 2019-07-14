import pygame
import math

class Camera:
    def __init__(self, player, window_size, map):
        self.camera_width = window_size[0]
        self.camera_height = window_size[1]
        self.player = player
        self.map = map
        self.Move()


    def Move(self):
        self.rect = (self.player.x - int(self.camera_width/2), self.player.y - int(self.camera_height/2),
                     self.player.x + int(self.camera_width/2), self.player.y + int(self.camera_height/2))

    def Active_tiles(self):
        # returns a list of tile tuples(x,y,img) that are currently around the player
        # and within the range of the camera
        active_tiles = []
        for tile in self.map.tile_map:
            if tile[0][0] in range(self.rect[0], self.rect[2]):
                if tile[0][1]in range(self.rect[1], self.rect[3]):
                    active_tiles.append(tile)
        return active_tiles


class Jet:
    def __init__(self, starting_coordinates):
        self.x = starting_coordinates[0]
        self.y = starting_coordinates[1]
        self.angle = starting_coordinates[2]
        # angle defined as 0 degrees North, 90 deg East etc.
    speed = 10
    acceleration = 2
    rotation_speed = 10
    maximum_speed = 20
    minimum_speed = 2


class Player(Jet):
    def __init__(self, starting_coordinates):
        Jet.__init__(self, starting_coordinates)
        self.sprite = pygame.image.load('Assets/Sprites/Plane.png')

    def move(self):
        self.y -= int(self.speed * math.cos(math.radians(self.angle)))
        self.x += int(self.speed * math.sin(math.radians(self.angle)))

    def rotate(self, direction):
        self.angle += direction * self.rotation_speed

    def accelerate(self, direction):
        self.speed += direction * self.acceleration