# Andy Truong
# start modules
import pgzrun
import sys
from random import *
import pygame
import os

# constants / variables
WIDTH = 800
HEIGHT = 600
score = 0
highscore = 0
tick = 0
gameOver = False
running = True
outText = ""
name = "Player"  
entered = False
won = False
start = False
count = 0
y0 = 300
t = 0
g = 9.81

# fonts
pygame.font.init()
font = pygame.font.Font("2026-10COMP-BirdGame-AT/font/Pix32.ttf", 70)
font2 = pygame.font.Font("2026-10COMP-BirdGame-AT/font/Pixeled.ttf", 40)
font3 = pygame.font.Font("2026-10COMP-BirdGame-AT/font/Pixelon.ttf", 70)
font4 = pygame.font.Font("2026-10COMP-BirdGame-AT/font/ARCADECLASSIC.TTF", 50)
font5 = pygame.font.Font("2026-10COMP-BirdGame-AT/font/Reset.ttf", 30)

# button pls work
button_width = 160
button_height = 50
button_x = (WIDTH // 2) - (button_width // 2)
button_y = (HEIGHT // 2) + 50
buttons = Rect((button_x, button_y), (button_width, button_height))

print('Welcome!\nThe game is about to start!\nClick the mouse to "flap" upwards\nDodge the pipes and the floor\nGood luck and have fun!')

background = Actor("bg2")
background.x = 400
background.y = 300

bird = Actor("bird")
bird.x = 160
bird.y = 300

title = Actor("flappybird")
title.x = 400
title.y = 100

# restart everything so no bug pls
def restart():
    global score, gameOver, tick, start, t, y0, won, outText, pipeslist
    bird.x = 160
    bird.y = 300
    y0 = bird.y
    t = 0
    score = 0
    tick = 0
    gameOver = False
    start = False
    won = False
    outText = ""
    pipeslist = [
        pipe(466, 400, 220),
        pipe(732, 180, 220),
        pipe(998, 415, 220)
    ]

# store the best highscore
def check_highscore_pt1():
    global highscore, outText
    try:
        with open("highscore.txt", "r") as file:
            line = file.readline().strip()
            if line == "":
                highscore = 0
            else:
                highscore = int(line)
    except FileNotFoundError:
        highscore = 0

    if score > highscore:
        with open("highscore.txt", "w") as file:
            file.write(str(score))
        outText = f"New Highscore! Score: {score}"
    else:
        outText = f"Score: {score}. Highscore: {highscore}"

def check_highscore_pt2():
    global won, outText
    scores_dict = {}
    try:
        with open("highscores.txt", "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        scores_dict[parts[0]] = int(parts[1])
    except FileNotFoundError:
        pass

    if name in scores_dict:
        if score > scores_dict[name]:
            won = True
            scores_dict[name] = score
    else:
        won = True
        scores_dict[name] = score

    with open("highscores.txt", "w") as file:
        for p_name, p_score in scores_dict.items():
            file.write(f"{p_name}:{p_score}\n")

    if won:
        outText = f"New Personal High Score! {name}: {score}"
    else:
        outText = f"Game Over, {name}! Your Score: {score}"

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
    self.top.x -= 2
    self.bottom.x -= 2
    if self.top.x < -44:
        self.top.x = 844
        self.bottom.x = 844
        self.gap = randint(180, 250)
        minimum = -150 + (300 // 2) + (self.gap // 2)
        maximum = 750 - ((300 // 2) + (self.gap // 2))
        self.center_y = randint(minimum, maximum)
        self.top.y = self.center_y - (300 + self.gap / 2)
        self.bottom.y = self.center_y + 300 + self.gap / 2

def drawPipes(self):
    self.top.draw()
    self.bottom.draw()

# draw everything
def draw():
    # clears everything off the screen then draws background
    screen.clear()
    background.draw()
    
    # pauses game til someone touches / clicks
    if not start:
        fontah4 = font4.render("Click the game to start!", True, "black")
        screen.blit(fontah4, (100, 200))
        bird.draw()
        title.draw()
        return
    # score and pipes when no die
    if not gameOver:
        bird.draw()
        for p in pipeslist:
            drawPipes(p)
        fontah3 = font3.render(f"{score}", True, "white")
        screen.blit(fontah3, (400, 20))
    # gameover screen
    else:
        screen.fill((0, 0, 0))
        fontah = font.render("Game Over!", True, "white")
        screen.blit(fontah, (200, 200))
        fontah2 = font2.render(f"{outText}", True, "white")
        screen.blit(fontah2, (200, 300))
        screen.draw.filled_rect(buttons, (0, 0, 0))
        text_center_x = buttons.x + (button_width // 2)
        text_center_y = buttons.y + (button_height // 2)
        screen.draw.text("Play Again?", center=(text_center_x, text_center_y), color=(255, 255, 255), fontsize=24, font=font5)


# update everything
def update():
    global score, gameOver, tick, t, y0, start, count
    if not start:
        # bird jumpys
        count = (count + 1) % 100
        if count > 50:
            bird.y += 0.5
        else:
            bird.y -= 0.5
        return
    if gameOver:
        return
    # bird anims
    tick += 1
    if tick == 31:
        tick = 0
    t += 0.1
    bird.y = y0 + (0.5 * g * (t ** 2))
    if tick == 15:
        bird.image = "bird1"
    elif tick == 30:
        bird.image = "bird2"
    # bird hits pipeuh
    for p in pipeslist:
        updatePipes(p)
        if p.top.x == 160:
            score += 1
        if bird.colliderect(p.top) or bird.colliderect(p.bottom):
            gameOver = True
            check_highscore_pt1()

    if bird.y > 600 or bird.y < 0:
        gameOver = True
        check_highscore_pt1()
# birb
def on_mouse_down(pos):
    global start, t, y0, gameOver

    if not start:
        start = True
        y0 = bird.y
        t = 0
        return

    if not gameOver:
        t = 0
        bird.y -= 50
        y0 = bird.y
    else:
        if buttons.collidepoint(pos):
            restart()

def on_key_down(key):
    global name, entered
    if gameOver and not entered:
        pass

pgzrun.go()
