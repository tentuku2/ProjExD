#from importlib.util import set_loader
#from turtle import Screen, pos
from pickle import TRUE
from re import T
from sre_constants import SUCCESS
from winreg import DisableReflectionKey
import pygame as pg
import sys
import random

class Display:
    def __init__(self, title, wh, col):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.Surface((1600,900))
        self.bgi_sfc.fill(col)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Ganban:
    def __init__(self):
        self.gx_size = 250
        self.gy_size = 200
        self.dig_count = 0
        self.dig_impct = 8
        self.kiban_size = pg.Rect(20,20,1000,800)
        self.color_list = [[255,255,255],[220,105,30],[160,82,45],[139,69,19]]
        self.rock = [[random.randint(1,3) for i in range(self.gx_size)] for j in range(self.gy_size)]
        self.kiban_sfc = pg.Surface((self.gx_size*4,self.gy_size*4))
        self.kiban_sfc.set_colorkey([255,255,255])
        self.kiban_sfc.set_alpha(255)
        self.kiban_rct = self.kiban_sfc.get_rect()
        self.dig_size = 45
        for y in range(self.gy_size):
            for x in range(self.gx_size):
                g_c = self.rock[y][x]
                pg.draw.rect(self.kiban_sfc,(self.color_list[g_c][0],self.color_list[g_c][1],self.color_list[g_c][2]),(((4*x)),(4*y),4,4))
        

    def dig(self):
        x,y = pg.mouse.get_pos()
        self.pos_x = x//4
        self.pos_y = y//4
        self.dig_count += self.dig_impct
        self.dig_list = []
        self.big_list_x = [[i for i in range(-1*(2+(self.dig_size//4-abs(j-self.dig_size//2))),5+(self.dig_size//4-abs(j-self.dig_size//2)))] for j in range(self.dig_size)]
        self.big_list_y = [i for i in range(-1*(self.dig_size//2),(self.dig_size//2)+5)]
        for y in range(len(self.big_list_x)):
            for x in range(len(self.big_list_x[y])):
                self.big_list_x[y][x] += self.pos_x

        for y in range(len(self.big_list_x)):
            p_y = self.big_list_y[y]
            for x in range(len(self.big_list_x[y])):
                p_x = self.big_list_x[y][x]
                try:
                    self.rock[self.pos_y + p_y][p_x] -= 1
                    g_c = self.rock[self.pos_y + p_y][p_x]
                    if g_c < 0 :
                        g_c = 0
                    pg.draw.rect(self.kiban_sfc,(self.color_list[g_c][0],self.color_list[g_c][1],self.color_list[g_c][2]),(((4*p_x)),(4*(self.pos_y + p_y)),4,4))
                except IndexError:
                    print("out of Index")

    def size_chang(self,size):
        if size == "big":
            self.dig_size = 45
            self.dig_impct = 8

        elif size == "small":
            self.dig_size = 15
            self.dig_impct = 2

    def bilt(self,dis:Display):
        dis.sfc.blit(self.kiban_sfc,(20,20,1000,800),self.kiban_rct)


class Object:
    def __init__(self,dis:Display):
        self.big_btn = pg.Rect(1100,50,200,100)
        self.sml_btn = pg.Rect(1350,50,200,100)
        self.scan_btn = pg.Rect(1100,750,200,100)
        self.mode1_scr = pg.Rect(1350,200,200,200)
        self.mode2_scr = pg.Rect(1370,220,160,160)

        pg.draw.rect(dis.bgi_sfc,(255,0,0),self.big_btn)
        pg.draw.rect(dis.bgi_sfc,(0,255,0),self.sml_btn)
        pg.draw.rect(dis.bgi_sfc,(255,255,0),self.scan_btn)
        self.HPbar_sfc = pg.Surface((1000,50))
        self.HPbar_rct = self.HPbar_sfc.get_rect()
        for i in range(500):
            pg.draw.rect(self.HPbar_sfc,(255,0,0),(i*2,0,2,50))

    def HP_chang(self,gbn:Ganban):
        for i in range(500,500-gbn.dig_count,-1):
            pg.draw.rect(self.HPbar_sfc,(0,0,255),(i*2,0,2,50))

    def yakitori(self,image,size,pos,gbn:Ganban):
        self.yakitori_img_sfc = pg.image.load(image)
        self.yakitori_img_sfc = pg.transform.rotozoom(self.yakitori_img_sfc,0,size)
        tori_x,tori_y = self.yakitori_img_sfc.get_width()//4,self.yakitori_img_sfc.get_width()//4
        self.yakitori_img_rct = self.yakitori_img_sfc.get_rect()
        self.yakitori_img_rct.center = pos
        self.yakitori_body_x = [i for i in range(pos[0]//4-(tori_x//2)//4,pos[0]//4+(tori_x//2)//4)]
        self.yakitori_body_y = [i for i in range(pos[1]//4-(tori_y//2)//4,pos[1]//4+(tori_y//2)//4)]
        self.yakitori_body = 0
        self.yakitori_body_lis = []
        for y in self.yakitori_body_y:
            for x in self.yakitori_body_x:
                self.yakitori_body_lis.append((y,x))
                self.yakitori_body += gbn.rock[y][x]

    def haikei(self,image,size):
        self.haikei_img_sfc = pg.image.load(image)
        self.haikei_img_sfc = pg.transform.scale(self.haikei_img_sfc,size)
        self.haikei_img_rct = self.haikei_img_sfc.get_rect()

    def doriru(self,image,size,pos):
        self.doriru_img_sfc = pg.image.load(image)
        self.doriru_img_sfc = pg.transform.rotozoom(self.doriru_img_sfc,0,size)
        self.doriru_img_rct = self.doriru_img_sfc.get_rect()
        self.doriru_img_rct.center = pos

    def hanma(self,image,size,pos):
        self.hanma_img_sfc = pg.image.load(image)
        self.hanma_img_sfc = pg.transform.rotozoom(self.hanma_img_sfc,0,size)
        self.hanma_img_rct = self.hanma_img_sfc.get_rect()
        self.hanma_img_rct.center = pos
    
    def hanma_bilt(self,pos,dis:Display):
        pg.draw.rect(dis.bgi_sfc,(0,0,0),self.mode1_scr)
        pg.draw.rect(dis.bgi_sfc,(230,230,230),self.mode2_scr)
        dis.sfc.blit(self.hanma_img_sfc,(pos),self.hanma_img_rct)


    def bilt(self,dis:Display):
        dis.sfc.blit(dis.bgi_sfc, dis.bgi_rct)
        dis.sfc.blit(self.haikei_img_sfc,self.haikei_img_rct)
        dis.sfc.blit(self.HPbar_sfc,(20,840,1000,50),self.HPbar_rct)
        dis.sfc.blit(self.yakitori_img_sfc,self.yakitori_img_rct)
        dis.sfc.blit(self.doriru_img_sfc,self.doriru_img_rct)
        dis.sfc.blit(self.hanma_img_sfc,self.hanma_img_rct)



class Start:
    def __init__(self,image,dis:Display):
        self.start_img_sfc = pg.image.load(image)
        self.start_img_sfc = pg.transform.scale(self.start_img_sfc,(1600,900))
        self.start_img_rct = self.start_img_sfc.get_rect()
        while True:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    return
            dis.sfc.blit(self.start_img_sfc,self.start_img_rct)
            pg.display.update()

class Finish:
    def __init__(self):
        pass

    def dig_succes(self,obj:Object,gbn:Ganban):
        succses = 0
        for i in obj.yakitori_body_lis:
            count = gbn.rock[i[0]][i[1]]
            if count < 0:
                count = 0
            succses += count
        if succses == 0:
            return True

    def game_clear(self,image,size):
        self.clear_img_sfc = pg.image.load(image)
        self.clear_img_sfc = pg.transform.scale(self.clear_img_sfc,size)
        self.clear_img_rct = self.over_img_sfc.get_rect()

    def game_over(self,image,size):
        self.over_img_sfc = pg.image.load(image)
        self.over_img_sfc = pg.transform.scale(self.over_img_sfc,size)
        self.over_img_rct = self.over_img_sfc.get_rect()

    def succes_bilt(self,dis:Display):
        dis.sfc.blit(self.clear_img_sfc,self.clear_img_rct)

    def end_bilt(self,dis:Display):
        dis.sfc.blit(self.over_img_sfc,self.over_img_rct)

def main():
    clock = pg.time.Clock()
    dis = Display("甦れコウカトン", (1600, 900), (192,192,192))
    gbn = Ganban()
    obj = Object(dis)
    fin = Finish()
    scan_flag  = 0
    clear_flag = False
    ture = "big"
    obj.yakitori("../fig/6.png", 2.0,(random.randint(85,gbn.kiban_sfc.get_width()-50), random.randint(85,gbn.kiban_sfc.get_height()-50)),gbn)
    obj.haikei("../fig/ganban.png",(1040,840))
    obj.doriru("../fig/doriruu.png", 0.4,(1450,90))
    obj.hanma("../fig/hanmaa.png", 0.3,(1200,95))
    fin.game_over("../fig/gameover.png",(1600,900))
    fin.game_clear("../fig/gameclear.png",(1600,900))
    Start("../fig/start.png",dis)
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            if event.type == pg.MOUSEBUTTONDOWN:
                if obj.big_btn.collidepoint(event.pos):
                    print("red button was pressed")
                    gbn.size_chang("big")
                    ture = "big"

                if obj.sml_btn.collidepoint(event.pos):
                    print("green button was pressed")
                    gbn.size_chang("small")
 
                if obj.scan_btn.collidepoint(event.pos):
                    print("scan button was pressed")
                    gbn.kiban_sfc.set_alpha(100)
                    scan_flag = 1

                if gbn.kiban_size.collidepoint(event.pos):
                    gbn.dig()
                    obj.HP_chang(gbn)
                    clear_flag = fin.dig_succes(obj,gbn)

        dis.blit()
        obj.bilt(dis)
        gbn.bilt(dis)
        
        if ture == "big":
            obj.hanma_bilt((1370,220,160,160),dis)

        if gbn.dig_count >=500:
            fin.end_bilt(dis)
        
        if clear_flag == True:
            fin.succes_bilt(dis)

        pg.display.update()
        if scan_flag == 1:
            pg.time.delay(1000)
            gbn.kiban_sfc.set_alpha(255)
            scan_flag = 0

        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
