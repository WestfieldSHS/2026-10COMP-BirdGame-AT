# Andy Truong
# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600

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
class Pipes:
    def __init__(self, x, center_y, gap):
        self.x = x
        self.center_y = center_y
        self.gap = gap

        self.top = Actor("top")
        self.bottom = Actor("bottom")

        self.top.x = x
        self.top.y = center_y - (150 + gap / 2)
        self.bottom.x = x
        self.bottom.y = center_y + 150 + gap / 2
pipeslist = [
        Pipes(266, 400, 220),
        Pipes(532, 180, 220),
        Pipes(798, 415, 220)
        ]

# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw characters
    bird.draw()
    # draw actors
    for Pipes in pipeslist:
        Pipes.top.draw()
        Pipes.bottom.draw()


# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes
    for Pipes in pipeslist:
        Pipes.top.x -= 1
        Pipes.bottom.x -= 1
    if Pipes.top.x < -44:
        Pipes.top.x = 844
        Pipes.bottom.x = 844
    # bird hits bottom of screen
    if bird.y > 600:
        print("Game Over!")
        sys.exit()
    # bird hits pipes
    if bird.colliderect(Pipes):
        print("Hit!")
        sys.exit()


# moving
def on_mouse_down():
    bird.y -= 50

# runs everything
pgzrun.go()