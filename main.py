import pygame
import random
import sys
import os
 
pygame.init()
pygame.mixer.init()
 
 
def resource_path(relative_path):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relative_path)
 
 
def get_save_path():
    if getattr(sys, "frozen", False):
        return os.path.join(os.path.dirname(sys.executable), "highscore.txt")
    return "highscore.txt"
 
 
CELL_SIZE = 32
COLS = 25
ROWS = 18
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
OBSTACLE_COUNT = 8
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)
big_font = pygame.font.SysFont("arial", 48)
small_font = pygame.font.SysFont("arial", 20)
 
 
def load_image(theme_name, file_name):
    image = pygame.image.load(resource_path("assets/" + theme_name + "/" + file_name)).convert_alpha()
    return pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
 
 
def load_theme(theme_name):
    images = {}
    for name in ["head", "head_open", "body1", "body2", "tail", "apple", "golden_apple", "obstacle"]:
        images[name] = load_image(theme_name, name + ".png")
    background = pygame.image.load(resource_path("assets/" + theme_name + "/background.png")).convert()
    images["background"] = pygame.transform.scale(background, (WIDTH, HEIGHT))
    return images
 
 
themes = {
    "normal": load_theme("normal"),
    "neon": load_theme("neon"),
}
music_files = {
    "normal": resource_path("assets/music/pixelland.mp3"),
    "neon": resource_path("assets/music/funny_bit.mp3"),
}
nom_sound = pygame.mixer.Sound(resource_path("assets/music/nom.mp3"))
 
 
def play_music(theme_name):
    try:
        pygame.mixer.music.load(music_files[theme_name])
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Could not play music:", music_files[theme_name])
 
 
def get_angle(dx, dy):
    if dx == 1:
        return 0
    elif dy == -1:
        return 90
    elif dx == -1:
        return 180
    else:
        return 270
 
 
def draw_text(text, text_font, x, y):
    shadow = text_font.render(text, True, BLACK)
    label = text_font.render(text, True, WHITE)
    screen.blit(shadow, (x + 2, y + 2))
    screen.blit(label, (x, y))
 
 
def draw_centered(text, text_font, center_y):
    shadow = text_font.render(text, True, BLACK)
    label = text_font.render(text, True, WHITE)
    shadow_rect = shadow.get_rect(center=(WIDTH // 2 + 2, center_y + 2))
    label_rect = label.get_rect(center=(WIDTH // 2, center_y))
    screen.blit(shadow, shadow_rect)
    screen.blit(label, label_rect)
 
 
def get_theme_hint():
    if theme == "normal":
        return "Press T to switch to the neon theme"
    else:
        return "Press T to switch to the normal theme"
 
 
def get_free_cell():
    while True:
        position = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if position in snake or position in obstacles:
            continue
        if position == apple or position == golden:
            continue
        return position
 
 
def make_obstacles():
    result = []
    while len(result) < OBSTACLE_COUNT:
        position = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        near_start = abs(position[0] - 12) <= 5 and abs(position[1] - 9) <= 2
        if position not in result and not near_start:
            result.append(position)
    return result
 
 
def load_high_score():
    try:
        with open(get_save_path(), "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0
 
 
def save_high_score(value):
    with open(get_save_path(), "w") as file:
        file.write(str(value))
 
 
theme = "normal"
images = themes[theme]
play_music(theme)
 
snake = [(12, 9), (11, 9), (10, 9)]
direction = (1, 0)
score = 0
game_over = False
paused = False
started = False
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 15, 200, 60)
high_score = load_high_score()
obstacles = make_obstacles()
apple = None
golden = None
golden_steps = 0
apple = get_free_cell()
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not started and button_rect.collidepoint(event.pos):
                started = True
        if event.type == pygame.KEYDOWN:
            if event.scancode == pygame.KSCAN_T:
                if theme == "normal":
                    theme = "neon"
                else:
                    theme = "normal"
                images = themes[theme]
                play_music(theme)
                if paused:
                    pygame.mixer.music.pause()
 
            if not started:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    started = True
            elif game_over:
                if event.key == pygame.K_SPACE:
                    snake = [(12, 9), (11, 9), (10, 9)]
                    direction = (1, 0)
                    obstacles = make_obstacles()
                    golden = None
                    apple = get_free_cell()
                    score = 0
                    game_over = False
            else:
                if event.scancode == pygame.KSCAN_P:
                    paused = not paused
                    if paused:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                if event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                if event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                if event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
 
    if started and not game_over and not paused:
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
 
        hit_wall = head_x < 0 or head_x >= COLS or head_y < 0 or head_y >= ROWS
        hit_self = (head_x, head_y) in snake
        hit_obstacle = (head_x, head_y) in obstacles
 
        if hit_wall or hit_self or hit_obstacle:
            game_over = True
            if score > high_score:
                high_score = score
                save_high_score(high_score)
        else:
            snake.insert(0, (head_x, head_y))
 
            if snake[0] == apple:
                apple = get_free_cell()
                score = score + 1
                nom_sound.play()
            elif snake[0] == golden:
                golden = None
                score = score + 5
                nom_sound.play()
            else:
                snake.pop()
 
            if golden is None:
                if random.randint(1, 80) == 1:
                    golden = get_free_cell()
                    golden_steps = 50
            else:
                golden_steps = golden_steps - 1
                if golden_steps <= 0:
                    golden = None
 
    screen.blit(images["background"], (0, 0))
 
    for obstacle in obstacles:
        screen.blit(images["obstacle"], (obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE))
 
    screen.blit(images["apple"], (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE))
 
    if golden is not None:
        if golden_steps > 15 or golden_steps % 2 == 0:
            screen.blit(images["golden_apple"], (golden[0] * CELL_SIZE, golden[1] * CELL_SIZE))
 
    for i in range(1, len(snake)):
        segment = snake[i]
        ahead = snake[i - 1]
        angle = get_angle(ahead[0] - segment[0], ahead[1] - segment[1])
 
        if i == 1:
            image = images["body1"]
        elif i == len(snake) - 1:
            image = images["tail"]
        else:
            image = images["body2"]
 
        rotated_image = pygame.transform.rotate(image, angle)
        screen.blit(rotated_image, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE))
 
    mouth_open = False
    for step in range(1, 3):
        cell = (snake[0][0] + direction[0] * step, snake[0][1] + direction[1] * step)
        if cell == apple or cell == golden:
            mouth_open = True
 
    if mouth_open:
        head_image = images["head_open"]
    else:
        head_image = images["head"]
 
    head_angle = get_angle(direction[0], direction[1])
    rotated_head = pygame.transform.rotate(head_image, head_angle)
    screen.blit(rotated_head, (snake[0][0] * CELL_SIZE, snake[0][1] * CELL_SIZE))
 
    draw_text("Score: " + str(score), font, 10, 10)
    draw_text("Best: " + str(high_score), font, 10, 40)
 
    if paused:
        draw_centered("Paused", big_font, HEIGHT // 2)
 
    if game_over:
        draw_centered("Game Over", big_font, HEIGHT // 2 - 20)
        draw_centered("Press SPACE to restart", font, HEIGHT // 2 + 30)
 
    if not started:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
 
        draw_centered("SNAKE", big_font, HEIGHT // 2 - 90)
 
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            button_color = (120, 230, 150)
        else:
            button_color = (80, 200, 120)
        pygame.draw.rect(screen, button_color, button_rect, border_radius=12)
        play_label = font.render("PLAY", True, BLACK)
        screen.blit(play_label, play_label.get_rect(center=button_rect.center))
 
        draw_centered("Click PLAY or press SPACE", small_font, HEIGHT // 2 + 65)
        draw_centered("Arrow keys - move", small_font, HEIGHT // 2 + 95)
        draw_centered("P - pause", small_font, HEIGHT // 2 + 120)
 
    draw_centered(get_theme_hint(), small_font, HEIGHT - 20)
 
    speed = 10 + score // 3
    if speed > 20:
        speed = 20
 
    pygame.display.flip()
    clock.tick(speed)
 
pygame.quit()
 