import pygame
from core.utils import grid_to_iso
import settings

class Tile:
    def __init__(self, x, y, image):
        self.grid_x = x
        self.grid_y = y
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, surface, offset_x, offset_y):
        iso_x, iso_y = grid_to_iso(self.grid_x, self.grid_y,
                                   settings.TILE_WIDTH, settings.TILE_HEIGHT)
        self.rect.topleft = (iso_x + offset_x, iso_y + offset_y)
        surface.blit(self.image, self.rect)