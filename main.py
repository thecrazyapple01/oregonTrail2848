import pygame as pg
import time
import random
import math

pg.init()

height_px = 600
width_px = 1000
reso = (width_px, height_px)
black = (0, 0, 0)
grey = (127, 127, 127)
white = (255, 255, 255)
font = pg.font.SysFont('Arial', 30)


def draw_background():
    screen.fill(black)


def draw_menu():
    # Start new game option
    text_start = font.render(f"Start a new game [SPACE]", False, white)
    text_start_rect = text_start.get_rect()
    text_start_rect.centerx = int(width_px / 2)
    text_start_rect.centery = int(height_px / 8)
    screen.blit(text_start, text_start_rect)

    # Instructions option
    text_instr = font.render(f"Read the instructions [I]", False, white)
    text_instr_rect = text_instr.get_rect()
    text_instr_rect.centerx = int(width_px / 2)
    text_instr_rect.centery = int(height_px * 3 / 8)
    screen.blit(text_instr, text_instr_rect)


screen = pg.display.set_mode(reso)
screen.fill(grey)

running = True
in_menu = True

while running:
    # Draw all the things
    draw_background()
    draw_menu()
    pg.display.flip()

    # Start of the commands
    pg.event.pump()
    keys = pg.key.get_pressed()

    if in_menu:
        space_key_pressed = False
        i_key_pressed = False
        escape_key_pressed = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not space_key_pressed:
                space_key_pressed = True
                print("Started new game")
            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                space_key_pressed = False

            if event.type == pg.KEYDOWN and event.key == pg.K_i and not i_key_pressed:
                i_key_pressed = True
                print("Opened instructions")
            if event.type == pg.KEYUP and event.key == pg.K_i:
                i_key_pressed = False

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE and not escape_key_pressed:
                escape_key_pressed = True
                print("Tries to exit")
            if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                escape_key_pressed = False

pg.quit()
