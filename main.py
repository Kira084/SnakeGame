import pygame
import random

pygame.init()

CELL_SIZE = 20
COLS = 30
ROWS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

GREEN = (80, 200, 120)
RED = (220, 60, 60)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)

snake = [(15, 10), (14, 10), (13, 10)]
direction = (1, 0)
apple = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            if event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            if event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]

    hit_wall = head_x < 0 or head_x >= COLS or head_y < 0 or head_y >= ROWS
    hit_self = (head_x, head_y) in snake

    if hit_wall or hit_self:
        snake = [(15, 10), (14, 10), (13, 10)]
        direction = (1, 0)
        apple = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        score = 0
    else:
        snake.insert(0, (head_x, head_y))

        if snake[0] == apple:
            apple = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            score = score + 1
        else:
            snake.pop()

    screen.fill((30, 30, 30))

    for segment in snake:
        x = segment[0] * CELL_SIZE
        y = segment[1] * CELL_SIZE
        pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    apple_x = apple[0] * CELL_SIZE
    apple_y = apple[1] * CELL_SIZE
    pygame.draw.rect(screen, RED, (apple_x, apple_y, CELL_SIZE, CELL_SIZE))

    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()