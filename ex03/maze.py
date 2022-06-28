from asyncio import events
from cProfile import label
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
        self.maze_canvas = tk.Canvas(self,width=1500,height=900,bg =("#000000"))
        self.maze_canvas.pack()
        self.tmr = 0
        self.bind_all("<KeyPress>",self.key_down)
        self.bind_all("<KeyRelease>",self.key_up)
        self.tori = tk.PhotoImage(file="fig/5.png")
        self.cx = 300 + 50
        self.cy = 400 + 50
        maze_lst = m_maker.make_maze(15,9)
        m_maker.show_maze(self.maze_canvas, maze_lst)
        self.maze_canvas.create_image(self.cx,self.cy,image=self.tori,tag="tori")
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
            self.cy-=100
        elif self.key == "Down":
            self.cy+=100
        elif self.key == "Left":
            self.cx -= 100
        elif self.key == "Right":
            self.cx += 100
        else:
            pass

        print(self.cx,self.cy)
        self.main_proc()

    def key_up(self,event):
        self.key = ""
        print(self.cx,self.cy)
        self.maze_canvas.coords("tori",self.cx,self.cy)
        self.main_proc()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    view = Main_GUI(root)
    view.pack(expand=True,fill=tk.BOTH)
    root.mainloop()