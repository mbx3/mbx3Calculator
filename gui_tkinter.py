import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk,THEMES
from functools import partial
from Calculator import calculations

class GUI:
    BUTTONS_TEXT=[['(',')','C','<--'],
                ['N','^','√','+'],
                ['1','2','3','-'],
                ['4','5','6','×'],
                ['7','8','9','÷'],
                ['Setting','0','.','=']]

    def __init__(self):
        # Create and configure Root
        self.root = ThemedTk(theme='adapta')
        self.root.configure(width=300,height=500)
        self.root.minsize(300, 500)
        self.root.maxsize(400, 700)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        style = ttk.Style()


        self.themesFrame = ttk.Frame(self.root)
        self.themesFrame.grid(row=0,column=0,sticky=tk.NSEW)
        self.themesFrame.grid_columnconfigure((0,1,2,3),weight=1)
        self.themesFrame.grid_rowconfigure((0,1),weight=1)
        ttk.Label(self.themesFrame,text='Theme : ').grid(row=0,column=0,padx=10,pady=5,sticky='nwe')
        theme = tk.StringVar()
        ttk.OptionMenu(self.themesFrame,theme,'adapta',*THEMES,command=lambda x: self.change_theme(x)).grid(row=0,column=1,padx=10,pady=5,columnspan=3,sticky='nwe')
        ttk.Button(self.themesFrame,text='OK',command=lambda : self.change_frame(self.mainFrame)). grid(row=1,column=1,pady=5,columnspan=2,sticky='swe')



        self.mainFrame = ttk.Frame(self.root)
        self.mainFrame.grid(row=0,column=0,sticky=tk.NSEW)

        self.mainFrame.rowconfigure(0, weight=5)
        for row in range(1,7):
            self.mainFrame.rowconfigure(row, weight=1)
        for column in range(4):
            self.mainFrame.columnconfigure(column, weight=1)



        self.calculationsText = tk.StringVar()
        self.label = ttk.Label(self.mainFrame,textvariable=self.calculationsText)
        self.label.grid(column=0,row=0,padx=2,pady=5,columnspan=4,sticky=tk.NSEW)
        for i in range(4):
            for j in range(1,7):
                txt = GUI.BUTTONS_TEXT[j-1][i]
                if txt == 'Setting' : btn_func = partial(self.change_frame,self.themesFrame)
                elif txt == 'C' : btn_func = self.clear_text
                elif txt == '<--': btn_func = self.delete_char
                elif txt == '=': btn_func = self.calculate
                else: btn_func = partial(self.add_text,txt)
                btn = ttk.Button(self.mainFrame,text=txt,command=btn_func)
                btn.grid(column=i,row=j,padx=2,pady=2,sticky=tk.NSEW)





        self.root.bind('<Key>',self.add_text)
        self.root.bind('<BackSpace>',self.delete_char)

        self.label.bind('<Configure>', lambda x: self.label.config(wraplength=self.label.winfo_width()))


        self.root.mainloop()    

    def add_text(self,event):
        if type(event) == str: 
            self.calculationsText.set(self.calculationsText.get()+event)
        elif event.char in '1234567890-+*/$^':
            if event.char == '*': char = '×'
            elif event.char == '/': char = '÷'
            elif event.char == '$': char = '√'
            else: char = event.char
            self.calculationsText.set(self.calculationsText.get()+char)
        

    def delete_char(self,event=None):
        self.calculationsText.set(self.calculationsText.get()[:-1])

    def clear_text(self):
        self.calculationsText.set('')

    def change_frame(self,frame:ttk.Frame):
        frame.tkraise()

    def calculate(self):
        try:
            self.calculationsText.set(calculations.calculate(self.calculationsText.get()))
        except ValueError:
            self.calculationsText.set("Error!")

    def change_theme(self,theme):
        self.root.config(theme=theme)
        self.root.minsize(300, 500)
        self.root.maxsize(400, 700)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=5)
        for row in range(1,7):
            self.mainFrame.rowconfigure(row, weight=1)
        for column in range(4):
            self.mainFrame.columnconfigure(column, weight=1)

GUI()    

