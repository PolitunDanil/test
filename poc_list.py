import threading
from tkinter import Button
from threading import *
from pokemons import *
from pokemons.choose_poc import stats


class Photo_poc(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.deiconify()
        self.label = tk.Label
        self.init_child()

    def init_child(self):
        self.title('Pokemons')
        self.geometry('800x550')
        self.for_page()


    def for_page(self):
        global take_url_pokemon
        global take_next
        self.take_pokemon_name = []
        take_url_pokemon = []
        url = "https://pokeapi.co/api/v2/pokemon/?limit=6&offset=0"
        response = r.get(url=url)
        data_1 = response.json()
        take_next = data_1['next']
        for i in data_1['results']:
            take_url_pokemon.append(i['url'])
        for i in data_1['results']:
            self.take_pokemon_name.append(i['name'])
        self.collect_data()

    def next_page(self):
        global take_url_pokemon
        global take_previous
        global take_next
        self.take_pokemon_name = []
        take_url_pokemon = []
        url = take_next
        response = r.get(url=url)
        data_1 = response.json()
        take_previous = data_1['previous']
        take_next = data_1['next']
        for i in data_1['results']:
            take_url_pokemon.append(i['url'])
        for i in data_1['results']:
            self.take_pokemon_name.append(i['name'])
        self.collect_data()

    def previous_page(self):
        global take_url_pokemon
        global take_previous
        global take_next
        self.take_pokemon_name = []
        take_url_pokemon = []
        url = take_previous
        response = r.get(url=url)
        data_1 = response.json()
        take_previous = data_1['previous']
        take_next = data_1['next']
        for i in data_1['results']:
            take_url_pokemon.append(i['url'])
        for i in data_1['results']:
            self.take_pokemon_name.append(i['name'])
        self.collect_data()

    def collect_data(self):
        global take_poc_stat
        take_poc_stat = []
        self.result = []
        for i in take_url_pokemon:
            url = i
            response = r.get(url=url)
            data = response.json()
            take_photo_url = data["sprites"]["other"]["home"]["front_default"]
            take_poc_stat.append(data['stats'])
            image_1 = Image.open(urlopen(take_photo_url))
            size = 200, 200
            image_1.thumbnail(size)
            self.result.append(ImageTk.PhotoImage(image_1))
            self.label = tk.Label()
            self.label.pack()
            self.label.image = self.result

        self.btn1 = Button(self, image=self.result[0], background='white', command=self.new_window)
        self.btn1.place(x=30, y=10)
        self.btn2 = Button(self, image=self.result[1], background='white', command=self.new_window2)
        self.btn2.place(x=300, y=10)
        self.btn3 = Button(self, image=self.result[2], background='white', command=self.new_window3)
        self.btn3.place(x=570, y=10)
        self.btn4 = Button(self, image=self.result[3], background='white', command=self.new_window4)
        self.btn4.place(x=30, y=300)
        self.btn5 = Button(self, image=self.result[4], background='white', command=self.new_window5)
        self.btn5.place(x=300, y=300)
        self.btn6 = Button(self, image=self.result[5], background='white', command=self.new_window6)
        self.btn6.place(x=570, y=300)

        self.btn_next = Button(self, text='Next page', bg='black', fg='white', command=self.potoc_next)
        self.btn_next.place(x=420, y=250)
        self.btn_previous = Button(self, text='Privious page', bg='black', fg='white', command=self.potoc_previous)
        self.btn_previous.place(x=320, y=250)
        self.take_stats()

    def potoc_next(self):
        self.t_next = threading.Thread(target=self.next_page)
        self.t_next.start()

    def potoc_previous(self):
        self.t_prev = Thread(target=self.previous_page)
        self.t_prev.start()


    def take_stats(self):
        self.special_attack = []
        self.deffense = []
        self.attack = []
        self.hp = []
        for i in take_poc_stat:
            hit_point = i[0]
            attack = i[1]
            deffense = i[2]
            special_attack = i[3]
            self.hp.append(hit_point['stat']['name'] + ' ' + str(hit_point['base_stat']))
            self.attack.append(attack['stat']['name'] + ' ' + str(hit_point['base_stat']))
            self.deffense.append(deffense['stat']['name'] + ' ' + str(deffense['base_stat']))
            self.special_attack.append(special_attack['stat']['name'] + ' ' + str(special_attack['base_stat']))

    def new_window(self):
        stats(self).stats_1()
        self.withdraw()

    def new_window2(self):
        stats(self).stats_2()
        self.withdraw()

    def new_window3(self):
        stats(self).stats_3()
        self.withdraw()

    def new_window4(self):
        stats(self).stats_4()
        self.withdraw()

    def new_window5(self):
        stats(self).stats_5()
        self.withdraw()

    def new_window6(self):
        stats(self).stats_6()
        self.withdraw()
