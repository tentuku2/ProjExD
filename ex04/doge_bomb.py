from ast import Pass
from turtle import Screen
import pygame as pg
import sys

class game():

    def __init__(self):
        pg.display.set_caption("逃げろコウカトン！")
        clock = pg.time.Clock()
        screen_sfc = pg.display.set_mode((1600,900))
        screen_rct = screen_sfc.get_rect()
        bg  = pg.image.load("pg_bg.jpg")
        bg_rect = bg.get_rect()

        clock.tick(0.2)

        while True:
            screen_sfc.blit(bg,bg_rect)
            pg.display.update(bg_rect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            

if __name__ == "__main__":
    pg.init()
    game()
    pg.quit()
    sys.exit()
