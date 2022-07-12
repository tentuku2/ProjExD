import datetime
from enum import Flag
from shutil import move
import tkinter
from pygame.locals import *
import random
import pygame as pg
import sys
import tkinter.messagebox as tkm

BIRD_POSI = [0,0]


class Screen:
    def __init__(self,title,size,irast):
        pg.display.set_caption(title)
        self.suface_sfc = pg.display.set_mode(size)
        self.suface_rct = self.suface_sfc.get_rect()
        self.bgi_sfc  = pg.image.load(irast)
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.suface_sfc.blit(self.bgi_sfc, self.bgi_rct)

    def bird_chake_bound(self,move_key):
        if move_key[0] == 0:
            if self.suface_rct.height > BIRD_POSI[0]+move_key[1] > 0:
                return True
            else:
                return False
        elif move_key[1] == 1:
            if self.suface_rct.width > BIRD_POSI[1]+move_key[1] > 0 :
                return True
            else:
                return False

class Bird:
    key_delta = {pg.K_UP:[0,-1],pg.K_DOWN:[0,1],pg.K_RIGHT:[1,0],pg.K_LEFT:[-1,0]}

    def __init__(self,image,size,pos):
        pos = list(pos)
        BIRD_POSI[0] =  pos[0]
        BIRD_POSI[1] =  pos[1]
        self.kkimg_sfc = pg.image.load(image)
        self.kkimg_sfc = pg.transform.rotozoom(self.kkimg_sfc,0,2.0)
        self.kkimg_rct = self.kkimg_sfc.get_rect()
        self.kkimg_rct.center = BIRD_POSI[0],BIRD_POSI[1]

    def update(self,scr:Screen):
        self.key_states = pg.key.get_pressed()
        if self.key_states[pg.K_UP] == True:
            if 0 < self.kkimg_rct.centery :
                self.kkimg_rct.centery -= 1
        if self.key_states[pg.K_DOWN]==True:
            if scr.suface_rct.height > self.kkimg_rct.centery :
                self.kkimg_rct.centery += 1
        if self.key_states[pg.K_RIGHT]==True:
            if scr.suface_rct.width > self.kkimg_rct.centerx:
                self.kkimg_rct.centerx+=1
        if self.key_states[pg.K_LEFT]==True:
            if 0 < self.kkimg_rct.centerx:
                self.kkimg_rct.centerx-=1        
            #move_key = Bird.key_delta[key_states]
            #if Screen.bird_chake_bound(move_key):
            #print("AA")
            #self.kkimg_rct.centerx += move_key[0]
            #self.kkimg_rct.centery += move_key[1]
        self.blit(scr)
    
    def blit(self, scr: Screen):
        scr.suface_sfc.blit(self.kkimg_sfc, self.kkimg_rct)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.suface_rct.width)
        self.rct.centery = random.randint(0, scr.suface_rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.suface_sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.suface_rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        bkd.update(scr)
        if kkt.kkimg_rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
