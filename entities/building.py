import pygame

class Building:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)