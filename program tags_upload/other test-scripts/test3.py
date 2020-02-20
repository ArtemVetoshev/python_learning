# import tkinter as tk
# from tkinter import ttk
# import sqlite3


# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self.init_main()
#         self.db = db
#         self.view_records()

#     def init_main(self):
#         toolbar = tk.Frame(bg='#d7d8e0', bd=2)
#         toolbar.pack(side=tk.TOP, fill=tk.X)

#         # self.add_img = tk.PhotoImage(file='add.gif')
#         btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
#                                     compound=tk.TOP)
#         btn_open_dialog.pack(side=tk.LEFT)

#         self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15, show='headings')

#         self.tree.column('ID', width=30, anchor=tk.CENTER)
#         self.tree.column('description', width=365, anchor=tk.CENTER)
#         self.tree.column('costs', width=150, anchor=tk.CENTER)
#         self.tree.column('total', width=100, anchor=tk.CENTER)

#         self.tree.heading('ID', text='ID')
#         self.tree.heading('description', text='Наименование')
#         self.tree.heading('costs', text='Статья дохода\расхода')
#         self.tree.heading('total', text='Сумма')

#         self.tree.pack()

#     def records(self, description, costs, total):
#         self.db.insert_data(description, costs, total)
#         self.view_records()

#     def view_records(self):
#         self.db.c.execute('''SELECT * FROM finance''')
#         [self.tree.delete(i) for i in self.tree.get_children()]
#         [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

#     def open_dialog(self):
#         Child()


# class Child(tk.Toplevel):
#     def __init__(self):
#         super().__init__(root)
#         self.init_child()
#         self.view = app

#     def init_child(self):
#         self.title('Добавить доходы\расходы')
#         self.geometry('400x220+400+300')
#         self.resizable(False, False)

#         label_description = tk.Label(self, text='Наименование:')
#         label_description.place(x=50, y=50)
#         label_select = tk.Label(self, text='Статья дохода\расхода:')
#         label_select.place(x=50, y=80)
#         label_sum = tk.Label(self, text='Сумма:')
#         label_sum.place(x=50, y=110)

#         self.entry_description = ttk.Entry(self)
#         self.entry_description.place(x=200, y=50)

#         self.entry_money = ttk.Entry(self)
#         self.entry_money.place(x=200, y=110)

#         self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
#         self.combobox.current(0)
#         self.combobox.place(x=200, y=80)

#         btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
#         btn_cancel.place(x=300, y=170)

#         btn_ok = ttk.Button(self, text='Добавить')
#         btn_ok.place(x=220, y=170)
#         btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
#                                                                   self.entry_money.get(),
#                                                                   self.combobox.get()))

#         self.grab_set()
#         self.focus_set()


# class DB:
#     def __init__(self):
#         self.conn = sqlite3.connect('finance.db')
#         self.c = self.conn.cursor()
#         self.c.execute(
#             '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)''')
#         self.conn.commit()

#     def insert_data(self, description, costs, total):
#         self.c.execute('''INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)''',
#                        (description, costs, total))
#         self.conn.commit()


# if __name__ == "__main__":
#     root = tk.Tk()
#     db = DB()
#     app = Main(root)
#     app.pack()
#     root.title("Household finance")
#     root.geometry("650x450+300+200")
#     root.resizable(False, False)
#     root.mainloop()'

import requests
import datetime
from pickle import dumps, load, loads
from lxml import html
from collections import Counter
import json
import re
import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2 import sql

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('site', 'url'),
                                 height=15, show='headings')
        self.tree.column("site", width=30, anchor=tk.CENTER)
        self.tree.column("url", width=365, anchor=tk.CENTER)
        # self.tree.column("date", width=150, anchor=tk.CENTER)
        # self.tree.column("tags", width=100, anchor=tk.CENTER)

        self.tree.heading("site", text='Название сайта')
        self.tree.heading("url", text='Ссылка')
        # self.tree.heading("date", text='Статья дохода/расхода')
        # self.tree.heading("tags", text='Сумма')

        self.tree.pack()

    def records(self, url):
        print(url)
        self.url_split = str(url)
        self.site = self.url_split.split("//")[-1].split("/")[0]
        self.db.insert_data(self.site, str(url))
        self.view_records()


    def view_records(self):
        self.db.c.execute('''SELECT site, url FROM site''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Загрузка тегов')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_select = tk.Label(self, text='Сайт:')
        label_select.place(x=50, y=80)

        result = []
        with open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'r') as f:
            for row in f:
                result.append(row.split(',')[0])
        result = list(set(result))

        self.url = ttk.Combobox(self, values=result)
        self.url.current(0)
        self.url.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.url.get()))

        self.grab_set()
        self.focus_set()

class DB:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='root', host='localhost', port='5432')
        self.c = self.conn.cursor()
        self.c.execute('drop table if exists site')
        self.c.execute('CREATE TABLE IF NOT EXISTS site (site varchar, url varchar)')
        self.conn.commit()

    def insert_data(self, site, url):
        print(url+"insert")
        # self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'r')
        # data = self.f.read()
        self.values = [site, url]
        self.c.execute(sql.SQL('INSERT INTO site VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, self.values))))
        self.conn.commit()
        # self.f.close()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Информация по тегам")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()