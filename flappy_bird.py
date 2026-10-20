# Andy Truong
# start modules
import pgzrun
import sys
from random import*

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False 

# print welcome
print('Welcome!\nThe game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

# make background
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

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
        pipe(266, 400, 220),
        pipe(532, 180, 220),
        pipe(798, 415, 220)
        ]

def updatePipes(self):
    self.top.x -= 1
    self.bottom.x -= 1
    if self.top.x < -44:
        self.top.x = 844
        self.bottom.x = 844
        self.gap = randint(160, 260)
        minimum = -250 + (300 // 2) + (self.gap // 2)
        maximum = 850 - ((300 // 2) + (self.gap // 2))
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
        screen.fill((0, 0, 0))  # RGB coloring for black background
        screen.draw.text("Game Over!", center=(400, 300), fontsize=60)
        screen.draw.text("Final Score: " + str(score), center=(400, 360), fontsize=40)
    else:
        # draw background
        background.draw()
        # draw characters
        bird.draw()
        # draw actors
        for pipe in pipeslist:
            drawPipes(pipe)
        screen.draw.text("Score: " + str(score), topleft=(20, 20), fontsize=30)

# update everything
def update():
    global score, gameOver
    if gameOver == True:
        return
    # update bird
    bird.y = bird.y + 2
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
    # bird hits pipes
    

# moving
def on_mouse_down():
    bird.y -= 50

# runs everything
pgzrun.go()