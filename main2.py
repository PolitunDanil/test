import tkinter as tk


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
        self.entry = tk.Entry(self, width=30)
        self.entry2 = tk.Entry(self, width=30)

    def init_child(self):
        self.title('Home')
        self.geometry('500x400')

        self.grab_set()
        self.focus_set()
        btn1 = tk.Button(self, text='+', command=self.add_new)
        btn1.place(x=30, y=20)

    def add_new(self):
        self.entry.place(x=20,y=50)
        btn2 = tk.Button(self, text='+', command=self.add_new2)
        btn2.place(x=300, y=20)

    def add_new2(self):
        self.entry2.place(x=300,y=50)
        




if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Entrance')
    root.geometry('700x400')

    root.mainloop()
