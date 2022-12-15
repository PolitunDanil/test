import tkinter
import tkinter as tk
from tkinter import *
import requests as r
from PIL import Image, ImageTk
import json
from urllib.request import urlopen
from poc_list import *
from reg_ac import *
import db


class Main(tk.Frame):
    def __init__(self):
        super().__init__(root)
        root.deiconify()
        self.db = db
        self.lable = tk.Label
        self.btn_go = tk.Button
        self.btn_reg = tk.Button
        self.entrys()

    def entrys(self):
        self.lable = Label(text='Let is start', font='Times 40')
        self.lable.place(x=220, y=20)
        self.lable = Label(text='Email')
        self.lable.place(x=320, y=150)
        self.login = Entry()
        self.login.place(x=275, y=170)
        self.lable = Label(text='Password')
        self.lable.place(x=310, y=200)
        self.password = Entry(show='*')
        self.password.place(x=275, y=220)
        self.btn_what_to_do_next()
        with open("email.txt", "r") as f:
            text = f.readlines()
            self.login.insert(0, text[0])
        with open("password.txt", "r") as f:
            text = f.readlines()
            self.password.insert(0, text[0])

    def btn_what_to_do_next(self):
        self.btn_go = Button(text='Login', bg='black', fg='white', command=self.go_to_poc)
        self.btn_reg = Button(text='Registration', bg='black', fg='white', command=self.registr)
        self.btn_go.place(x=315, y=250)
        self.btn_reg.place(x=300, y=350)

    def go_to_poc(self):
        check_em = self.login.get()
        data_em = (check_em,)
        check_pass = self.password.get()
        data_pass = (check_pass,)
        self.mycursor = self.db.cnx.cursor(buffered=True)
        req = 'SELECT * FROM users WHERE email = %s'
        qer = 'SELECT * FROM users WHERE password = %s'
        self.mycursor.execute(req, data_em)
        self.db.cnx.commit()
        with open('email.txt', 'w') as f:
            f.write(check_em)
        if not self.mycursor.fetchone():
            print('не верный логин')
            self.__init__()
        else:
            self.mycursor.execute(qer, data_pass)
            self.db.cnx.commit()
            with open('password.txt', 'w') as f:
                f.write(check_pass)
        if not self.mycursor.fetchone():
            print('не верный пароль')
            self.__init__()
        else:
            Photo_poc()
            root.withdraw()

    def registr(self):
        registration(self)
        root.withdraw()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main()
    app.pack()
    root.title('Entrance')
    root.geometry('700x400')
    root.mainloop()
