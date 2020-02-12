# from pickle import dumps, load


# def store(arg):
#     f = open('C:/Users/Артём/Desktop/file.txt', 'wb')
#     f.write(dumps(arg))
#     f.close()


# def extract():
#     f = open('C:/Users/Артём/Desktop/file.txt', 'rb')
#     result = load(f)
#     f.close()
#     return result


# d0 = {'one': 1, 'two': 2}
# store(d0)
# d1 = extract()
# print(d1)

# import datetime

# now = datetime.datetime.now()

# print ("Текущая дата и время с использованием метода str:")
# print (str(now))
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
import psycopg2
from psycopg2 import sql
import pickle

a = [1, 10, 0, -3, 9]
ab = pickle.dumps(a)
print(ab)
# b'\x80\x03]q\x00(K\x01K\nK\x00J\xfd\xff\xff\xffK\te.'
b = pickle.loads(ab)
print(b)
print(type(b))