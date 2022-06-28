from asyncio import events
from cProfile import label
from email.mime import image
import tkinter as tk
from tkinter import Button, ttk as ttk
import random
import tkinter.messagebox as tkm

class Main_GUI(tk.Frame):
    def __init__(self,master):
        super(Main_GUI,self).__init__()
        self.maze_canvas = tk.Canvas(self,width=1500,height=900,bg =("#000000"))
        self.maze_canvas.pack()
        self.tmr = 0
        self.bind_all("<KeyPress>",self.key_down)
        self.bind_all("<KeyRelease>",self.key_up)
        self.tori = tk.PhotoImage(file="fig/5.png")
        self.cx = 300
        self.cy = 400
        self.maze_canvas.create_image(self.cx,self.cy,image=self.tori,tag="tori")

    
    def count_up(self):
        self.tmr += 1
        self.label["text"] =  self.tmr
        self.after(1000,self.count_up)
    
    def key_down(self,event):
        self.key = event.keysym
 
    def key_up(self):
        self.key = ""




if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    view = Main_GUI(root)
    view.pack(expand=True,fill=tk.BOTH)
    root.mainloop()