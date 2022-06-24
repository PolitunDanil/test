from tkinter import *
import tkinter as tk
from tkinter.ttk import *



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        text = tk.Label(text='Shop', font='Bold 20', width=20, height=5)
        text_log = tk.Label(text='email', width=10, height=1)
        log = tk.Entry()
        text_pass = tk.Label(text="password", width=10, height=2)
        password = tk.Entry(show='&')
        btn = tk.Button(text='login', bg='green', command=self.new_window)
        text.pack()
        text_log.pack()
        log.pack()
        text_pass.pack()
        password.pack()
        btn.pack()

    def new_window(self):
        Child()


class Child(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.entry = Entry(self, width=30)
        self.entry2 = Entry(self, width=30)

        




    def init_child(self):
        self.title('Home')
        self.geometry('500x400')
        self.grab_set()
        self.focus_set()

        btn1 = tk.Button(self, text='+', command=self.add_new)
        btn1.place(x=30, y=20)
    sv = StringVar


    def add_new(self):
        self.theList = Listbox(self, selectmode=SINGLE)
        
        self.theList.place(x=20, y=50)
        self.theList.insert(0, "Что мне нужно:")
        

        btn2 = Button(self, text='+', command=self.add_new2)
        btn2.place(x=300, y=20)
        btn4 = Button(self, text='Удалить', command=self.off_list)
        btn4.place(x=30, y=220)

    def add_new2(self):
        self.entry2.place(x=300, y=50)
        btn3 = Button(self, text='Добавить в список', command=self.to_list)
        btn3.place(x=300, y=75)


    def to_list(self):
        add_list = self.entry2.get()
        self.theList.insert(END, add_list)

    def off_list(self):
        what = self.theList.curselection()
        self.theList.delete(what[0])







if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Entrance')
    root.geometry('700x400')

    root.mainloop()
