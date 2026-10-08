import pygame

pygame.init()

CELL_SIZE = 20
COLS = 30
ROWS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

GREEN = (80, 200, 120)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snake = [(15, 10), (14, 10), (13, 10)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    for segment in snake:
        x = segment[0] * CELL_SIZE
        y = segment[1] * CELL_SIZE
        pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit() 