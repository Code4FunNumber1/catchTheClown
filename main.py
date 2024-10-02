#setup
import pygame, random

pygame.init()

#settings
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()

#windowSettings
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch The Clown")

#constants
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 5
CLOWN_ACCELERATION = 1

#varibles
score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

#colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

#font
font = pygame.font.Font("assets/Franxurter.ttf", 32)

#textBoxes
title_text = font.render("Catch the Clown!", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render("Score: " + str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render("Game Over!", True, BLUE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to continue.", True, YELLOW)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

#clown
clown_image = pygame.image.load("assets/clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

#background
background_image = pygame.image.load("assets/background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

#sounds
click_sound = pygame.mixer.Sound("assets/click_sound.wav")
miss_sound = pygame.mixer.Sound("assets/miss_sound.wav")
pygame.mixer.music.load("assets/ctc_background_music.wav")
pygame.mixer.music.play(-1)