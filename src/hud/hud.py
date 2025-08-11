import pygame

class HUD:
    def __init__(self, font):
        self.font = font
        self.shop_rect = pygame.Rect(600, 0, 200, 600)

    def draw(self, surface):
        pygame.draw.rect(surface, (50, 50, 50), self.shop_rect)
        text = self.font.render("SHOP", True, (255, 255, 255))
        surface.blit(text, (self.shop_rect.x + 50, 20))