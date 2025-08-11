import pygame
import settings
from entities.tile import Tile
from hud.hud import HUD

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Jeu de gestion iso")
        self.clock = pygame.time.Clock()

        # Charger assets
        self.tile_img = pygame.image.load("assets/tiles/grass.png").convert_alpha()

        # Plateau
        self.tiles = [Tile(x, y, self.tile_img) for x in range(settings.GRID_WIDTH)
                                                 for y in range(settings.GRID_HEIGHT)]

        # HUD
        self.font = pygame.font.Font(None, 30)
        self.hud = HUD(self.font)

        # Décalage pour centrer le plateau
        self.offset_x = settings.SCREEN_WIDTH // 2
        self.offset_y = 50

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 100, 200))  # fond bleu ciel

            # Dessiner plateau
            for tile in self.tiles:
                tile.draw(self.screen, self.offset_x, self.offset_y)

            # Dessiner HUD
            # self.hud.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(settings.FPS)

        pygame.quit()