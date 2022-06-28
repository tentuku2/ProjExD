import tkinter as tk
from tkinter import Button, ttk as ttk
import tkinter.messagebox as tkm
import maze_maker as m_maker
import datetime

class Main_GUI(tk.Frame):
    def __init__(self,master):
        super(Main_GUI,self).__init__()
        #カンバス
        self.maze_canvas = tk.Canvas(self,width=1500,height=900,bg =("#000000"))
        self.maze_canvas.pack()
        #キーアクションたち
        self.bind_all("<KeyPress>",self.key_down)
        self.bind_all("<KeyRelease>",self.key_up)
        #使う画像ども
        self.tori = tk.PhotoImage(file="ex03/fig/5.png")
        self.start = tk.PhotoImage(file="ex03/fig/S.png")
        self.gool = tk.PhotoImage(file="ex03/fig/G.png")
        #比較用座標
        self.cx = 1
        self.cy = 1
        #鳥座標
        self.mx = 1
        self.my = 1
        #gole座標
        self.gx = 13
        self.gy = 7
        self.maze_fill()
        self.main_proc()

    def main_proc(self): #メインループ関数
        self.after(100,self.main_proc)
    
    def maze_fill(self): #描画関数
        #外部関数呼び出し
        self.maze_lst = m_maker.make_maze(15,9)
        m_maker.show_maze(self.maze_canvas, self.maze_lst)
        #描画
        self.maze_canvas.create_image(150,150,image=self.start,tag="start")
        self.maze_canvas.create_image(self.gx*100+50,self.gy*100+50,image=self.gool,tag="gool")
        self.maze_canvas.create_image(self.mx*100+50,self.my*100+50,image=self.tori,tag="tori")
        #時間計測開始
        self.st = datetime.datetime.now()

    def key_down(self,event):#キー入力字関数
        #関数イベント変数
        self.key = event.keysym
        if self.key ==  "Up":
            self.cy -= 1
        elif self.key == "Down":
            self.cy += 1
        elif self.key == "Left":
            self.cx -= 1
        elif self.key == "Right":
            self.cx += 1
        else:
            pass
        #壁があるかの判定
        if self.maze_lst[self.cy][self.cx] == 0:
            self.mx = self.cx
            self.my = self.cy
        else:
            self.cx = self.mx
            self.cy = self.my

        self.main_proc()

    def key_up(self,event):#キー入力終了字関数
        self.key = ""
        #ゴールについたかの判断
        if self.gx == self.mx  and  self.gy == self.my:
            self.mx,self.my,self.cx,self.cy = 1,1,1,1
            #こうかとんの削除
            self.maze_canvas.delete("tori")
            #メッセージボックスの表示
            self.messeg()
            #描画関数の表示
            self.maze_fill()
        self.maze_canvas.coords("tori",self.mx*100+50,self.my*100+50)
        self.main_proc()

    def messeg(self): #メッセージボックス関数
        #終了時間獲得
        self.et = datetime.datetime.now()
        #メッセージボックス
        ret = tkm.askyesno('ナイストライ！', f'クリアタイムは{(self.et-self.st).seconds}秒だったドン！\nもう一回遊ぶドン？')
        if ret == False:
            self.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    view = Main_GUI(root)
    view.pack(expand=True,fill=tk.BOTH)
    root.mainloop()