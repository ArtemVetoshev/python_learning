# #     f = open('C:/Users/Артём/Desktop/file.txt', 'wb')
# #     f.write(dumps(arg))
# #     f.close()

# #     f = open('C:/Users/Артём/Desktop/file.txt', 'rb')
# #     result = load(f)
# #     f.close()
# #     return result

# # d0 = {'one': 1, 'two': 2}
# # store(d0)
# # d1 = extract()
# # print(d1)

# # import psycopg2
# # from psycopg2 import sql
# # import pickle

# # a = [1, 10, 0, -3, 9]
# # ab = pickle.dumps(a)
# # print(ab)
# # b = pickle.loads(ab)
# # print(b)
# # print(type(b))

# import json

# # objects = ['{"bar": "baz", "balance": 7.77, "active":false}']

# # dump = "[\n" + ",\n".join([ "\t" + json.dumps(obj) for obj in objects ]) + "\n]"
# # print(dump)

# # with open("C:/Users/Артём/Desktop/python_learning/out.txt", "w") as outfile:
# #   outfile.write(dump)

# d = ['bar: 1, bar: 2, bar: 3']

# jsonarray = json.dumps(d)

# f = open('file.txt' , 'a') #дозапись в файл
# f = open('C:/Users/Artem_Vetoshev/Desktop/py/file2.txt', 'wb')
# f.write(dumps(data))
# f.close()

# # def extract():
# f = open('C:/Users/Artem_Vetoshev/Desktop/py/file2.txt', 'rb')
# result = load(f)
# print(result)
# f.close()

# d0 = {'one': 1, 'two': 2}
# store(d0)
# d1 = extract()
# print(d1)




# with open('C:/Users/Артём/Desktop/py2.txt', 'w') as fileW:
# 	for e in c:
# 		fileW.write('{}: {}\n'.format(e, c[e]))
# fileW = open('C:/Users/Артём/Desktop/py2.txt', 'r')
# with open('C:/Users/Артём/Desktop/pickle.txt', 'wb') as fileWb:
# 	pickle.dump(fileW.readlines(), fileWb)
# # with open('C:/Users/Артём/Desktop/py2.txt', 'wb') as file:
# # 	for e in c:
# # 		pickle.dump('{}: {}'.format(e, c[e]), file)

# with open('C:/Users/Артём/Desktop/pickle.txt', 'rb') as file:
# 	data_new = pickle.load(file)
# 	print(data_new)

# Readme = open('C:/Users/Артём/Desktop/Readme.txt', 'r')
# with open('C:/Users/Артём/Desktop/readme2.txt', 'wb') as file:
# 	pickle.dump(Readme.read(), file)


# with open('C:/Users/Артём/Desktop/readme2.txt', 'rb') as f:
# 	data_new = pickle.load(f)
# 	print(data_new)





# data = {
#     'a': [1, 2.0, 3, 4+6j],
#     'b': ("character string", b"byte string"),
#     'c': {None, True, False}
# }
# with open('C:/Users/Артём/Desktop/pickle.txt', 'wb') as f:
#     pickle.dump(data, f)



# data = {
#     'a': [1, 2.0, 3, 4+6j],
#     'b': ("character string", b"byte string"),
#     'c': {None, True, False}
# }
# with open('C:/Users/Артём/Desktop/pickle.txt', 'wb') as f:
#     pickle.dump(data, f)

# with open('C:/Users/Артём/Desktop/pickle.txt', 'rb') as f:
# 	data_new = pickle.load(f)
# 	print(data_new)




# from tkinter import *
 
# root = Tk()
 
# e = Entry(width=20)
# b = Button(text="Преобразовать")
# l = Label(bg='black', fg='white', width=20)
 
# def strToSortlist(event):
#     s = e.get()
#     s = s.split()
#     s.sort()
#     l['text'] = ' '.join(s)
 
# b.bind('<Button-1>', strToSortlist)
 
# e.pack()
# b.pack()
# l.pack()
# root.mainloop()


# all_the_same = ()
# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True

# import re

# mac_table = '''
# 100    aabb.cc10.7000    DYNAMIC     Gi0/1
# 200    aabb.cc20.7000    DYNAMIC     Gi0/2
# 300    aabb.cc30.7000    DYNAMIC     Gi0/3
# 100    aabb.cc40.7000    DYNAMIC     Gi0/4
# 500    aabb.cc50.7000    DYNAMIC     Gi0/5
# 200    aabb.cc60.7000    DYNAMIC     Gi0/6
# 300    aabb.cc70.7000    DYNAMIC     Gi0/7
# '''

# print(re.sub(r' *(\d+) +'
#              r'([a-f0-9]+)\.'
#              r'([a-f0-9]+)\.'
#              r'([a-f0-9]+) +\w+ +'
#              r'(\S+)',
#              r'\1 \2:\3:\4 \5',
#              mac_table))

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

        btn_site = ttk.Button(toolbar, text='Получить информацию по сайту:')
        btn_site.bind('<Button-1>', lambda event: self.records(self.url.get()))
        btn_site.pack(side=tk.LEFT)

        # btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
        #                             compound=tk.TOP)
        # btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('site_name', 'url', 'date', 'tags'),
                                 height=15, show='headings')

        result = []
        with open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'r') as f:
            for row in f:
                result.append(row.split(',')[0])
        result = list(set(result))
        self.url = ttk.Combobox(toolbar, values=result)
        self.url.current(0)
        self.url.place(x=200, y=2, width = 300)

        # self.url = ttk.Entry(toolbar)
        # self.url.place(x=200, y=2, width = 300)

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
    	self.url_split = str(self.url)
    	# self.site = self.url_split.split("//")[-1].split("/")[0]
    	self.page = requests.get(self.url)
    	self.tree = html.fromstring(self.page.content)
    	self.now = datetime.datetime.now()

    	self.f = open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'a')
    	self.f.write('{}, {}\n'.format(self.url_split, self.now.strftime("%Y-%m-%d %H:%M:%S")))
    	self.f.close()

    	self.all_elms = self.tree.cssselect('*')
    	self.all_tags = [x.tag for x in self.all_elms]
    	self.c = Counter(self.all_tags)

    	self.f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'w')
    	for e in self.c:
    		self.d = "{" + ", ".join(json.dumps('{}: {}'.format(e, self.c[e])) for e in self.c ) + "}"
    	self.reg = re.sub(r'\"+(\w+)\: +' r'(\d{1,4})\"', r'"\1": \2', self.d)
    	self.f.write(self.reg)
    	self.f.close()

    	self.db.insert_data(site_name, url, now)
    	self.view_records()


    def view_records(self):
        self.db.c.execute('''SELECT site_name, url, date, tags FROM tags''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]



class DB:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='root', host='localhost', port='5432')
        self.c = self.conn.cursor()
        self.c.execute('drop table if exists tags')
        self.c.execute('CREATE TABLE IF NOT EXISTS tags (site_name varchar, url varchar, date timestamp, pickled_tags text, tags jsonb)')
        self.conn.commit()

    def insert_data(self, site, url, date, pickled_tags, tags):
    	self.f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'r')
    	self.data = self.f.read()
    	self.values = [self.site, self.url, self.date, dumps(self.data), self.data]
    	self.c.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, self.values))))
    	self.conn.commit()
    	self.f.close()

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


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Домашние финансы")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()