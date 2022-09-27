import pygame, random

# Init pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("SnakeGame")

# Game Clock FPS
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render("SnakeGame", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# Set images5
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display, GREEN, head_coord)

body_coords = []



# main loop
game_running = True
while game_running:
  # check if user wants to quit the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        snake_dx = -1*SNAKE_SIZE
        snake_dy = 0
      if event.key == pygame.K_RIGHT:
        snake_dx = SNAKE_SIZE
        snake_dy = 0
      if event.key == pygame.K_UP:
        snake_dx = 0
        snake_dy = -1*SNAKE_SIZE
      if event.key == pygame.K_DOWN:
        snake_dx = 0
        snake_dy = SNAKE_SIZE

  body_coords.insert(0, head_coord)
  body_coords.pop()

  head_x += snake_dx
  head_y += snake_dy
  head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

  if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
      display.blit(game_over_text, game_over_rect)
      display.blit(continue_text, continue_rect)
      pygame.display.update()

      is_paused = True
      while is_paused:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            score = 0

            head_x = WINDOW_WIDTH//2
            head_y = WINDOW_HEIGHT//2 + 100
            head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
                    
            body_coords = []

            snake_dx = 0
            snake_dy = 0

            is_paused = False
          if event.type == pygame.QUIT:
            is_paused = False
            running = False

  if head_rect.colliderect(apple_rect):
    score += 1

    apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
    apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
    apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

    body_coords.append(head_coord)

  score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)

  display.fill(BLACK)
    
  display.blit(title_text, title_rect)
  display.blit(score_text, score_rect)

  for body in body_coords:
      pygame.draw.rect(display, DARKGREEN, body)
  head_rect = pygame.draw.rect(display, GREEN, head_coord)
  apple_rect = pygame.draw.rect(display, RED, apple_coord)

    #Update display and tick clock
  pygame.display.update()
  clock.tick(FPS)

#End the game
pygame.quit()
