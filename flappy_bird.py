# Andy Truong
# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600

# print welcome
print('The game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

# make background
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# make pipes
class Pipes():
    def _init_(self, parameter1 = 50, parameter2 = 100, parameter3 = 200):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        top.y = 100 - (100(300) + 50)
        bottom.y = 100 + 100(300) + 50
top = Actor("top")
bottom = Actor("bottom")

# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw characters
    bird.draw()

# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes

    # bird hits bottom of screen
    if bird.y > 600:
        print("Game Over!")
        sys.exit()
    # bird hits pipes


# moving
def on_mouse_down():
    bird.y -= 50

# runs everything
pgzrun.go()