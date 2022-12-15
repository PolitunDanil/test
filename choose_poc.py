from pokemons import *
from poc_list import *


class stats(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.btn = Button
        self.window = parent
        self.listbox = Listbox(self, width=18, height=5, background='#f0f0f0', font='Fixedsys 14', borderwidth=0)
        self.title('Stata')
        self.geometry('800x550')
        self.canvas = Canvas(self, width=200, height=200)
        self.button_back()


    def stats_1(self):
        self.lable = Label(self, text=self.window.take_pokemon_name[0], font='Bold 30')
        self.lable.place(x=320, y=20)
        self.listbox.place(x=450, y=200)
        self.listbox.insert(0, self.window.hp[0])
        self.listbox.insert(0, self.window.attack[0])
        self.listbox.insert(0, self.window.deffense[0])
        self.listbox.insert(0, self.window.special_attack[0])
        self.canvas.create_image(10, 10, anchor='nw', image=self.window.result[0])
        self.canvas.place(x=170, y=100)

    def stats_2(self):
        self.lable = Label(self, text=self.window.take_pokemon_name[1], font='Bold 30')
        self.lable.place(x=320, y=20)
        self.listbox.place(x=450, y=200)
        self.listbox.insert(0, self.window.hp[1])
        self.listbox.insert(0, self.window.attack[1])
        self.listbox.insert(0, self.window.deffense[1])
        self.listbox.insert(0, self.window.special_attack[1])
        self.canvas.create_image(10, 10, anchor='nw', image=self.window.result[1])
        self.canvas.place(x=170, y=100)

    def stats_3(self):
        self.lable = Label(self, text=self.window.take_pokemon_name[2], font='Bold 30')
        self.lable.place(x=320, y=20)
        self.listbox.place(x=450, y=200)
        self.listbox.insert(0, self.window.hp[2])
        self.listbox.insert(0, self.window.attack[2])
        self.listbox.insert(0, self.window.deffense[2])
        self.listbox.insert(0, self.window.special_attack[2])
        self.canvas.create_image(10, 10, anchor='nw', image=self.window.result[2])
        self.canvas.place(x=170, y=100)

    def stats_4(self):
        self.lable = Label(self, text=self.window.take_pokemon_name[3], font='Bold 30')
        self.lable.place(x=320, y=20)
        self.listbox.place(x=450, y=200)
        self.listbox.insert(0, self.window.hp[3])
        self.listbox.insert(0, self.window.attack[3])
        self.listbox.insert(0, self.window.deffense[3])
        self.listbox.insert(0, self.window.special_attack[3])
        self.canvas.create_image(10, 10, anchor='nw', image=self.window.result[3])
        self.canvas.place(x=170, y=100)

    def stats_5(self):
        self.lable = Label(self, text=self.window.take_pokemon_name[4], font='Bold 30')
        self.lable.place(x=320, y=20)
        self.listbox.place(x=450, y=200)
        self.listbox.insert(0, self.window.hp[4])
        self.listbox.insert(0, self.window.attack[4])
        self.listbox.insert(0, self.window.deffense[4])
        self.listbox.insert(0, self.window.special_attack[4])
        self.canvas.create_image(10, 10, anchor='nw', image=self.window.result[4])
        self.canvas.place(x=170, y=100)

    def stats_6(self):
        self.lable = Label(self, text=self.window.take_pokemon_name[5], font='Bold 30')
        self.lable.place(x=320, y=20)
        self.listbox.place(x=450, y=200)
        self.listbox.insert(0, self.window.hp[5])
        self.listbox.insert(0, self.window.attack[5])
        self.listbox.insert(0, self.window.deffense[5])
        self.listbox.insert(0, self.window.special_attack[5])
        self.canvas.create_image(10, 10, anchor='nw', image=self.window.result[5])
        self.canvas.place(x=170, y=100)

    def button_back(self):
        self.btn = Button(self, text='<--', bg='black', fg='white', command=self.back_to_choose_poc)
        self.btn.place(x=20, y=20)

    def back_to_choose_poc(self):
        self.window.__init__()
        self.withdraw()

