import pygame
import random
import Tile

class TileHandler(object):

    def __init__(self):
        self.tile_array_x = 150
        self.tile_array_y = 100

        self.tile_array = [[(y * 10) + x for x in xrange(self.tile_array_x)] for y in xrange(self.tile_array_y)]

        self.tile_size = 16

    def print_text_arrangement(self):
        for y in xrange(self.tile_array_y):
            for x in xrange(self.tile_array_x):
                print self.tile_array[y][x],

            print ""

    def fill_array_random(self):
        image_array = [pygame.image.load("res/"+["Red", "Green", "Blue", "Yellow", "Cyan"][x]+"Tile.png") for x in xrange(5)]
        for y in xrange(self.tile_array_y):
            for x in xrange(self.tile_array_x):
                self.tile_array[y][x] = Tile.Tile(x * self.tile_size, y * self.tile_size, random.choice(image_array))

    def render(self, surface):
        for y in xrange(self.tile_array_y):
            for x in xrange(self.tile_array_x):
                self.tile_array[y][x].render(surface)
