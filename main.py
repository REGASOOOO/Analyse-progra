import pygame

pygame.init()
screen_size = pygame.display.get_desktop_sizes()[0]
print(f"Screen size: {screen_size[1]}")
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()