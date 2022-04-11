import pygame
from random import randrange
from time import sleep
pygame.init()

# ------- Constants -------- #
white = (255, 255, 255)
black = (0, 0, 0)
red =   (255, 0, 0)
green = (0, 155, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 10
FOOD_SIZE = 10
FPS = 15
# -------------------------- #


# ----------------------------- Setup ----------------------------- #
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('old snake')
clock = pygame.time.Clock()
# ----------------------------------------------------------------- #


def on_screen_message(message, color, x, y, offset):
    """Display a message on screen"""
    OFFSET = 100
    font = pygame.font.SysFont(None, 50)
    screen_text = font.render(message, True, color)
    game_screen.blit(screen_text, (x - offset, y - offset))


def speed_handler(move_event: pygame.event.Event) -> tuple[int, int]:
    """Process keypress and return a velocity vector"""
    x_speed = 0
    y_speed = 0
    if move_event.key == pygame.K_LEFT or move_event.key == pygame.K_a:
        x_speed = -SNAKE_SIZE
        y_speed = 0
    if move_event.key == pygame.K_RIGHT or move_event.key == pygame.K_d:
        x_speed = SNAKE_SIZE
        y_speed = 0
    if move_event.key == pygame.K_UP or move_event.key == pygame.K_w:
        y_speed = -SNAKE_SIZE
        x_speed = 0
    if move_event.key == pygame.K_DOWN or move_event.key == pygame.K_s:
        y_speed = SNAKE_SIZE
        x_speed = 0
    return x_speed, y_speed



def snake(body, block_size):
    """Draw the snake"""
    for segment in body:
        x, y = segment
        pygame.draw.rect(game_screen, green, [x, y, block_size, block_size])


def game_loop():
    """Main game loop"""
    x_pos = SCREEN_WIDTH / 2 - SNAKE_SIZE
    y_pos = SCREEN_HEIGHT / 2 - SNAKE_SIZE
    food_x = randrange(0, SCREEN_WIDTH - FOOD_SIZE, 10)
    food_y = randrange(0, SCREEN_HEIGHT - FOOD_SIZE, 10)
    snake_list = []
    snake_length = 1

    dx = 0
    dy = 0
    close_game = False
    game_over = False
    while not close_game:
        # Loop for when the game ends
        while game_over:
            game_screen.fill(white)
            on_screen_message('Game over!', red, SCREEN_WIDTH / 2 + 80, SCREEN_HEIGHT / 2 + 100, 200)
            on_screen_message('Press enter to play again', red, SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2 + 150, 200)
            on_screen_message('Press Q to quit.', red, SCREEN_WIDTH / 2 + 60, SCREEN_HEIGHT / 2 + 200, 200)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close_game = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close_game = True
                        game_over = False
                    if event.key == pygame.K_RETURN:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game = True
            if event.type == pygame.KEYDOWN:
                dx, dy = speed_handler(event)

        clock.tick(FPS)
        x_pos += dx
        y_pos += dy
        if x_pos < 0 or x_pos > SCREEN_WIDTH - SNAKE_SIZE or y_pos < 0 or y_pos > SCREEN_HEIGHT - SNAKE_SIZE:
            game_over = True

        game_screen.fill(white)
        # Draw Food and snake head
        pygame.draw.rect(game_screen, red, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))
        snake(snake_list, SNAKE_SIZE)

        snake_head = [x_pos, y_pos]
        snake_list.append(snake_head)


        if len(snake_list) > snake_length:
            del snake_list[0]


        # Eat food
        if x_pos == food_x and y_pos == food_y:
            food_x = randrange(0, SCREEN_WIDTH - FOOD_SIZE, 10)
            food_y = randrange(0, SCREEN_HEIGHT - FOOD_SIZE, 10)
            snake_length += 1



        pygame.display.update()

    pygame.quit()
    quit()


game_loop()

