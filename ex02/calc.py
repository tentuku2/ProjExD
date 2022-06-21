from io import TextIOBase
from operator import imod
from random  import randint
import tkinter as tk
from tkinter import RAISED, Button, Entry, ttk
from tkinter.tix import COLUMN

class Main_GUI(tk.Frame):
    def __init__(self,mastar):
        super(Main_GUI,self).__init__()
        self.m_frame = tk.Frame(self,width=500,height=800,padx=30,pady=10,relief=RAISED,bg="#ff00ff")
        self.m_frame.place(x=0,y=0)
        self.b_frame = tk.Frame(self,width=300,height=500,padx=1,pady=1,relief=RAISED,bg="#ff0000")
        self.b_frame.place(x=10,y=150)
        self.frame_widget()

    def frame_widget(self):
        self.textbox = Entry(self.m_frame,justify="right",font =("Times new roman",40),width=10)
        self.textbox.place(x=10,y=30)
        Button_list = ["%","CE","C","⇐×","1/x","x²","²√x","÷","7","8","9","×","4","5","6","-","1","2","3","+","+/-","0",".","="]
        for y in range(6):
            for  x in range(4):
                btn = Button(self.b_frame,text=Button_list[x+(y*4)],width=4,height=1,bg="#555555",fg="#000000",font=("Times new roman",30))
                btn.bind("<1>",self.num_button_click)
                btn.grid(column=x,row=y)
                #btn.place(x=x*95,y=y*120)

    def num_button_click(self,event):
        num_list = ["1","2","3","4","5","6","7","8","9","0","+","-","%","×","÷","x²"]
        #self.num = event.widget["text"]
        self.ans = self.textbox.get()
        befor_list = ["×","÷","x²"]
        after_list = ["*","/","**2"]
        if event.widget["text"] in num_list:
            self.textbox.insert(tk.END,event.widget["text"])
        elif event.widget["text"] == "C":
            self.textbox.delete(0,tk.END)
        elif event.widget["text"] == "⇐×":
            self.textbox.delete(len(self.ans)-1,tk.END)
        elif event.widget["text"] == ".":
            self.textbox.delete(0,tk.END)
            self.ans = float(self.ans)/10
            self.textbox.insert(tk.END,self.ans)
        elif event.widget["text"] == "=":
            self.textbox.delete(0,tk.END)
            for be,af in zip(befor_list,after_list):
                self.ans  = self.ans.replace(be,af)
            self.textbox.insert(tk.END,eval(self.ans))
        elif event.widget["text"] == "CE":
            self.gameing()
        elif event.widget["text"] == "1/x":
            self.frame_widget()


    def gameing(self):
        self.b_frame.place_forget()
        self.g_frame = tk.Frame(self,width=300,height=500,padx=1,pady=1,relief=RAISED,bg="#ff0000")
        self.b_frame.place(x=10,y=150)
        Button_list = ["%","CE","C","⇐×","1/x","x²","²√x","÷","7","8","9","×","4","5","6","-","1","2","3","+","+/-","0",".","="]
        
        for y in range(6):
            for  x in range(4):
                game = f"#{str(hex(randint(100,255)))[2:]}{hex(randint(100,255))[2:]}{hex(randint(100,255))[2:]}"
                btn = Button(self.b_frame,text=Button_list[x+(y*4)],width=4,height=1,bg=game,fg="#000000",font=("Times new roman",30))
                btn.bind("<1>",self.num_button_click)
                btn.grid(column=x,row=y)





def main():
    root = tk.Tk()
    root.geometry("500x800")
    view = Main_GUI(root)
    view.pack(expand=True,fill=tk.BOTH)
    root.mainloop()

main()