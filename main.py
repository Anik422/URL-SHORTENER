import bitly_api
from tkinter import *
import time
from tkinter import messagebox
from PIL import Image, ImageTk
import threading

class Url_short:
    def __init__(self, root):
        self.root = root
        self.root.title("URL SHORTENER")
        self.root.geometry("300x340+1050+340")
        self.root.iconphoto(False, PhotoImage(file="image\icon.png"))
        self.root.configure(bg="#FFFFFF")


        body_frame = LabelFrame(self.root, bd=2, bg="#FFFFFF")
        body_frame.place(x=10, y=35, width=280, height=300)

        # ========================= top lable =========================
        # top_lbl = Label(self.root, text="URL SHORTENER", font=("Ruda", 15, "bold"), fg="#FFFFFF", bg="#F67656")
        # top_lbl.place( x=0, y=0, width=300)
        #  #   ========================  Top Image lable frame ========================

        top_img = Image.open("image/icon.png")
        top_img = top_img.resize((100, 100))#, Image.ANTIALIAS
        self.photoTopImg = ImageTk.PhotoImage(top_img)
        topLblImg = Label(self.root, image=self.photoTopImg, bd=0, relief="groove", bg='#FFFFFF').place(x=120, y=-7, width=67, height=80)
       
        # ========================= Enter url link =========================
        def on_enter_url(event):
            entry_url_value = self.entry_url.get()
            if entry_url_value == 'Enter Url':
                self.entry_url.delete(0, END)
        
        def on_leave_url(event):
            entry_url_value = self.entry_url.get()
            if entry_url_value == '':
                self.entry_url.insert(0, "Enter Url")
    

        self.entry_url = Entry(body_frame, font=("Ruda", 9), bd=0, fg="black", bg="#E8E8E8", justify=CENTER)
        self.entry_url.place(x=20, y=70, width=240, height=25)
        self.entry_url.insert(0, "Enter Url")
        self.entry_url.bind("<FocusIn>", on_enter_url)
        self.entry_url.bind("<FocusOut>", on_leave_url)
        entry_url_frame = Frame(body_frame, bg="dimgray")
        entry_url_frame.place(x=20, y=95, width=240, height=2)

        # =========================  url short button =========================
        button = Button(body_frame, text="Create Short Url", font=("Ruda", 11, "bold"), fg="#FFFFFF", bg="#F67656", bd=1, command=lambda:threading.Thread(target=self.creat_new_url()).start())
        button.place(x=45, y=105, width=180, height=30)

        # =========================  copyed msg show =========================
        self.msg_show = Label(body_frame, bg="#FFFFFF", fg="#F67656", font=("Ruda", 10))
        self.msg_show.place(x=100, y=155, width=80, height=20)

        # =========================  shorted url lable =========================
        self.entry_new_url = Entry(body_frame, font=("Ruda", 9), bd=0, fg="black", bg="#E8E8E8", justify=CENTER)
        self.entry_new_url.place(x=20, y=190, width=240, height=25)
        entry_url_frame = Frame(body_frame, bg="dimgray")
        entry_url_frame.place(x=20, y=215, width=240, height=2)

        copy_btn =  Button(body_frame, text="Copy Short Url", font=("Ruda", 11, "bold"), fg="#FFFFFF", bg="#F67656", bd=1, command= lambda:threading.Thread(target=self.new_url_copy()).start() )
        copy_btn.place(x=40, y=225, width=180, height=30)
        #   =======================   create title  ========================
        create_tatle = Label(self.root, text="© 2022 | CREATE BY ANIK SAHA", font=(
            "Ruda", 8), fg="#F67656", bg="white")
        create_tatle.place(x=75, y=320)
    

    # ========================= create new url =========================
    def creat_new_url(self):
        self.entry_new_url.delete(0, END)
        entr_url = self.entry_url.get()
        if entr_url != "Enter Url":
            try:
                BITLY_ACCESS_TOKEN = "74e40eae5737852ee2bba8ece28adb3b452208c4"
                bit = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
                new_url = bit.shorten(entr_url)
                self.entry_new_url.insert(0, new_url['url'])
                self.entry_url.delete(0, END)
            except Exception as ex:
                messagebox.showwarning('Worning', "The link you provided is already short.", parent=self.root)
                self.entry_url.delete(0, END)


    # ========================= new url copy =========================
    def new_url_copy(self):
        if self.entry_new_url.get() != '':
            self.root.clipboard_clear()
            self.root.clipboard_append(self.entry_new_url.get().rstrip())
            self.msg_show.config(text="Copied")
            self.msg_show.update()
            time.sleep(2)
            self.msg_show.config(text="")
            self.msg_show.update()
            
            






if __name__ == "__main__":
    root = Tk(className='Python Examples - Window Size')
    obj = Url_short(root)
    root.mainloop()