import pygame as pg
import time
import random
import math

pg.init()

height_px = 480
width_px = 900
reso = (width_px, height_px)
black = (0, 0, 0)
grey = (127, 127, 127)
white = (255, 255, 255)
fontArial30 = pg.font.SysFont('Arial', 30)
texts = []


def draw_background():
    screen.fill(black)


class TextToDraw():
    def __init__(self, name="", text="", posx=int(width_px / 2), posy=int(height_px / 2), color=white, font=fontArial30):
        self.name = str(name)
        self.text = str(text)
        self.centerx = int(posx)
        self.centery = int(posy)
        self.color = color
        self.font = font
        # self.visible = False -- not sure if I need it

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = self.centerx
        text_rect.centery = self.centery
        screen.blit(text_surface, text_rect)


# Initialise texts
texts.append(TextToDraw("main_start", "Start a new game [SPACE]", posy=int(height_px / 8)))
texts.append(TextToDraw("main_instructions", "Read the instructions [I]", posy=int(height_px * 3 / 8)))
texts.append(TextToDraw("exit_main", "Do you really want to exit? [Y/N]"))
texts.append(TextToDraw("instructions_line1", "Here instructions will be written...", posy=int(height_px / 4)))

screen = pg.display.set_mode(reso)
screen.fill(grey)

running = True
state = "main"

while running:
    # Draw all the things
    draw_background()
    for text in texts:
        if text.name.split('_')[0] == state:
            text.draw()
    pg.display.flip()

    # Start of the commands
    pg.event.pump()
    keys = pg.key.get_pressed()

    if state == "main":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                print("Started new game")

            if event.type == pg.KEYDOWN and event.key == pg.K_i:
                state = "instructions"

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                state = "exit"
    elif state == "exit":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_y:
                running = False
                pg.quit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_n:
                state = "main"
    elif state == "instructions":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                state = "main"

pg.quit()
