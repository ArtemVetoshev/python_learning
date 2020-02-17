import requests
import datetime
from pickle import dumps, load, loads
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
cur.execute('drop table if exists tags')
cur.execute('CREATE TABLE IF NOT EXISTS tags (site_name varchar, url varchar, date timestamp, pickled_tags text, tags jsonb)')

url = ('https://vk.com/im?peers=c144')
site = url.split("//")[-1].split("/")[0]
page = requests.get(url)
tree = html.fromstring(page.content)
now = datetime.datetime.now()

f = open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'a')
f.write('{}, {}\n'.format(url, now.strftime("%Y-%m-%d %H:%M:%S")))
f.close()

all_elms = tree.cssselect('*')
all_tags = [x.tag for x in all_elms]
c = Counter(all_tags)

f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'w')
for e in c:
	d = "{" + ", ".join(json.dumps('{}: {}'.format(e, c[e])) for e in c ) + "}"
reg = re.sub(r'\"+(\w+)\: +' r'(\d{1,4})\"', r'"\1": \2', d)
f.write(reg)
print(reg)
f.close()

f = open('C:/Users/artem_vetoshev/Desktop/python_learning/file.txt', 'r')
data = f.read()
print(data)
values = [site, url, now.strftime("%Y-%m-%d %H:%M:%S"), dumps(data), data]
cur.execute(sql.SQL('INSERT INTO tags VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, values))))
f.close()


pg_data = cur.execute('select site_name, url, date, pickled_tags, tags from tags')
records = cur.fetchall()

for row in records:
	print('site:', row[0])
	print('url:', row[1])
	print('data:', row[2])
	# print('pickled_tags:', row[3])
	print('tags:', row[4])
f.close()
conn.close()


# f = open('C:/Users/Артём/Desktop/python_learning/sites.txt', 'r')
# data = f.readlines()
# for row in data:
# 	kek = row.split(',')[0]
# print(kek)


result = []
with open('C:/Users/artem_vetoshev/Desktop/python_learning/sites.txt', 'r') as f:
	for row in f:
		result.append(row.split(',')[0])
result = list(set(result))
print(result)

# f = open('C:/Users/Артём/Desktop/python_learning/file.txt', 'w')
# for e in c:
# 	f.write('{}: {}'.format(e, c[e]))
# f.close()

# f = open('C:/Users/Артём/Desktop/python_learning/fromdb.txt', 'wb')
# f.write(dumps(reg))
# f.close()

# f = open('C:/Users/Артём/Desktop/python_learning/fromdb.txt', 'rb')
# pickled_tags = load(f)
# print(pickled_tags)