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

# print(d)

# import re
# s = "Example String"
# replaced = re.sub('[ES]', 'a', s)
# article = re.sub(r'(?is)</html>.+', '</html>', article)
# print (replaced)
# print (article) 

from tkinter import *
 
root = Tk()
 
e = Entry(width=20)
b = Button(text="Преобразовать")
l = Label(bg='black', fg='white', width=20)
 
def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)
 
b.bind('<Button-1>', strToSortlist)
 
e.pack()
b.pack()
l.pack()
root.mainloop()