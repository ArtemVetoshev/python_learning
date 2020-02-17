# import requests
# import datetime
# from pickle import dumps, load, loads
# from lxml import html
# from collections import Counter
# import json
# import re
# import tkinter as tk
# from tkinter import ttk
# import psycopg2
# from psycopg2 import sql

# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)

#         self.init_main()
#         self.db = db
#         self.view_records()


#     def init_main(self):
#         toolbar = tk.Frame(bg='#d7d8e0', bd=2)
#         toolbar.pack(side=tk.TOP, fill=tk.X)

#         btn_site = ttk.Button(toolbar, text='Получить информацию по сайту:')
#         btn_site.bind('<Button-1>', lambda event: self.records(self.url.get()))
#         btn_site.pack(side=tk.LEFT)

#         # btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
#         #                             compound=tk.TOP)
#         # btn_open_dialog.pack(side=tk.LEFT)

#         self.tree = ttk.Treeview(self, columns=('site_name', 'url', 'date', 'tags'),
#                                  height=15, show='headings')

#         result = []
#         # with open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'r') as f:
#         with open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'r') as f:
#             for row in f:
#                 result.append(row.split(',')[0])
#         result = list(set(result))
#         self.url = ttk.Combobox(toolbar, values=result)
#         self.url.current(0)
#         self.url.place(x=200, y=2, width = 300)

#         # self.url = ttk.Entry(toolbar)
#         # self.url.place(x=200, y=2, width = 300)

#         self.tree.column("site_name", width=30, anchor=tk.CENTER)
#         self.tree.column("url", width=365, anchor=tk.CENTER)
#         self.tree.column("date", width=150, anchor=tk.CENTER)
#         self.tree.column("tags", width=100, anchor=tk.CENTER)

#         self.tree.heading("site_name", text='Домен')
#         self.tree.heading("url", text='Ссылка на сайт')
#         self.tree.heading("date", text='Дата')
#         self.tree.heading("tags", text='Теги')

#         self.tree.pack()

#     def records(self, url):
#     	self.url_split = str(self.url)
#     	# self.site = self.url_split.split("//")[-1].split("/")[0]
#     	self.page = requests.get(self.url)
#     	self.tree = html.fromstring(self.page.content)
#     	self.now = datetime.datetime.now()

#     	self.f = open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'a')
#     	self.f.write('{}, {}\n'.format(self.url_split, self.now.strftime("%Y-%m-%d %H:%M:%S")))
#     	self.f.close()

#     	self.all_elms = self.tree.cssselect('*')
#     	self.all_tags = [x.tag for x in self.all_elms]
#     	self.c = Counter(self.all_tags)

#     	self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'w')
#     	for e in self.c:
#     		self.d = "{" + ", ".join(json.dumps('{}: {}'.format(e, self.c[e])) for e in self.c ) + "}"
#     	self.reg = re.sub(r'\"+(\w+)\: +' r'(\d{1,4})\"', r'"\1": \2', self.d)
#     	self.f.write(self.reg)
#     	self.f.close()

#     	self.db.insert_data(site_name, url, now)
#     	self.view_records()


#     def view_records(self):
#         self.db.c.execute('''SELECT site_name, url, date, tags FROM tags''')
#         [self.tree.delete(i) for i in self.tree.get_children()]
#         [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]



# class DB:
#     def __init__(self):
#         self.conn = psycopg2.connect(dbname='postgres', user='postgres',
#                         password='root', host='localhost', port='5432')
#         self.c = self.conn.cursor()
#         self.c.execute('drop table if exists tags')
#         self.c.execute('CREATE TABLE IF NOT EXISTS tags (site_name varchar, url varchar, date timestamp, pickled_tags text, tags jsonb)')
#         self.conn.commit()

#     def insert_data(self, site, url, date, pickled_tags, tags):
#     	self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'r')
#     	self.data = self.f.read()
#     	self.values = [self.site, self.url, self.date, dumps(self.data), self.data]
#     	self.c.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, self.values))))
#     	self.conn.commit()
#     	self.f.close()

# url = ('https://vk.com/im?peers=36283568_c144_60616368')
# site = url.split("//")[-1].split("/")[0]
# page = requests.get(url)
# tree = html.fromstring(page.content)
# now = datetime.datetime.now()

# f = open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'a')
# f.write('{}, {}\n'.format(site, now.strftime("%Y-%m-%d %H:%M:%S")))
# f.close()

# all_elms = tree.cssselect('*')
# all_tags = [x.tag for x in all_elms]
# c = Counter(all_tags)

# f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'w')
# for e in c:
# 	d = "{" + ", ".join(json.dumps('{}: {}'.format(e, c[e])) for e in c ) + "}"
# reg = re.sub(r'\"+(\w+)\: +' r'(\d{1,4})\"', r'"\1": \2', d)
# f.write(reg)
# print(reg)
# f.close()

# f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'r')
# data = f.read()
# print(data)
# values = [site, url, now.strftime("%Y-%m-%d %H:%M:%S"), dumps(data), data]
# cur.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, values))))
# f.close()


# if __name__ == "__main__":
#     root = tk.Tk()
#     db = DB()
#     app = Main(root)
#     app.pack()
#     root.title("Домашние финансы")
#     root.geometry("650x450+300+200")
#     root.resizable(False, False)
#     root.mainloop()



# -------------------------------------------------------------

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

        # self.add_img = tk.PhotoImage(file="C:/Users/artem_vetoshev/Desktop/add.png")
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('site_name', 'url', 'date', 'tags'),
                                 height=15, show='headings')
        self.tree.column("site_name", width=30, anchor=tk.CENTER)
        self.tree.column("url", width=365, anchor=tk.CENTER)
        self.tree.column("date", width=150, anchor=tk.CENTER)
        self.tree.column("tags", width=100, anchor=tk.CENTER)

        self.tree.heading("site_name", text='Домен')
        self.tree.heading("url", text='Ссылка на сайт')
        self.tree.heading("date", text='Дата')
        self.tree.heading("tags", text='Теги')

        self.tree.pack()

    def records(self, url):
        print(self.url)
        self.url_split = str(self.url)
        self.site = self.url_split.split("//")[-1].split("/")[0]
        self.page = requests.get(self.url)
        self.tree = html.fromstring(self.page.content)
        self.now = datetime.datetime.now()

        self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'a')
        self.f.write('{}, {}\n'.format(self.url_split, self.now.strftime("%Y-%m-%d %H:%M:%S")))
        self.f.close()

        self.all_elms = self.tree.cssselect('*')
        self.all_tags = [x.tag for x in self.all_elms]
        self.c = Counter(self.all_tags)

        self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'w')
        for e in self.c:
            self.d = "{" + ", ".join(json.dumps('{}: {}'.format(e, self.c[e])) for e in self.c ) + "}"
        self.reg = re.sub(r'\"+(\w+)\: +' r'(\d{1,4})\"', r'"\1": \2', self.d)
        self.f.write(self.reg)
        self.f.close()

        self.db.insert_data(self.site, self.url, self.now)
        self.view_records()


    def view_records(self):
        self.db.c.execute('''SELECT site_name, url, date, tags FROM tags''')
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
        # print(result)
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
        self.c.execute('drop table if exists tags')
        self.c.execute('CREATE TABLE IF NOT EXISTS tags (site_name varchar, url varchar, date timestamp, pickled_tags text, tags jsonb)')
        self.conn.commit()

    def insert_data(self, site, url, date):
        self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'r')
        self.data = self.f.read()
        self.values = [self.site, self.url, self.date, dumps(self.data), self.data]
        self.c.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, self.values))))
        self.conn.commit()
        self.f.close()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Информация по тегам")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()