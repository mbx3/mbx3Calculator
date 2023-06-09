import tkinter as tk
from tkinter import ttk
from functools import partial
from CalculatorMain import calculations,string_work
from PIL import Image,ImageTk
import webbrowser
class GUI:
    BUTTONS_TEXT=[['(',')','C','⟵'],
                ['mod','^','√','+'],
                ['1','2','3','-'],
                ['4','5','6','×'],
                ['7','8','9','÷'],
                ['Setting','0','.','=']]
    
    COLOR_PALETTES = {
        'Light' : ['#FAEDCD','#FEFAE0','#E9EDC9','#A7727D'],
        'Dark' : ['#18122B','#393053','#443C68','#635985'],
        'Blue' : ['#62CDFF','#97DEFF','#C9EEFF','#AA77FF'],
        'Red' : ['#AF0404','#FF0032','#FF0000','#252525'],
        'Green' : ['#14C38E','#B8F1B0','#00FFAB','#E3FCBF'],
        'Yellow' : ['#E7B10A','#F7F1E5','#898121','#4C4B16'],
        'Jigili' : ['#F94A29','#D61355','#30E3DF','#FCE22A'],
        'Gold' : ['#FFCE45','#D4AC2B','#B05E27','#7E370C'],
        'Coffee' : ['#594545','#815B5B','#9E7676','#FFF8EA'],
        'Warm' : ['#630606','#890F0D','#E83A14','#D9CE3F'],
        'Cold' : ['#0E8388','#9E4784','#66347F','#37306B'],
    }

    SOCIAL_NETWORKS = {
        'Email'     :   {
                        'username'  : 'mbx3.bzr3@gmail.com',
                        'link'      : '',
                        'path'      : r'pics/Email.png'
                        },
        'GitHub'    :   {
                        'username'  : 'mbx3',
                        'link' : r'https://github.com/mbx3',
                        'path' : r'pics/GitHub.png'
                        },
        'LinkedIn'  :   {
                        'username'  : 'Mohammad Bazrafshan',
                        'link' : r'https://www.linkedin.com/in/mohammad--bazrafshan/',
                        'path' : r'pics/LinkedIn.png'
                        },
        'Telegram'  :   {
                        'username'  : 'MBX_3',
                        'link' : r'https://t.me/MBX_3',
                        'path' : r'pics/Telegram.png'
                        },
    }

    def __init__(self):
        # Create and configure Root
        self.root = tk.Tk()
        self.root.configure(width=300,height=500)
        self.root.minsize(300, 500)
        self.root.maxsize(400, 700)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.change_theme('Dark')

        # Create and configure Themes Frame
        self.themesFrame = ttk.Frame(self.root)
        self.themesFrame.grid(row=0,column=0,sticky=tk.NSEW)
        self.themesFrame.grid_columnconfigure((0,1,2,3),weight=1)
        self.themesFrame.grid_rowconfigure((0,1,2,3,5,6,7,8),weight=1)
        self.themesFrame.grid_rowconfigure((4,9),weight=2)
        theme = tk.StringVar(value='Dark')
        ttk.Label(self.themesFrame,text='Theme : ').grid(row=0,column=0,padx=10,pady=5,sticky='nwe')
        for i,cp in enumerate(GUI.COLOR_PALETTES):
            colors = GUI.COLOR_PALETTES[cp]
            styleClass = cp+'.TRadiobutton'
            self.style.configure(styleClass,background=colors[1],foreground=colors[3],indicatorcolor=colors[1])
            self.style.map(styleClass,
                    background=[('pressed', colors[2]),
                                ('active', colors[1]),
                                ('hover', colors[2]),
                                ('selected', colors[0])],
                    indicatorcolor=[('selected', colors[1]),
                                    ('hover',colors[2])])
            ttk.Radiobutton(self.themesFrame,style=styleClass,text=cp,variable=theme,value=cp,command=lambda x=cp: self.change_theme(x)).grid(row=(i+1)//4,column=(i+1)%4,padx=10,pady=5,sticky='nwe')
        ttk.Separator(self.themesFrame). grid(row=3,column=0,pady=5,columnspan=4,sticky='nwe')
        ttk.Label(self.themesFrame,text="Creator : Mohammad Bazrafshan").grid(row=4,column=0,padx=10,pady=5,columnspan=4,sticky='nw')
        photos=[]
        for i,sn in enumerate(GUI.SOCIAL_NETWORKS):
            username = GUI.SOCIAL_NETWORKS[sn]['username']
            link = GUI.SOCIAL_NETWORKS[sn]['link']
            imagePath = GUI.SOCIAL_NETWORKS[sn]['path']
            img = Image.open(imagePath).resize((20,20))
            photo = ImageTk.PhotoImage(img)
            photos.append(photo)
            txt = sn + ' : ' + username
            label = ttk.Label(self.themesFrame,text=txt,image=photo,compound="left")
            label.grid(row=5+i,column=0,sticky='w',columnspan=4,padx=10)
            if link:
                label.bind('<Button-1>',lambda x,link=link: self.callback(link))
                label.config(cursor="hand2")
        ttk.Button(self.themesFrame,text='OK',command=lambda : self.change_frame(self.mainFrame)). grid(row=9,column=1,pady=5,columnspan=2,sticky='swe')


        # Create and configure Main Frame
        self.mainFrame = ttk.Frame(self.root)
        self.mainFrame.grid(row=0,column=0,sticky=tk.NSEW)
        self.mainFrame.rowconfigure(0, weight=5)
        self.mainFrame.rowconfigure(list(range(1,7)), weight=1)
        self.mainFrame.columnconfigure(list(range(4)), weight=1)
        self.calculationsText = tk.StringVar(value="0")
        self.label = ttk.Label(self.mainFrame,textvariable=self.calculationsText)
        self.label.grid(column=0,row=0,padx=2,pady=5,columnspan=4,sticky=tk.NSEW)
        for i in range(4):
            for j in range(1,7):
                txt = GUI.BUTTONS_TEXT[j-1][i]
                if txt == 'Setting' : btn_func = partial(self.change_frame,self.themesFrame)
                elif txt == 'C' : btn_func = self.clear_text
                elif txt == '⟵': btn_func = self.delete_char
                elif txt == '=': btn_func = self.calculate
                else: btn_func = lambda x=txt: self.add_text(x)
                btn = ttk.Button(self.mainFrame,text=txt,command=btn_func)
                btn.grid(column=i,row=j,padx=2,pady=2,sticky=tk.NSEW)




        # Bind functions to widgets
        self.root.bind('<Key>',self.add_text)
        self.root.bind('<BackSpace>',self.delete_char)
        self.label.bind('<Configure>', lambda x: self.label.config(wraplength=self.label.winfo_width()))

        # Start GUI main loop
        self.root.mainloop()    

    def add_text(self,event):
        newtxt = ""
        if type(event) == str:
            newtxt=event
        elif event.char in '1234567890-+*/$^m.()':
            newtxt=event.char
        if newtxt:
            self.calculationsText.set(string_work.correction(self.calculationsText.get(),newtxt))    

    def delete_char(self,event=None):
        if self.calculationsText.get() == "Error!" : self.clear_text()
        elif self.calculationsText.get()[-3:] == "mod": self.calculationsText.set(self.calculationsText.get()[:-3])
        else: self.calculationsText.set(string_work.correction(self.calculationsText.get()[:-1]))

    def clear_text(self):
        self.calculationsText.set('0')

    def change_frame(self,frame:ttk.Frame):
        frame.tkraise()

    def calculate(self):
        try:
            self.calculationsText.set(calculations.calculate(self.calculationsText.get()))
        except ValueError:
            self.calculationsText.set("Error!")

    def change_theme(self,color_palette):
        color_palette = GUI.COLOR_PALETTES[color_palette]
        self.style.configure('TFrame',background=color_palette[0])
        self.style.configure('TLabel',background=color_palette[0],foreground=color_palette[3],font=('arial',11))
        self.style.configure('TSeparator',background=color_palette[3])
        self.style.configure('TButton',activebackground=color_palette[0],background=color_palette[0],foreground=color_palette[3],focuscolor=color_palette[0],font=('arial',11))
        self.style.map('TButton',
                background=[('pressed', color_palette[2]),
                            ('active', color_palette[1]),
                            ('hover', color_palette[2]),
                            ('selected', color_palette[0])])

    def callback(self,url):
        webbrowser.open_new(url)

GUI()    

