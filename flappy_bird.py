# Andy Truong
# start modules
import pgzrun
import sys
from random import*
import pygame
import os

# create constants
WIDTH = 800
HEIGHT = 600
score = 0
highscore = 0
tick = 0
gameOver = False
running = True
outText = ""
name = ""   
font = pygame.font.Font('2026-10COMP-BirdGame-AT/font/Pixelon.ttf', 70)
font2 = pygame.font.Font('2026-10COMP-BirdGame-AT/font/Pixeled.ttf', 40)
font3 = pygame.font.Font('2026-10COMP-BirdGame-AT/font/Pix32.ttf', 40)
button_width = 160
button_height = 50
button_x = (WIDTH // 2) - (button_width // 2)
button_y = (HEIGHT // 2) + 50
buttons = Rect((button_x, button_y), (button_width, button_height))
entered = False
won = False

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

# highscore
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
        outText = f"Congratulations! You beat the highscore! Your score was: {score}"
    else:
        outText = f"Your score was: {score}. The current highscore is: {highscore}"


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

def draw():
    screen.clear()
    screen.fill((135, 206, 235))  
    
    if not start:
        screen.draw.text("Click the game to start!", center=(WIDTH//2, HEIGHT//2 - 50), color=(255, 255, 255), fontsize=30)
        bird.draw()
        return

    if not gameOver:
        bird.draw()
        screen.draw.text(f"Score: {score}", (10, 10), color=(255, 255, 255))
    else:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2 - 120), color=(255, 0, 0), fontsize=50)
        screen.draw.text(outText, center=(WIDTH//2, HEIGHT//2 - 50), color=(255, 255, 255), fontsize=20)
        screen.draw.filled_rect(buttons, (0, 200, 100))  
        
        text_center_x = buttons.x + (buttons)
        text_center_y = buttons.y + (buttons.height // 2)
        screen.draw.text("Play Again?", center=(text_center_x, text_center_y), color=(255, 255, 255), fontsize=24)


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

# pow pow
def on_key_down(key):
    global name, entered
    if gameOver and not entered:
        pass

# runs everything
pgzrun.go()