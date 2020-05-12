import pygame as pg

height_px = 500
width_px = 600
reso = (width_px, height_px)
black = (0, 0, 0)
grey = (127, 127, 127)

pg.init()

pg.init()

screen = pg.display.set_mode(reso)
screen.fill(grey)

car = pg.image.load("images/car.png")
carimg = pg.transform.scale(car, (100, 100))
carrect = carimg.get_rect()
carrect.centerx = 500
carrect.centery = 250
screen.blit(carimg, carrect)
pg.display.flip()

for t in range(12000):
    if t % 20 == 0:
        carrect.centerx -= 1
        screen.fill(grey)
        screen.blit(carimg, carrect)
    pg.display.flip()



pg.quit()

