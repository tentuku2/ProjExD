from doctest import FAIL_FAST
import datetime
from linecache import checkcache
import tkinter
from pygame.locals import *
import random
import pygame as pg
import sys
import tkinter.messagebox as tkm

class game:

    def __init__(self):
        pg.display.set_caption("逃げろコウカトン！")
        #self.clock = pg.time.Clock()
        self.screen_sfc = pg.display.set_mode((1600,900))
        self.screen_rct = self.screen_sfc.get_rect()
        self.bg  = pg.image.load("pg_bg.jpg")
        self.bg_rect = self.bg.get_rect()
        self.flag = 0
        self.setup()

    def setup(self):
        self.kkimg_sfc = pg.image.load("fig/6.png")
        self.kkimg_sfc = pg.transform.rotozoom(self.kkimg_sfc,0,2.0)
        self.kkimg_rct = self.kkimg_sfc.get_rect()
        self.kkimg_rct.center = 900,400
        if self.flag == 0:
            self.bom_sfc = pg.Surface((100,100))
            self.bom_sfc.set_colorkey((0,0,0))
            pg.draw.circle(self.bom_sfc, (255,0,0), (50,50),10)
        elif self.flag ==1:
            self.bom_sfc = pg.image.load("fig/fire.png")
            self.bom_sfc = pg.transform.rotozoom(self.bom_sfc,0,0.1)
        self.bom_rect = self.bom_sfc.get_rect()
        self.bom_rect.centerx = random.randint(0,self.screen_rct.width)
        self.bom_rect.centery = random.randint(0,self.screen_rct.height)
        self.vx,self.vy = 1,1
        self.main()
        #self.clock.tick(0.2)

    def main(self):
        while True:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.key_states = pg.key.get_pressed()

            if self.key_states[pg.K_c] == True:
                print("assss")
                self.cook()
            if self.key_states[pg.K_UP] == True:
                if 0 < self.kkimg_rct.centery :
                    self.kkimg_rct.centery -= 1
            if self.key_states[pg.K_DOWN]==True:
                 if self.screen_rct.height > self.kkimg_rct.centery :
                    self.kkimg_rct.centery += 1
            if self.key_states[pg.K_RIGHT]==True:
                if self.screen_rct.width > self.kkimg_rct.centerx:
                    self.kkimg_rct.centerx+=1
            if self.key_states[pg.K_LEFT]==True:
                if 0 < self.kkimg_rct.centerx:
                    self.kkimg_rct.centerx-=1
            if 0 > self.bom_rect.centerx or self.bom_rect.centerx>self.screen_rct.width:
                self.vx *= -1
            if 0>self.bom_rect.centery or self.bom_rect.centery >self.screen_rct.height:
                self.vy *= -1
            if  self.kkimg_rct.colliderect(self.bom_rect):
                if self.flag == 1:
                    self.yakitori()
                else:
                    self.end()
            self.bom_rect.move_ip(self.vx,self.vy)
        
            self.screen_sfc.blit(self.bg,self.bg_rect)
            self.screen_sfc.blit(self.bom_sfc,self.bom_rect)
            self.screen_sfc.blit(self.kkimg_sfc,self.kkimg_rct)
            pg.display.update(self.bg_rect)

    def cook(self):
        self.flag = 1
        self.setup()

    def yakitori(self):
        self.kkimg_sfc = pg.image.load("fig/koukaton_future.png")
        self.kkimg_sfc = pg.transform.rotozoom(self.kkimg_sfc,0,2.0)
        self.kkimg_rct = self.kkimg_sfc.get_rect()
        self.screen_sfc.blit(self.kkimg_sfc,self.kkimg_rct)
        a = self.alarm()
        pg.display.update(self.bg_rect)
        ret = tkm.askyesno('ナイストライ！', "こんがり焼けました!\nもう一度遊びますか？")
        if ret == False:
            sys.exit()
        else:
            self.flag = 0
            self.setup()
    
    def alarm(self):
        pg.mixer.init(frequency = 44100)    # 初期設定
        pg.mixer.music.load("fig/sample.wav")     # 音楽ファイルの読み込み
        pg.mixer.music.play(1)              # 音楽の再生回数(1回)
        t = datetime.datetime.now()
        while(1):
            t2 = datetime.datetime.now()
            if(t2-t).seconds == 3:
                return 0
    
        pg.mixer.music.stop()               # 再生の終了
        return 0

    def end(self):
        sys.exit()

if __name__ == "__main__":
    pg.init()
    game()
    pg.quit()
    sys.exit()
