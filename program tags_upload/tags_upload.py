import os
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

# создаю класс Main с аргументом Frame(контейнер для организации объектов и виджетов внутри окна)
# создаю конструктор класса и передаю ему 2 аргумента (экземпляр класса и корневое окно программы)
# метод super() отыскивает базовый класс класса Main и возвращает его, а дальше идет обращение к методу __init__ найденного класса (в него, в свою очередь, передаем аргумент root)
# далее вызываем функции
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db # созданный экземпляр класса DB подаем в конструктор класса Main
        self.view_records()

# создаю функцию для инициализации объектов графического интерфейса
    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2) # устанавливаю цвет фона и границу
        toolbar.pack(side=tk.TOP, fill=tk.X) # располагаю тулбар вверху и растягиваю по горизонтали

        self.add_button1 = tk.PhotoImage(file="C:/Users/artem_vetoshev/Desktop/python_learning/b1.png") # передаю изображения для дальнейшего использования в кнопках
        self.add_button2 = tk.PhotoImage(file="C:/Users/artem_vetoshev/Desktop/python_learning/b2.png")
        self.add_button3 = tk.PhotoImage(file="C:/Users/artem_vetoshev/Desktop/python_learning/b3.png")

        # располагаю кнопку, которая будет открывать второе окно (команда на вызов функции open_dialog); указываю доп. параметры для кнопки
        btn_open_dialog = tk.Button(toolbar, text='Запросить данные по сайту', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_button1)
        btn_open_dialog.pack(side=tk.LEFT)

        # кнопка для открытия файла с историей обращений к сайтам
        btn_open_history = tk.Button(toolbar, text='История обращения к сайтам', command=self.open_history, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_button2)
        btn_open_history.pack(side=tk.RIGHT)

        # кнопка для открытия файла со списком тегов последнего запрошенного сайта
        btn_open_tags = tk.Button(toolbar, text='Список тегов последнего запрошенного сайта', command=self.open_tags, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_button3)
        btn_open_tags.pack(anchor=tk.CENTER)

        # создаю виджет, передаю кортеж из колонок
        self.tree = ttk.Treeview(self, columns=('site_name', 'url', 'date', 'tags'),
                                 height=15, show='headings')

        # обращение к колонкам
        self.tree.column("site_name", width=125, anchor=tk.CENTER)
        self.tree.column("url", width=270, anchor=tk.CENTER)
        self.tree.column("date", width=150, anchor=tk.CENTER)
        self.tree.column("tags", width=290, anchor=tk.CENTER)

        # даю названия колонкам
        self.tree.heading("site_name", text='Домен 2го уровня')
        self.tree.heading("url", text='Ссылка на сайт')
        self.tree.heading("date", text='Дата запроса')
        self.tree.heading("tags", text='Теги')

        # применяю метод pack, чтобы виджет отображался в главном окне
        self.tree.pack()

    # функции передается указанная в поле ввода дочернего окна ссылка
    def records(self, url):
        self.url_split = str(url) # передаю переменной ссылку в формате str
        self.site = self.url_split.split("//")[-1].split("/")[0] # разбиваю ссылку по разделителям и получаю домен 2го уровня
        self.now = datetime.datetime.now() # получаю текущую дату в формате timestamp

        self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'a') # открываю файл на дозапись
        self.f.write('{}, {}\n'.format(self.url_split, self.now.strftime("%Y-%m-%d %H:%M:%S"))) # записываю домен и текущую дату
        self.f.close() # закрываю файл

        self.page = requests.get(url) # получаю веб-страницу с помощью метода get
        self.html_tree = html.fromstring(self.page.content) # получаю содержимое сайта
        self.all_elms = self.html_tree.cssselect('*') # выбираю все элементы
        self.all_tags = [x.tag for x in self.all_elms] # получаю теги
        self.c = Counter(self.all_tags) # считаю количество тегов

        # открываю файл на запись
        self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'w')
        for e in self.c:
            self.d = "{" + ", ".join(json.dumps('{}: {}'.format(e, self.c[e])) for e in self.c ) + "}" # привожу данные к формату {"tag1: 4", "tag2: 10"}
        # т.к. формат выше не воспринимается постгресом как jsonb, не нашел ничего лучше, как привести его немного к другому формату с помощью регулярных выражений
        self.reg = re.sub(r'\"+(\S+)\: +' r'(\d{1,4})\"', r'"\1": \2', self.d) # привожу к формату {"tag1": 4, "tag2": 10}
        self.f.write(self.reg) # записываю теги в формате jsonb в файл
        self.f.close() # закрываю файл

        self.db.insert_data(self.site, str(url), self.now) # вызываю функцию для добавления данных в базу и передаю 3 аргумента
        self.view_records() # вызываю функцию для отоюбражения данных в виджете

    # функция для отображения данных из базы данных в виджете основного окна
    def view_records(self):
        self.db.c.execute('''SELECT site, url, date, tags FROM tags''') # извлекаем данные
        [self.tree.delete(i) for i in self.tree.get_children()] # реализую очистку содержимого виджета, чтобы данные отображались в соответствии с данными в базе
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()] # отображаю содержимое базы в виджете с помощью генератора списка
                                                                                # в цикле с помощью метода fetchall() возвращается список кортежей (последовательностей строк)

    # функция для вызова класса Child()
    def open_dialog(self):
        Child()

    # функция для открытия файла с историей обращений к сайтам
    def open_history(self):
        os.startfile('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt')

    # функция для открытия файла со списком тегов последнего запрошенного сайта
    def open_tags(self):
        os.startfile('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt')

# класс для дочернего окна
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app # передаем класс Main в класс Child, т.к. функция records содержится в классе Main, а вызывается она из класса Child

    # функция для инициализации объектов графического интерфейса в дочернем окне
    def init_child(self):
        self.title('Загрузка тегов')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        # создание и расположение надписи "Сайт:"
        label_select = tk.Label(self, text='Сайт:')
        label_select.place(x=50, y=30)

        # создаю пустой список, открываю файл на чтение
        # запускаю цикл по строчкам файла и добавляю в список result элемент с индексом 0 (ссылки на сайты), определяя его по разделителю ','
        result = []
        with open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'r') as f:
            for row in f:
                result.append(row.split(',')[0])
        result = list(set(result)) # т.к. требуются уникальные ссылки, преобразую список в множество
        self.url = ttk.Combobox(self, values=result) # передаю в выпадающий список (виджет combobox) элементы множества

        # не стал указывать элемент в выпадающем списке, который отображался бы по умолчанию, поскольку возникает ошибка, если файл с данными пуст
        # self.url.current(0)
        self.url.place(x=120, y=30, width=250)

        # кнопка для закрытия дочернего окна
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        # кнопка для передачи записи функции records
        btn_add = ttk.Button(self, text='Добавить')
        btn_add.place(x=220, y=170)
        btn_add.bind('<Button-1>', lambda event: self.view.records(self.url.get()))

        self.grab_set() # метод перехватывает все события, происходящие в приложении
        self.focus_set() # метод для захвата и удерживания фокуса

# класс для инициализации подключения к СУБД PostgreSQL и создания таблицы
class DB:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='root', host='localhost', port='5432')
        self.c = self.conn.cursor()
        # self.c.execute('drop table if exists tags')
        self.c.execute('CREATE TABLE IF NOT EXISTS tags (site varchar, url varchar, date timestamp, pickled_tags text, tags jsonb)')
        self.conn.commit()

# функция для добавления данных в таблицу базы данных
# на вход подаются название сайта (домен), ссылка на сайт и дата в формате timestamp
    def insert_data(self, site, url, date):
        self.f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'r') #для добавления списка тегов в таблицу, открываем файл с ними
        data = self.f.read() # читаем файл и передаем в переменную
        self.values = [site, url, date, dumps(data), data] # создаем список со значениями и передаем туда данные
        self.c.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, self.values)))) #добавляем данные в таблицу базы данных
        self.conn.commit() # коммит
        self.f.close() # закрываем файл

# если скрипт запущен как осн программа, то ее содержание выполнится
if __name__ == "__main__":
    root = tk.Tk() # создаем корневое окно программы
    db = DB() # создаем экземпляр класса DB
    app = Main(root) # т.к. мы наследовались от объекта библиотеки tkinter Frame, и для того чтобы отображать содержимое окна, нам надо его упаковать с помощью метода pack
    app.pack() # применяем метод pack и упаковываем
    root.title("Информация по тегам") # название окна
    root.geometry("850x400+300+200") # размер окна и точка на экране, где она будет появляться
    root.resizable(False, False) # не изменяемый размер окна по горизонтали и вертикали
    root.mainloop() # метод для отображения окна