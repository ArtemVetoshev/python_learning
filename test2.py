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
#   for e in c:
#       fileW.write('{}: {}\n'.format(e, c[e]))
# fileW = open('C:/Users/Артём/Desktop/py2.txt', 'r')
# with open('C:/Users/Артём/Desktop/pickle.txt', 'wb') as fileWb:
#   pickle.dump(fileW.readlines(), fileWb)
# # with open('C:/Users/Артём/Desktop/py2.txt', 'wb') as file:
# #     for e in c:
# #         pickle.dump('{}: {}'.format(e, c[e]), file)

# with open('C:/Users/Артём/Desktop/pickle.txt', 'rb') as file:
#   data_new = pickle.load(file)
#   print(data_new)

# Readme = open('C:/Users/Артём/Desktop/Readme.txt', 'r')
# with open('C:/Users/Артём/Desktop/readme2.txt', 'wb') as file:
#   pickle.dump(Readme.read(), file)


# with open('C:/Users/Артём/Desktop/readme2.txt', 'rb') as f:
#   data_new = pickle.load(f)
#   print(data_new)





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
#   data_new = pickle.load(f)
#   print(data_new)




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

        self.add_img = tk.PhotoImage(file="C:/Users/Артём/Desktop/add.png")
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'),
                                 height=15, show='headings')
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("description", width=365, anchor=tk.CENTER)
        self.tree.column("costs", width=150, anchor=tk.CENTER)
        self.tree.column("total", width=100, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("description", text='Наименование')
        self.tree.heading("costs", text='Статья дохода/расхода')
        self.tree.heading("total", text='Сумма')

        self.tree.pack()

    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()


    def view_records(self):
        self.db.c.execute('''SELECT * FROM finance''')
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
        self.title('Добавить доходы/расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Сайт:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Сумма:')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        result = []
        with open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'r') as f:
            for row in f:
                result.append(row.split(',')[0])
        result = list(set(result))
        # print(result)
        self.combobox = ttk.Combobox(self, values=result)
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                  self.entry_money.get(),
                                                                  self.combobox.get()))

        self.grab_set()
        self.focus_set()

class DB:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='root', host='localhost', port='5432')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)''')
        self.conn.commit()

    def insert_data(self, description, costs, total):
        self.values = [description, costs, total]
        self.c.execute(sql.SQL('INSERT INTO finance VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, self.values))))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Домашние финансы")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()