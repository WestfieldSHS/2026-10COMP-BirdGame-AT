# Andy Truong
# start modules
import pgzrun
import sys
from random import*
import pygame

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
tick = 0
gameOver = False
running = True
BASE_DIR = os.path.dirname(__file__) 
SOUND_PATH = os.path.join(BASE_DIR, "sound", "2026-10COMP-BirdGame-AT/sound/chirps.mp3") 
flap_sfx = pygame.mixer.Sound(SOUND_PATH)
font = pygame.font.Font('2026-10COMP-BirdGame-AT/font/Pixelon.ttf', 70)
font2 = pygame.font.Font('2026-10COMP-BirdGame-AT/font/Pixeled.ttf', 40)
font3 = pygame.font.Font('2026-10COMP-BirdGame-AT/font/Pix32.ttf', 40)

# print welcome
print('Welcome!\nThe game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

# make background
background = Actor("bg2")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# tryna make sound


# make pipes
class pipe:
    def __init__(self, x, center_y, gap):
        self.x = x
        self.center_y = center_y
        self.gap = gap

        self.top = Actor("top")
        self.bottom = Actor("bottom")

        self.top.x = x
        self.top.y = center_y - (300 + gap / 2)
        self.bottom.x = x
        self.bottom.y = center_y + 300 + gap / 2
pipeslist = [
        pipe(466, 400, 220),
        pipe(732, 180, 220),
        pipe(998, 415, 220)
        ]

def updatePipes(self):
    self.top.x -= 1
    self.bottom.x -= 1
    if self.top.x < -44:
        self.top.x = 844
        self.bottom.x = 844
        self.gap = randint(180, 250)
        minimum = -150 + (300 // 2) + (self.gap // 2)
        maximum = 750 - ((300 // 2) + (self.gap // 2))
        self.center_y = randint(minimum, maximum)
        self.top.y = self.center_y - (300 + self.gap / 2)
        self.bottom.y = self.center_y + 300 + self.gap / 2
    for pipe in pipeslist:
            for part in [pipe.top, pipe.bottom]:
                if part.colliderect(bird):
                    gameOver = True
        
def drawPipes(self):
    self.top.draw()
    self.bottom.draw()

# draw everything to screen
def draw():
    if gameOver == True:
        screen.fill((0, 0, 0))
        fontah2 = font2.render("Game Over!", True, 'white')
        screen.blit(fontah2, (200, 250))

        fontah3 = font3.render(f'Final Score: {score}', True, 'white')
        screen.blit(fontah3, (200, 360))
#        fontah3 = font3.render(f'Highscore: {highscore}', True, 'white')
#        screen.blit(fontah3, (200, 410))

    else:
        # draw background
        background.draw()
        # draw characters
        bird.draw()
        # draw actors
        for pipe in pipeslist:
            drawPipes(pipe)
        fontah1 = font.render(f'{score}', True, 'white')
        screen.blit(fontah1, (400,20))

# update everything
def update():
    global score, gameOver, tick
    if gameOver == True:
        return
    tick += 1
    if tick == 31:
        tick = 0
    # update bird
    bird.y = bird.y + 2
    if tick == 15:
        bird.image = "bird1"
    elif tick == 30:
        bird.image = "bird2"
    # update pipes
    for pipe in pipeslist:
        updatePipes(pipe)
        if pipe.top.x == 160:
            score += 1
        if bird.colliderect(pipe.top) or bird.colliderect(pipe.bottom):
            gameOver = True
    # bird hits bottom of screen
    if bird.y > 600 or bird.top < 0:
        gameOver = True
    
# moving
def on_mouse_down():
    bird.y -= 50


# runs everything
pgzrun.go()