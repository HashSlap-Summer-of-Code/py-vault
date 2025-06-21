import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Snake & Food
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def generate_food():
    return [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]

def show_score(score):
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

def game_over(score):
    screen.fill(BLACK)
    msg = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def main():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_pos = generate_food()
    score = 0
    speed = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_w] and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key in [pygame.K_DOWN, pygame.K_s] and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key in [pygame.K_LEFT, pygame.K_a] and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key in [pygame.K_RIGHT, pygame.K_d] and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        if direction == 'UP':
            snake_pos[1] -= CELL_SIZE
        elif direction == 'DOWN':
            snake_pos[1] += CELL_SIZE
        elif direction == 'LEFT':
            snake_pos[0] -= CELL_SIZE
        elif direction == 'RIGHT':
            snake_pos[0] += CELL_SIZE

        # Game over on collision
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
            snake_pos in snake_body):
            game_over(score)

        # Update snake
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_pos = generate_food()
        else:
            snake_body.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
        show_score(score)
        pygame.display.update()
        clock.tick(speed + score // 5)

if __name__ == "__main__":
    main()
