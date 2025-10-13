import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
snake_dx = 0
snake_dy = 0
snake_body = [(snake_x, snake_y)]

# Set up the food
food_x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
food_y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy != 1:
                snake_dx = 0
                snake_dy = -1
            elif event.key == pygame.K_DOWN and snake_dy != -1:
                snake_dx = 0
                snake_dy = 1
            elif event.key == pygame.K_LEFT and snake_dx != 1:
                snake_dx = -1
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -1:
                snake_dx = 1
                snake_dy = 0

    # Move the snake
    snake_x += snake_dx * BLOCK_SIZE
    snake_y += snake_dy * BLOCK_SIZE
    snake_body.insert(0, (snake_x, snake_y))

    # Check for collisions with the wall
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Check for collisions with the food
    if (snake_x, snake_y) == (food_x, food_y):
        food_x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        food_y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
    else:
        snake_body.pop()

    # Check for collisions with the snake body
    if (snake_x, snake_y) in snake_body[1:]:
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for x, y in snake_body:
        pygame.draw.rect(screen, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(SPEED)