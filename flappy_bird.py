# Andy Truong
# start modules
import pgzrun
import sys

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

# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw characters
    bird.draw()
    # draw actors
    for pipe in pipeslist:
        pipe.top.draw()
        pipe.bottom.draw()


# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes
    for pipe in pipeslist:
        pipe.top.x -= 1
        pipe.bottom.x -= 1
        if pipe.top.x < -44:
            pipe.top.x = 844
            pipe.bottom.x = 844
    # bird hits bottom of screen
            if bird.y > 600:
                print("Game Over!")
                sys.exit()
    # bird hits pipes
            if bird.colliderect(pipe.top):
                print("Hit!\nGame Over!")
                sys.exit()  
            if bird.colliderect(pipe.bottom):
                print("Hit!\nGame Over!")
                sys.exit() 
    # global?
        global score, gameOver 
        if bird.colliderect(pipe.top) or bird.colliderect(pipe.bottom) or bird.bottom > 600 or bird.top < 0: 
                gameOver = True
        if pipe.top.x < 0: 
                score += 1
        if gameOver == True:
                print("Hit!\nGame Over!")
                print(f"Final Score: {score}")
                sys.exit()

# moving
def on_mouse_down():
    bird.y -= 50

# runs everything
pgzrun.go()