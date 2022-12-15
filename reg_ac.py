from pokemons import *
import db
import re
from email_validator import validate_email, EmailNotValidError


class registration(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.new_window = parent
        self.title('Registration')
        self.geometry('600x400')
        self.db = db
        self.labls()
        self.entries()
        self.btn_to_main = Button(self, text='Go to log', bg='black', fg='white', command=self.check_pass)
        self.btn_to_main.place(x=290, y=300)

    def labls(self):
        self.deiconify()
        self.lable_registr = Label(self, text="REGISTRATION", font='Bold 25')
        self.lable_registr.place(x=200, y=20)
        self.lable_name = Label(self, text='Name')
        self.lable_name.place(x=300, y=100)
        self.lable_surname = Label(self, text='Surname')
        self.lable_surname.place(x=295, y=140)
        self.lable_email = Label(self, text='Email')
        self.lable_email.place(x=300, y=200)
        self.lable_pass = Label(self, text='Password')
        self.lable_pass.place(x=290, y=240)

    def entries(self):
        self.entry_name = Entry(self)
        self.entry_name.place(x=260, y=120)
        self.entry_surname = Entry(self, width=30)
        self.entry_surname.place(x=230, y=160)
        self.entry_email = Entry(self, width=40)
        self.entry_email.place(x=200, y=220)
        self.entry_pass = Entry(self, width=40)
        self.entry_pass.place(x=200, y=260)

    def check_pass(self):
        check_pass = self.entry_pass.get()
        fl = 0
        if (len(check_pass) < 8):
            fl = -1
            print('введите не менее 8 символов пароля')
        elif not re.search("[a-z]", check_pass):
            fl = -1
            print('используйте латинские и заглавные буквы')
        elif not re.search("[A-Z]", check_pass):
            fl = -1
            print('используйте латинские и заглавные буквы')
        elif not re.search("[0-9]", check_pass):
            fl = -1
            print('используйте цифры в пароле')
        if fl == 0:
            self.check_name()

    def check_name(self):
        check_name = self.entry_name.get()
        global gg
        gg = 0
        if (len(check_name) < 1):
            gg = -1
            print('введите имя')
        elif gg == 0:
            self.check_em()

    def check_em(self):
        check_em = self.entry_email.get()
        if (len(check_em) > 5):
            try:
                validation = validate_email(check_em, check_deliverability=True)
                print(type(validation))
                self.check_sr()
            except EmailNotValidError as e:
                print(str(e))
                print('неверный эмейл')
        else:
            print('введите корректный эмейл')


    def check_sr(self):
        check_surname = self.entry_surname.get()
        global ww
        ww = 0
        if (len(check_surname) < 1):
            ww = -1
            print('введите фамилию')
        elif ww == 0:
            self.to_db()

    def to_db(self):
        add_to_db_email = self.entry_email.get()
        add_to_db_password = self.entry_pass.get()
        add_to_db_name = self.entry_name.get()
        add_to_db_surname = self.entry_surname.get()
        self.mycoursor = self.db.cnx.cursor()
        data = (add_to_db_email, add_to_db_password, add_to_db_name, add_to_db_surname)
        req = "INSERT INTO users(email, password, name, surname) values(%s, %s, %s, %s)"
        with self.mycoursor as cursor:
            cursor.execute(req, data)
        self.db.cnx.commit()
        print('регистрация оконченна')
        self.new_window.__init__()
        self.withdraw()
