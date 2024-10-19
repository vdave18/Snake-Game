import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display size
dis_width = 800
dis_height = 600

# Set the snake's block size and speed
snake_block = 10
snake_speed = 15

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set up the clock for controlling the snake's speed
clock = pygame.time.Clock()

# Set the font styles
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def score(score):
    value = score_font.render(f"Your Score: {score}", True, blue)
    dis.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def game_loop():
    game_over = False
    game_close = False

    # Set initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Set initial movement
    x1_change = 0
    y1_change = 0

    # Create the snake's body
    snake_list = []
    length_of_snake = 1

    # Set the position of the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # Draw the food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Update the snake's position
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collisions with the snake itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
