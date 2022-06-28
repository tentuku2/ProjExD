from asyncio import events
from cProfile import label
from distutils.file_util import move_file
from email.mime import image
import mailcap
import tkinter as tk
from tkinter import Button, ttk as ttk
import random
import tkinter.messagebox as tkm
import maze_maker as m_maker

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
        self.tori = tk.PhotoImage(file="fig/5.png")
        self.start = tk.PhotoImage(file="fig/S.png")
        self.gool = tk.PhotoImage(file="fig/G.png")
        self.cx = 1
        self.cy = 1
        self.mx = 1
        self.my = 1
        self.maze_lst = m_maker.make_maze(15,9)
        m_maker.show_maze(self.maze_canvas, self.maze_lst)
        #print(maze_lst)
        self.maze_canvas.create_rectangle(50,50,50,50,fill="#ff00ff")
        self.maze_canvas.create_image(150,150,image=self.start,tag="start")
        self.maze_canvas.create_image(1350,750,image=self.gool,tag="gool")

        self.maze_canvas.create_image(self.mx*100+50,self.my*100+50,image=self.tori,tag="tori")
        self.main_proc()

    def main_proc(self):
        self.after(100,self.main_proc)

    def count_up(self):
        self.tmr += 1
        self.label["text"] =  self.tmr
        self.after(1000,self.count_up)
    
    def key_down(self,event):
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
        if self.maze_lst[self.cy][self.cx] == 0:
            self.mx = self.cx
            self.my = self.cy
        else:
            self.cx = self.mx
            self.cy = self.my

        self.main_proc()

    def key_up(self,event):
        self.key = ""
        self.maze_canvas.coords("tori",self.mx*100+50,self.my*100+50)
        self.main_proc()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1500x900")
    view = Main_GUI(root)
    view.pack(expand=True,fill=tk.BOTH)
    root.mainloop()