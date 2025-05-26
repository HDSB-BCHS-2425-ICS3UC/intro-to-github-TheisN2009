import pygame

# Define colours
black = (0, 0, 0)
green = (0, 255, 0)

# Initialize pygame
pygame.init()

# Screen setup
width, height = 720, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Snake setup
snake_position = [width // 2, height // 2]
snake_size = [10, 10]
snake_speed = 10
direction = 'RIGHT'  # Initial direction

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Direction input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_position[1] -= snake_speed
    elif direction == 'DOWN':
        snake_position[1] += snake_speed
    elif direction == 'LEFT':
        snake_position[0] -= snake_speed
    elif direction == 'RIGHT':
        snake_position[0] += snake_speed

    # Wrap around screen
    if snake_position[0] >= width:
        snake_position[0] = 0
    elif snake_position[0] < 0:
        snake_position[0] = width - snake_size[0]
    if snake_position[1] >= height:
        snake_position[1] = 0
    elif snake_position[1] < 0:
        snake_position[1] = height - snake_size[1]

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], snake_size[0], snake_size[1]))
    pygame.display.flip()

    # Control game speed
    clock.tick(15)

pygame.quit()