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
big_font = pygame.font.SysFont("arial", 48)

snake = [(15, 10), (14, 10), (13, 10)]
direction = (1, 0)
score = 0
game_over = False


def spawn_apple():
    while True:
        position = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if position not in snake:
            return position


apple = spawn_apple()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_SPACE:
                    snake = [(15, 10), (14, 10), (13, 10)]
                    direction = (1, 0)
                    apple = spawn_apple()
                    score = 0
                    game_over = False
            else:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                if event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                if event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                if event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

    if not game_over:
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]

        hit_wall = head_x < 0 or head_x >= COLS or head_y < 0 or head_y >= ROWS
        hit_self = (head_x, head_y) in snake

        if hit_wall or hit_self:
            game_over = True
        else:
            snake.insert(0, (head_x, head_y))

            if snake[0] == apple:
                apple = spawn_apple()
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

    if game_over:
        over_text = big_font.render("Game Over", True, WHITE)
        over_rect = over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        screen.blit(over_text, over_rect)

        restart_text = font.render("Press SPACE to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        screen.blit(restart_text, restart_rect)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()