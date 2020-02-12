import requests
import datetime
from pickle import dumps, load
import tkinter as tk
from lxml import html
from collections import Counter
import psycopg2
from psycopg2 import sql
import json
import re

conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='root', host='localhost', port='5432')
cur = conn.cursor()
conn.autocommit = True

cur.execute('drop table tags')
cur.execute('CREATE TABLE IF NOT EXISTS tags (site_name varchar, url varchar, date timestamp, pickled_tags text, tags text)')


url = ('https://python-scripts.com/question/3322')
site = url.split("//")[-1].split("/")[0]
page = requests.get(url)
tree = html.fromstring(page.content)
now = datetime.datetime.now()

# '{"bar": "baz", "balance": 7.77, "active":false}'
f = open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'a')
f.write('{}: {}'.format(site, now.strftime("%Y-%m-%d %H:%M:%S")))
f.close()

 
all_elms = tree.cssselect('*')
all_tags = [x.tag for x in all_elms]
c = Counter(all_tags)


f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'w')
for e in c:
	d = "{\n" + ",\n".join(json.dumps('{}: {}'.format(e, c[e])) for e in c ) + "\n}"
	# "[\n" + json.dump('{}: {}'.format(e, c[e]), f, separators=(': ', ', ')) + "\n]"
	# json.dump((e, c[e]), f, sort_keys=True, separators=(': ', ', '))
# f.write(d)
# replaced = re.sub('[ES]', 'a', s)
reg = re.sub('"[a-z]: [0-9]"', '"[a-z]": [0-9]', d)
print(type(d))
print(reg)
f.close()
# with open("out", "w") as outfile:
#   outfile.write(dump)

# f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'w')
# for e in c:
# 	f.write('{}: {}'.format(e, c[e]))
# f.close()

f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'r')
data = f.read()
print(data)
values = [site, url, now.strftime("%Y-%m-%d %H:%M:%S"), dumps(data), data]
cur.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, values))))
# cur.execute("INSERT INTO tags VALUES ('{}', '{}', '{}', $${}$$)".format(site, url, now.strftime("%Y-%m-%d %H:%M:%S"), dumps(data)))

f.close()


dicti = cur.execute('select site_name, url, date, tags from tags')
records = cur.fetchall()

print(type(records))

for row in records:
	tag = [row[3]]
	print('site:', row[0])
	print('url:', row[1])
	print('data:', row[2])
	# t = loads(bytes(row[3], encoding='utf8'))
	# print(type(t))
	print('tags:', row[3])
	print(tag)
# print(cur.fetchone())
conn.close()




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


# file = open('C:\\Users\\Artem_Vetoshev\\Desktop\\test.txt', 'r')
# fileStreams = open('test2.txt', 'w')
# array = file.readlines()
# target = '''    - column:
#         name: %s
#         type: %s

# '''
# for i in range(0, len(array)):
#     nameStr = array[i].strip().split(' ')[0]
#     typeStr = array[i].strip().split(' ')[1]
#     print(nameStr)
#     fileStreams.write(target % (nameStr, typeStr))
# file.close()
# fileStreams.close()