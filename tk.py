import tkinter as tk
from tkinter import ttk

# class Main(tk.Frame): #Frame - контейнер, служащий для организации объектов и виджетов внутри окна
# 	def __init__(self, root): #создаем конструктор класса (спец. метод, который автоматически вызывается при создании класса и передает ему 2 аргумента: 1 - текущий экземпляр класса, 2 - корневое окно программы)
# 		super().__init__(root) #возьмем метод __init__ у базового класса frame и передадим в него аргумент root, переданный в init производного класса Main
# 							   #метод super отыскивает базовый класс класса main и возвращает его, а дальше идет обращение к методу init этого найденного класса.
# 							   #польза в том, что при изменении родительского класса не придется изменять содержимое метода, а также дает возможность корректно использовать класс в наследовании
# 		self.init_main() #вызываем функцию

class Main(tk.Frame): 
	def __init__(self, root): 
		super().__init__(root) 
							   
							   
		self.init_main()

	def init_main(self):
		toolbar = tk.Frame(bg='#d7d8e0', bd=2) #устанавливаем цвет фона и границу
		toolbar.pack(side=tk.TOP, fill=tk.X) #располагаем тулбар вверху и растягиваем по горизонтали

		self.add_img = tk.PhotoImage(file='C:/Users/Артём/Desktop/add.png')
		btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
									compound=tk.TOP, image=self.add_img)
		btn_open_dialog.pack(side=tk.LEFT)

		self.tree = ttk.Treeview(self, columns=('id', 'description', 'costs', 'total'), height=15, show='headings')
		#добавляем виджет на главное окно программы
		self.tree.column('ID', width=30, anchor=tk.CENTER) #передаем параметры колонке ID
		self.tree.column('description', width=30, anchor=tk.CENTER)
		self.tree.column('costs', width=30, anchor=tk.CENTER)
		self.tree.column('total', width=30, anchor=tk.CENTER)

		self.tree.heading('ID', text='ID')
		self.tree.heading('description', text='Наименование')
		self.tree.heading('costs', text='Статья дохода/расхода')
		self.tree.heading('total', text='Сумма')

		self.tree.pack() #чтобы виджет отображался в главном окне, применяем метод pack

	def open_dialog(self):
		Child()
#для создания дочернего окна наследуемся от объекта Toplevel
#(окно верхнего уровня, которое служит для создания многооконных программ и дочерних окон)
class Child(tk.Toplevel):
	def __init__(self): # создаем конструктор класса
		super().__init__(root) #прописываем метод супер
		self.init_child()

#функция для инициализации объектов и виджетов дочернего окна
	def init_child(self):
		self.title('Добавить доходы/расходы')
		self.geometry('400x220+400+300') #окно 400 на 220, окно будет отображать в координатах 400 и 300
		self.resizable(False, False)

		label_description = ttk.Label(self, text='Наименование:')
		label_description.place(x=50, y=50)

		label_select = ttk.Label(self, text='Статья дохода/расхода:')
		label_select.place(x=50, y=80)
		
		label_sum = ttk.Label(self, text='Сумма:')
		label_sum.place(x=50, y=110)
		
		self.entry_description = ttk.Entry(self)
		self.entry_description.place(x=200, y=50)

		self.entry_money = ttk.Entry(self)
		self.entry_money.place(x=200, y=110)

		self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
		self.combobox.current(0)
		self.combobox.place(x=200, y=80)

		btn_cancel = ttk.Button(self, text='Закрыть', command = self.destroy)
		btn_cancel.place(x=300, y=80)

		btn_add = ttk.Button(self, text='Добавить')
		btn_add.place(x=220, y=170)
		btn_add.bind('<Button-1>') #чтобы срабатывала по нажатию левой кнопки мыши

		self.grab_set() #этот метод перехватывает события в приложении
		self.focus_set() #захватывает и удерживает фокус


#если скрипт запущен как осн программа, то ее содержание выполнится
#если импортируется, то не пойдет на выполнение
if __name__== "__main__":
	root = tk.Tk() #создаем корневое окно программы
	app = Main(root) #т.к. мы наследовались от объекта библиотеки tkinter Frame,и для того чтобы отображать содержимое окна, нам надо его упаковать с помощью метода pack
	app.pack() #применяем метод pack и упаковываем
	root.title("Tags count") #название окна
	root.geometry("650x450+300+200") #размер окна и точку на экране, где она будет появляться
	root.resizable(False, False) #не изменяемый размер окна по горизонтали и вертикали
	root.mainloop() #метод для отображения вероятно