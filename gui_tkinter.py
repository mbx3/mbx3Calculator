import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk,THEMES
from functools import partial
from Calculator import calculations


BUTTONS_TEXT=[['(',')','C','<--'],
              ['N','^','√','+'],
              ['1','2','3','-'],
              ['4','5','6','×'],
              ['7','8','9','÷'],
              ['Setting','0','.','=']]

def add_text(event):
    if type(event) == str: 
        calculationsText.set(calculationsText.get()+event)
    elif event.char in '1234567890-+*/$^':
        if event.char == '*': char = '×'
        elif event.char == '/': char = '÷'
        elif event.char == '$': char = '√'
        else: char = event.char
        calculationsText.set(calculationsText.get()+char)
    

def delete_char(event=None):
    calculationsText.set(calculationsText.get()[:-1])

def clear_text():
    calculationsText.set('')

def change_frame(frame:ttk.Frame):
    frame.tkraise()

def calculate():
    try:
        calculationsText.set(calculations.calculate(calculationsText.get()))
    except ValueError:
        calculationsText.set("Error!")

def change_theme(theme):
    root.config(theme=theme)
    root.minsize(300, 500)
    root.maxsize(400, 700)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=5)
    for row in range(1,7):
        mainFrame.rowconfigure(row, weight=1)
    for column in range(4):
        mainFrame.columnconfigure(column, weight=1)

root = ThemedTk(theme='adapta')
root.configure(width=300,height=500)
root.minsize(300, 500)
root.maxsize(400, 700)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
style = ttk.Style()


themesFrame = ttk.Frame(root)
themesFrame.grid(row=0,column=0,sticky=tk.NSEW)
themesFrame.grid_columnconfigure((0,1,2,3),weight=1)
themesFrame.grid_rowconfigure((0,1),weight=1)
ttk.Label(themesFrame,text='Theme : ').grid(row=0,column=0,padx=10,pady=5,sticky='nwe')
theme = tk.StringVar()
ttk.OptionMenu(themesFrame,theme,'adapta',*THEMES,command=lambda x: change_theme(x)).grid(row=0,column=1,padx=10,pady=5,columnspan=3,sticky='nwe')
ttk.Button(themesFrame,text='OK',command=lambda : change_frame(mainFrame)). grid(row=1,column=1,pady=5,columnspan=2,sticky='swe')





mainFrame = ttk.Frame(root)
mainFrame.grid(row=0,column=0,sticky=tk.NSEW)

mainFrame.rowconfigure(0, weight=5)
for row in range(1,7):
    mainFrame.rowconfigure(row, weight=1)
for column in range(4):
    mainFrame.columnconfigure(column, weight=1)



calculationsText = tk.StringVar()
label = ttk.Label(mainFrame,textvariable=calculationsText)
label.grid(column=0,row=0,padx=2,pady=5,columnspan=4,sticky=tk.NSEW)
for i in range(4):
    for j in range(1,7):
        txt = BUTTONS_TEXT[j-1][i]
        if txt == 'Setting' : btn_func = partial(change_frame,themesFrame)
        elif txt == 'C' : btn_func = clear_text
        elif txt == '<--': btn_func = delete_char
        elif txt == '=': btn_func = calculate
        else: btn_func = partial(add_text,txt)
        btn = ttk.Button(mainFrame,text=txt,command=btn_func)
        btn.grid(column=i,row=j,padx=2,pady=2,sticky=tk.NSEW)





root.bind('<Key>',add_text)
root.bind('<BackSpace>',delete_char)

label.bind('<Configure>', lambda x: label.config(wraplength=label.winfo_width()))

root.mainloop()