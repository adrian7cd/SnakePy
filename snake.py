import pygame

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
# Set sounds and music
#pick_up_sound = pygame.mixer.Sound()

# Set images
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

  display.fill(WHITE)

  # HUD
  display.blit(title_text, title_rect)
  display.blit(score_text, score_rect)

  pygame.draw.rect(display, GREEN, head_coord)
  pygame.draw.rect(display, RED, apple_coord)

  # Update display
  pygame.display.update()
  clock.tick(FPS)

# END GAME
pygame.quit()
