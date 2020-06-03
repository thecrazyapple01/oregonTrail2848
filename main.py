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
font = pg.font.SysFont('Arial', 30)


def draw_background():
    screen.fill(black)


def draw_menu():
    # Start new game option
    text_start = font.render("Start a new game [SPACE]", True, white)
    text_start_rect = text_start.get_rect()
    text_start_rect.centerx = int(width_px / 2)
    text_start_rect.centery = int(height_px / 8)
    screen.blit(text_start, text_start_rect)

    # Instructions option
    text_instr = font.render("Read the instructions [I]", True, white)
    text_instr_rect = text_instr.get_rect()
    text_instr_rect.centerx = int(width_px / 2)
    text_instr_rect.centery = int(height_px * 3 / 8)
    screen.blit(text_instr, text_instr_rect)


def draw_exit_menu():
    # Main question
    text_main = font.render("Do you really want to exit? [Y/N]", True, white)
    text_main_rect = text_main.get_rect()
    text_main_rect.centerx = int(width_px / 2)
    text_main_rect.centery = int(height_px / 2)
    screen.blit(text_main, text_main_rect)


def draw_instructions():
    #Main text
    text_main = font.render("Here instructions will be written...", True, white)
    text_main_rect = text_main.get_rect()
    text_main_rect.centerx = int(width_px / 2)
    text_main_rect.centery = int(height_px / 4)
    screen.blit(text_main, text_main_rect)


screen = pg.display.set_mode(reso)
screen.fill(grey)

running = True
in_menu = True
in_exit_menu = False
in_instructions = False

while running:
    # Draw all the things
    draw_background()
    if in_menu:
        draw_menu()
    elif in_exit_menu:
        draw_exit_menu()
    pg.display.flip()

    # Start of the commands
    pg.event.pump()
    keys = pg.key.get_pressed()

    if in_menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                print("Started new game")

            if event.type == pg.KEYDOWN and event.key == pg.K_i:
                print("Opened instructions")

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                in_exit_menu = True
                in_menu = False

    if in_exit_menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

            if event.type == pg.KEYDOWN and event.key == pg.K_y:
                running = False
                pg.quit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_n:
                in_menu = True
                in_exit_menu = False
pg.quit()
