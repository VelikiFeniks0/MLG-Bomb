# MLG Bomb
# Made by VelikiFeniks XDDDDDDDD

# BTW I DO NOT OWN CONTENT FROM memes AND sounds FOLDERS


# Importing awesome stuff :O
from tkinter import font, PhotoImage, Tk, \
LEFT, TOP, Toplevel, Label, \
IntVar, Checkbutton, Button, Scale

from pygame import mixer, init
from time import sleep
from win32api import GetAsyncKeyState, GetCursorPos
from threading import Thread
from sys import exit as _exit
from _tkinter import TclError
from tkinter import messagebox as msgbox
from os import getcwd

# freaking setup 10/10!!!!
init()
mixer.init()


currentDir = getcwd()

root = Tk()
root.config(bg="#1c1c27")
root.geometry("860x516")
root.title("MLG Bomb")
root.resizable(False,False)

_font = font.Font(family="Comic Sans MS")

# logo
try:
    image = PhotoImage(file=f"{currentDir}\\memes\\mlg_bomb_logo.png")
    logo = Label(root, image=image, bg="#1c1c27")
    logo.pack(side=TOP)
except TclError:
    msgbox.showerror("What the heck", message="Where the heck did you put files XD")

hitmarker_var = IntVar(root,1)
hitmarker = Checkbutton(root, text="CoD hitmarker", font=_font, onvalue=1, offvalue=0, variable=hitmarker_var, bg="#3b3b4d", fg="#ff0000", activebackground="#3b3b4d", activeforeground="#ff0000").pack(side=LEFT)

# various MLG stuff
class Hitmarker:
    def __init__(self, master):
        global hitmarker_var
        self.master = master
        self.window = Toplevel(master)
        self.window.geometry("45x45")
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "#f0f0f0")
        self.window.wm_attributes("-topmost", True)

        self.image = PhotoImage(file=f"{currentDir}\\memes\\cod_hitmarker.png")
        self.label = Label(self.window, image=self.image)

    
    def move(self, event=None):
        self.window.geometry(f"+{event[0]-23}+{event[1]-25}")


    def effect(self):
        sound = mixer.Sound(f"{currentDir}\\audio\\hitmarker_2.mp3")
        sound.set_volume(0.1)
        sound.play(loops=0)
        self.label.pack()
        self.window.after(100,self.label.pack_forget)
        sleep(0.2)
        sound.stop()


    def get_click(self):
        global hitmarker_var
        while True:
            if hitmarker_var.get() == 1:
                self.move(GetCursorPos())
                if GetAsyncKeyState(1):
                    self.effect()
                    sleep(0.001)
            
    
    def update(self):
        Thread(target=self.get_click, daemon=True).start()


class Meme:
    def __init__(self, master, image, geometry, x,y):
        self.window = Toplevel(master)
        
        self.window.config(bg="#f0f0f0")
        self.window.resizable(False, False)
        self.window.geometry(f"+{str(geometry[0])}+{str(geometry[1])}")
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "#f0f0f0")

        self.x = x
        self.y = y

        try:
            self.image = PhotoImage(file=image)
            self.label = Label(self.window, image=self.image)
            self.label.pack()
        except TclError:
            msgbox.showerror("What the heck", message="Where the heck did you put files XD")

    def move(self, event=None):
        self.window.geometry(f"+{str(self.window.winfo_pointerx()-self.x)}+{str(self.window.winfo_pointery()-self.y)}")


    def update(self):
        self.label.pack()
        self.window.bind("<B1-Motion>", self.move)


class RainbowFrog:
    def __init__(self):
        global speedVar
        self.window = Toplevel(root)
        self.window.resizable(False,False)
        self.window.geometry("+200+200")
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "#f0f0f0")
        self.window.lift()

        self.frameCount = 10
        try:
            self.frames = [PhotoImage(
                file=f"{currentDir}\\memes\\rainbow_frog_meme.gif",
                format="gif -index %i" % (i)
            ) for i in range(self.frameCount)]

            self.label = Label(self.window, image="")
        except TclError:
            msgbox.showerror("What the heck", message="Where the heck did you put files XD")


    def move(self, event=None):
        self.window.geometry(f"+{self.window.winfo_pointerx()-50}+{self.window.winfo_pointery()-50}")
    
    def update_gif(self, ind=0):
        global speedVar
        frame = self.frames[ind]
        ind += 1
        
        if ind == self.frameCount:
            ind = 0
        
        self.label.configure(image=frame)
        self.window.after(((250-(speedVar.get()*50))), self.update_gif, ind)


    def update(self):
        self.label.pack()
        Thread(target=self.update_gif, daemon=True, name="Rainbow Frog").start()
        self.window.bind("<B1-Motion>", self.move) 

def MY_HOPE_WILL_NEVER_DIE():
    mixer.music.load(f"{currentDir}\\audio\\MLG_MY_HOPE_WILL_NEVER_DIE.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play(loops=0)


hitmarker = Hitmarker(root)

pepe = (f"{currentDir}\\memes\\pepe.png", (700,300),60,50)
glasses = (f"{currentDir}\\memes\\mlg_glasses.png", (800,300),45,5)
sanic = (f"{currentDir}\\memes\\sanic.png", (600,300),110,80)
doritos = (f"{currentDir}\\memes\\doritos.png", (600,300),50,60)
dew = (f"{currentDir}\\memes\\mtn_dew.png", (300,600),30,50)
doge = (f"{currentDir}\\memes\\doge.png", (500,400),60,70)


root.after(1,hitmarker.update)

rainbow_frog_button = Button(root, text="Rainbow Frog", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,RainbowFrog().update))).place(x=190,y=290)
pepe_button = Button(root,text="Pepe", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,Meme(root, pepe[0], pepe[1], pepe[2], pepe[3]).update))).place(x=493,y=290)
glasses_button = Button(root,text="MLG Glasses", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,Meme(root, glasses[0], glasses[1], glasses[2], glasses[3]).update))).place(x=265,y=340)
sanic_button = Button(root,text="Sanic", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,Meme(root, sanic[0], sanic[1], sanic[2], sanic[3]).update))).place(x=433,y=290)
doritos_button = Button(root,text="Doritos", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,Meme(root, doritos[0], doritos[1], doritos[2], doritos[3]).update))).place(x=190,y=340)
dew_button = Button(root,text="Mountain Dew", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,Meme(root, dew[0], dew[1], dew[2], dew[3]).update))).place(x=310,y=290)
doge_button = Button(root,text="Doge", font=_font, bg="#3b3b4d", fg="#00ff00", command=(lambda: root.after(1,Meme(root, doge[0], doge[1], doge[2], doge[3]).update))).place(x=378,y=340)
exit_button = Button(root, text="Exit", font=_font, bg="#ff0000", fg="#ffffff", command=lambda:_exit()).place(x=815, y=0)
myhopewillneverdie_button = Button(root, text="MY HOPE WILL NEVER DIE", font=_font, bg="#3b3b4d",fg="#ff00ff", command=MY_HOPE_WILL_NEVER_DIE).place(x=0, y=430)


Label(root,bg="#1c1c27", fg="#ff0000", text="Rainbow Frog Speed:", font=_font).place(x=510,y=380)

speedVar = IntVar(root,2)

speedSlider = Scale(
    root, 
    bg="#1c1c27", 
    font=_font, 
    fg="#ff00ff",
    activebackground="#ff0000", 
    variable=speedVar, 
    from_=4, to=1, 
    borderwidth=0, border=0, 
    highlightthickness=0, highlightbackground="#3b3b4d", highlightcolor="#3b3b4d"
).place(x=680,y=350)


# update it all m8
root.mainloop()