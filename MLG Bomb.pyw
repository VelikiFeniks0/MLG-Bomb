# MLG Bomb
# 6.24.2023.
# A project made just for fun



# imports
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time, win32api, win32con, threading, pygame, os, sys, random
from tkinter import ttk
from tkinter import font

current_dir = __file__[0:-13]

# Main class
class Main:
    def __init__(self):
        pygame.mixer.init()

        # setup
        root = tk.Tk()
        root.config(bg='#1c1c27')
        root.geometry('860x516')
        root.title('MLG Bomb')
        root.resizable(False, False)
        self.font = font.Font(family="Calibri")


        self.hitmarker_window = tk.Toplevel(root)
        self.hitmarker_window.geometry('45x45')
        self.hitmarker_window.overrideredirect(True)
        self.hitmarker_window.wm_attributes('-transparent', '#f0f0f0')
        self.hitmarker_window.wm_attributes('-topmost', True)

        self.hitmarker_image = Image.open(f"{current_dir}\\memes\\cod_hitmarker.png")
        self.hitmarker_image = ImageTk.PhotoImage(self.hitmarker_image)

        self.hitmarker_panel = Label(self.hitmarker_window, image=self.hitmarker_image)
        self.hitmarker_panel.pack()


        logo_image = ImageTk.PhotoImage(Image.open(f"{current_dir}\\memes\\mlg_bomb_logo.png"))

        self.logo_label = Label(root, image=logo_image, bg='#1c1c27')
        self.logo_label.pack(side=TOP)


        self.hitmarker_int_var = IntVar(root, value=1)
        self.hitmarker_checkbox = Checkbutton(root, text="CoD hitmarker effect", font=self.font, onvalue=1, offvalue=0, variable=self.hitmarker_int_var, bg="#3b3b4d", fg="#ff0000", activebackground="#3b3b4d", activeforeground="#ff0000").pack(side=LEFT)


        self.move_meme_int_var = IntVar(root, value=0)
        self.move_meme_checkbox = Checkbutton(root, text="Move memes randomly", font=self.font, onvalue=1, offvalue=0, variable=self.move_meme_int_var, bg="#3b3b4d", fg="#ff0000", activebackground="#3b3b4d", activeforeground="#ff0000").place(x=0, y=290)

        # mouse effect
        def move_hitmarker(event):
            self.hitmarker_window.geometry(f'+{event[0]-23}+{event[1]-25}')
    

        def get_click():
            while True:
                if self.hitmarker_int_var.get() == 1:
                    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
                        move_hitmarker(win32api.GetCursorPos())
                        display_effect()
                        time.sleep(0.001)


        def display_effect():
            pygame.mixer.music.load(f'{current_dir}\\audio\\hitmarker_2.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(loops=0)
            self.hitmarker_panel.pack()
            self.hitmarker_window.after(100, self.hitmarker_panel.pack_forget)

        t = threading.Thread(target=get_click).start()

        # memes
        def pepe():
            pepe_window = tk.Toplevel(root)
            pepe_window.config(bg='#f0f0f0')
            pepe_window.geometry('+700+300')
            pepe_window.overrideredirect(True)
            pepe_window.wm_attributes('-transparent', '#f0f0f0')
            pepe_window.lift()
            pepe_img = Image.open(f'{current_dir}\\memes\\pepe.png')
            pepe_img = ImageTk.PhotoImage(pepe_img)

            def move_pepe_randomly():
                while True:
                    if self.move_meme_int_var.get() == 1:
                        pepe_window.geometry(f'+{random.randint(100, 900)}+{random.randint(100, 900)}')
                        time.sleep(0.3)

            def move_pepe(event=None):
                x, y = pepe_window.winfo_pointerxy()
                pepe_window.geometry(f'+{x-60}+{y-50}')

            pepe_panel = Label(pepe_window, image=pepe_img)
            pepe_panel.pack()
            threading.Thread(target=move_pepe_randomly).start()
            pepe_window.bind('<B1-Motion>', move_pepe)
            pepe_window.mainloop()


        def glasses():
            glasses_window = tk.Toplevel(root)
            glasses_window.config(bg='#f0f0f0')
            glasses_window.geometry('+800+300')
            glasses_window.overrideredirect(True)
            glasses_window.wm_attributes('-transparent', '#f0f0f0')
            glasses_window.lift()
            glasses_img = Image.open(f'{current_dir}\\memes\\mlg_glasses.png')
            glasses_img = ImageTk.PhotoImage(glasses_img)

            def move_glasses(event=None):
                x, y = glasses_window.winfo_pointerxy()
                glasses_window.geometry(f'+{x-45}+{y-5}')

            glasses_panel = Label(glasses_window, image=glasses_img)
            glasses_panel.pack()

            glasses_window.bind('<B1-Motion>', move_glasses)
            glasses_window.mainloop()


        def sanic():
            sanic_window = tk.Toplevel(root)
            sanic_window.config(bg='#f0f0f0')
            sanic_window.geometry('+600+300')
            sanic_window.overrideredirect(True)
            sanic_window.wm_attributes('-transparent', '#f0f0f0')
            sanic_window.lift()
            sanic_img = Image.open(f'{current_dir}\\memes\\sanic.png')
            sanic_img = ImageTk.PhotoImage(sanic_img)

            def move_sanic_randomly():
                while True:
                    if self.move_meme_int_var.get() == 1:
                        sanic_window.geometry(f'+{random.randint(100, 900)}+{random.randint(100, 900)}')
                        time.sleep(0.3)

            def move_sanic(event=None):
                x, y = sanic_window.winfo_pointerxy()
                sanic_window.geometry(f'+{x-110}+{y-80}')


            sanic_panel = Label(sanic_window, image=sanic_img)
            sanic_panel.pack()
            threading.Thread(target=move_sanic_randomly).start()
            sanic_window.bind('<B1-Motion>', move_sanic)
            sanic_window.mainloop()


        def doritos():
            doritos_window = tk.Toplevel(root)
            doritos_window.config(bg='#f0f0f0')
            doritos_window.geometry('+600+300')
            doritos_window.overrideredirect(True)
            doritos_window.wm_attributes('-transparent', '#f0f0f0')
            doritos_window.lift()
            doritos_img = Image.open(f'{current_dir}\\memes\\doritos.png')
            doritos_img = ImageTk.PhotoImage(doritos_img)

            def move_doritos(event=None):
                x, y = doritos_window.winfo_pointerxy()
                doritos_window.geometry(f'+{x-50}+{y-60}')

            doritos_panel = Label(doritos_window, image=doritos_img)
            doritos_panel.pack()

            doritos_window.bind('<B1-Motion>', move_doritos)
            doritos_window.mainloop()


        def dew():
            mtn_dew_window = tk.Toplevel(root)
            mtn_dew_window.config(bg='#f0f0f0')
            mtn_dew_window.geometry('+300+600')
            mtn_dew_window.overrideredirect(True)
            mtn_dew_window.wm_attributes('-transparent', '#f0f0f0')
            mtn_dew_window.lift()

            mtn_dew_img = Image.open(f'{current_dir}\\memes\\mtn_dew.png')
            mtn_dew_img = ImageTk.PhotoImage(mtn_dew_img)

            def move_dew(event=None):
                x, y = mtn_dew_window.winfo_pointerxy()
                mtn_dew_window.geometry(f'+{x-30}+{y-50}')

            mtn_dew_panel = Label(mtn_dew_window, image=mtn_dew_img)
            mtn_dew_panel.pack()

            mtn_dew_window.bind('<B1-Motion>', move_dew)
            mtn_dew_window.mainloop()


        def doge():
            doge_window = tk.Toplevel(root)
            doge_window.config(bg='#f0f0f0')
            doge_window.geometry('+500+400')
            doge_window.overrideredirect(True)
            doge_window.wm_attributes('-transparent', '#f0f0f0')
            doge_window.lift()
            doge_img = Image.open(f'{current_dir}\\memes\\doge.png')
            doge_img = ImageTk.PhotoImage(doge_img)

            def move_doge_randomly():
                while True:
                    if self.move_meme_int_var.get() == 1:
                        doge_window.geometry(f'+{random.randint(100, 900)}+{random.randint(100, 900)}')
                        time.sleep(0.3)

            def move_doge(event=None):
                x, y = doge_window.winfo_pointerxy()
                doge_window.geometry(f'+{x-60}+{y-70}')

            doge_panel = Label(doge_window, image=doge_img)
            doge_panel.pack()
            threading.Thread(target=move_doge_randomly).start()
            doge_window.bind('<B1-Motion>', move_doge)
            doge_window.mainloop()


        def rainbow_frog():
            rainbow_frog_window = tk.Toplevel(root)
            rainbow_frog_window.config(bg='#f0f0f0')
            rainbow_frog_window.geometry('+200+200')
            rainbow_frog_window.overrideredirect(True)
            rainbow_frog_window.wm_attributes('-transparent', '#f0f0f0')
            rainbow_frog_window.lift()
            ind = 0
            image = Image.open(f'{current_dir}\\memes\\rainbow_frog_meme.gif')
            frameCnt = image.n_frames
            frames = [PhotoImage(file=f'{current_dir}\\memes\\rainbow_frog_meme.gif', width=rainbow_frog_window.winfo_x(), height=rainbow_frog_window.winfo_y(), format = f'gif -index {i}',) for i in range(frameCnt)]
            showAnimation = None

            def update(ind):
                global showAnimation
                frame = frames[ind]
                ind += 1
                if ind == frameCnt:
                    ind = 0
                label.configure(image=frame)
                showAnimation = rainbow_frog_window.after(100, update, ind)
            def move(event=None):
                x, y = rainbow_frog_window.winfo_pointerxy()
                rainbow_frog_window.geometry(f'+{x-50}+{y-50}')
            label = Label(rainbow_frog_window, image="")
            label.pack()
            threading.Thread(target=update(ind)).start()
            rainbow_frog_window.bind('<B1-Motion>', move)
        threading.Thread(target=rainbow_frog).start()

        # buttons
        self.rainbow_frog_button = Button(root, text="Rainbow frog", font=self.font, bg="#3b3b4d", fg="#00ff00", command=rainbow_frog).place(x=200, y=290)
        self.doritos_button = Button(root, text="Doritos", font=self.font, bg="#3b3b4d", fg="#00ff00", command=doritos).place(x=200, y=340)
        self.dew_button = Button(root, text="Moutain Dew", font=self.font, bg="#3b3b4d", fg="#00ff00", command=dew).place(x=310, y=290)
        self.glasses_button = Button(root, text="MLG Glasses", font=self.font, bg="#3b3b4d", fg="#00ff00", command=glasses).place(x=270, y=340)
        self.sanic_button = Button(root, text="Sanic", font=self.font, bg="#3b3b4d", fg="#00ff00", command=sanic).place(x=420, y=290)
        self.doge_button = Button(root, text="Doge", font=self.font, bg="#3b3b4d", fg="#00ff00", command=doge).place(x=380, y=340)
        self.pepe_button = Button(root, text="Pepe", font=self.font, bg="#3b3b4d", fg="#00ff00", command=pepe).place(x=480, y=290)
        self.exit_button = Button(root, text="Exit", font=self.font, bg="#ff0000", fg="#ffffff", command=(lambda: sys.exit())).place(x=820, y=0)


        # play MY HOPE WILL NEVER DIE
        def MY_HOPE_WILL_NEVER_DIE():
            pygame.mixer.music.load(f'{current_dir}\\audio\\MLG_MY_HOPE_WILL_NEVER_DIE.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(loops=0)
        
        self.my_hope_will_never_die_button = Button(root, text="MY HOPE WILL NEVER DIE", font=self.font, bg="#3b3b4d", fg="#ff00ff", command=MY_HOPE_WILL_NEVER_DIE).place(x=0, y=430)

        # starting functions
        root.after(7, pepe)
        root.after(6, glasses)
        root.after(5, sanic)
        root.after(10, doritos)
        root.after(1, dew)
        root.after(2, doge)

        # starting a window
        root.lift()

        root.mainloop()

# starting a thread to start a class
threading.Thread(target=Main).start()
