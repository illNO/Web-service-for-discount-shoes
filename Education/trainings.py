# import numpy as np
from datetime import date

# dictionary = {'key' : 'value', 'key1': 'value1'}
# print(dictionary.values())
#
# string = 'this is a string'
# print(string[1:5])
#
# for i in range(5):
#    if i%2 == 0:
#       print(i)
#    else:
#       pass
#
# for i in range(5):
#    if i%2 == 0:
#       print(i)
#
# #map function example
# def number_exponential(num):
#    return num**2
# number_list = [2,3,4,5]
# print(list(map(number_exponential, number_list)))

# list_example = [1,2,3,4,5]
# #Iniating Deep copy with .copy attribute
# another_list = list_example.copy()
# another_list[0] = 100
# print(list_example)
# print(another_list)

# list_example = ['apple', 'grape', 'orange']
# print(' '.join(list_example))

# #Example membership operators
# print('me' in 'membership')
# print('mes' not in 'membership')

# print(list(zip([1, 2, 3], ['apple', 'grape', 'orange'], ['x', 2, True])))
# for num, fruit, thing in zip([1, 2, 3], ['apple', 'grape', 'orange'], ['x', 2, True]):
#     print(num)
#     print(fruit)
#     print(thing)

# for i in range(1,5):
#    print(i)
# for i in range(1, 10, 2):
#    print(i)

# a = np.array([i for i in range(100)])
# p = np.percentile(a, 50) #Returns 50th percentile, e.g. median
# print(p)


# a = '1'
# b = '2'
# c = '3'
# s = a + '[' + b + ':' + c + ']'
# print(s)
#
# import sys
# print(sys.version)

# def star_triangle(r):
#    for x in range(r):
#       print(' '*(r-x-1)+'*'*(2*x+1))
# star_triangle(4)

# a = input()
# print(a == a[::-1])

#
# def squares(n):
#     i = 1
#     while(i<=n):
#         yield i**2
#         i+=1
#
#
# for i in squares(7):
#     print(i)

# def f(x, l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)

# str = 'abc'
# str1 = str
# str1 += 'a'
# print(id(str))
# print(id(str1))
#
# zoo = 'max', 'igor'
# print(zoo)
# print(type(zoo))
# print(1,2,3)
# print((1, 2, 3))


# ab = { 'Swaroop' : 'swaroop@swaroopch.com',
# 'Larry' : 'larry@wall.org',
# 'Matsumoto' : 'matz@ruby-lang.org',
# 'Spammer' : 'spammer@hotmail.com'
# }
# ab['igor'] = 'igor@gmail.com'
# for name, address in ab.items():
#     print(name, address)

# bri = set(['Бразилия', 'Россия', 'Индия'])
# bri.add('Индия')
# print(bri)
#
# mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
# print(' '.join(mylist))

# x = 20


# def func(name, age=18, gender='male'):
#     print('Name is: {}, age is: {}, gender is: {}'.format(name, age, gender))
#     # global x
#     # print('x равно', x)
#     # x = 2
#     # print('Заменяем глобальное значение x на', x)
# # print('Значение x составляет', x)
#
#
# func('Igor')
# func('Oksana', 25, 'female')
# func('Nastya', gender='female')


# def total(initial=5, *numbers, **keywords):
#     '''Total
#     Variable number of Arguments'''
#     count = initial
#     for number in numbers:
#         count += number
#     for key in keywords:
#         count += keywords[key]
#     print(keywords)
#     print(numbers)
#     return count
#
#
# total(10, 1, 2, 3, vegetables=50, fruits=100, shit=20)
# print(total.__doc__)


# def someFunction(a=1, b=0):
#     '''Every function returns None
#     if we dont write our own return'''
#     print(1)
#
#
# print(someFunction())
# print(someFunction.__doc__)


# def printMax(x, y):
#     '''Выводит максимальное из двух чисел.
#     Оба значения должны быть целыми числами.'''
#     x = int(x) # конвертируем в целые, если возможно
#     y = int(y)
#     if x > y:
#         print(x, 'наибольшее')
#     else:
#         print(y, 'наибольшее')
# printMax(3, 5)
# print(printMax.__doc__)

# import sys
# print('Аргументы командной строки:')
# for i in sys.argv:
#     print(i)
# print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')


# import my_module
# my_module.func()
#
# import this
# print(my_module.a)
# print(my_module.__version__)
# print(dir(my_module))
# print(dir())
# print(not this)


"""List"""
# shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
# print('Я должен сделать ', len(shoplist), 'покупок.')
# print('Покупки:', end=' ')
# for item in shoplist:
#     print(item, end=', ')
#
# print(help(int))


'''Set'''
# a = {1, 2, 3, 1}
# print(a)


'''Classes'''

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def sayHi(self):
#         print('Привет! Меня зовут', self.name)
#
#
# p = Person('Swaroop')
# p.sayHi()
# # Этот короткий пример можно также записать как Person('Swaroop').sayHi()
#
#
# class Car:
#     def __init__(self, brand, year, odometer=0):
#         self.brand = brand
#         self.year = year
#         self.odometer = odometer
#
#     def drive(self, miles):
#         self.odometer += miles
#
#
# tucson=Car('Hyundai', 2007, 10000)
# tucson.drive(500)
# print(tucson.odometer)
#
#
# class Robot:
#     '''Представляет робота с именем.'''
#     # Переменная класса, содержащая количество роботов
#     population = 0
#     def __init__(self, name):
#         '''Инициализация данных.'''
#         self.name = name
#         print('(Инициализация {0})'.format(self.name))
#         # При создании этой личности, робот добавляется
#         # к переменной 'population'
#         Robot.population += 1
#
#     def __del__(self):
#         '''Я умираю.'''
#         print('{0} уничтожается!'.format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print('{0} был последним.'.format(self.name))
#         else:
#             print('Осталось {0:d} работающих роботов.'.format(Robot.population))
#
#     def sayHi(self):
#         '''Приветствие робота.
#         Да, они это могут.'''
#         print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
#
#     @staticmethod
#     def howMany():
#         '''Выводит численность роботов.'''
#         print('У нас {0:d} роботов.'.format(Robot.population))
#
#     # howMany = staticmethod(howMany)
#
#
# droid1 = Robot('R2-D2')
# droid1.sayHi()
# Robot.howMany()
#
# droid2 = Robot('C-3PO')
# droid2.sayHi()
# Robot.howMany()
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("Роботы закончили свою работу. Давайте уничтожим их.")
# del droid1
# del droid2
# Robot.howMany()

# Method of class. Decorator: @classmethod
# dct = dict.fromkeys('AEIOU')  # <- вызывается при помощи класса dict
# dct['A'] = 'Igor'
# print(dct)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # self.age = date.today().year-age
#
#     @classmethod
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#
#
# person1 = Person('Sarah', 25)
# person2 = Person.from_birth_year('Roark', 1994)
# print(person1.name, person1.age)
# print(person2.name, person2.age)
# print(Person.is_adult(25))

'''
There are three types of methods 
1 - Instance method. Requires self in the scopes. Belongs to instance, can change only instance. 
2 - Class method. Decorator - classmethod. Requires cls in the scopes. Belongs to class, can change only class. 
3 - Static method. Decorator - @staticmethod. Nothing is required in the scopes. Can change neither class, nor it`s instance. 
'''

# class SchoolMember:
#     '''Представляет любого человека в школе.'''
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Создан SchoolMember: {0})'.format(self.name))
#
#     def tell(self):
#         '''Вывести информацию.'''
#         print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
#
#
# class Teacher(SchoolMember):
#     '''Представляет преподавателя.'''
#
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('(Создан Teacher: {0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Зарплата: "{0:d}"'.format(self.salary))
#
#
# class Student(SchoolMember):
#     '''Представляет студента.'''
#
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Создан Student: {0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Оценки: "{0:d}"'.format(self.marks))
#
#
# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
# print()  # печатает пустую строку
# members = [t, s]
# for member in members:
#     member.tell()  # работает как для преподавателя, так и для студента


'''Work with files'''
# import pickle
#
# # name of file
# shoplistfile = 'shoplist.data'
#
# shoplist = ['яблоки', 'манго', 'морковь']
#
# # Write data into file
# f = open(shoplistfile, 'wb')
# pickle.dump(shoplist, f)  # put object into file
# f.close()
# del shoplist
# # Read data from file
# f = open(shoplistfile, 'rb')
# stored_list = pickle.load(f)  # load object from file
# print(stored_list)

'''Work with errors'''
# try:
#     text = input('Введите что-нибудь --> ')
# except EOFError:
#     print('Ну зачем вы сделали мне EOF?')
# except KeyboardInterrupt:
#     print('Вы отменили операцию.')
# else:
#     print('Вы ввели {0}'.format(text))
###########################################################


# class ShortInputException(Exception):
#     '''Пользовательский класс исключения.'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
#
# try:
#     text = input('Введите что-нибудь --> ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
# # Здесь может происходить обычная работа
# except EOFError:
#     print('Ну зачем вы сделали мне EOF?')
# except ShortInputException as ex:
#     print('ShortInputException: Длина введённой строки -- {0}; '
#           '\ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
# else:
#     print('Не было исключений. Строка: {}'.format(text))

# hi = '''hello
#     hi
#     hey'''
# f = open('poem.txt', 'w')
# f.write(hi)
# f.close()
# with open("poem.txt") as f:
#     for line in f:
#         print(line, end='')

'''Logging
    Треба розібратись'''

# import os, platform, logging
# if platform.platform().startswith('Windows'):
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
#                     os.getenv('HOMEPATH'), \
#                     'test.log')
# else:
#     logging_file = os.path.join(os.getenv('HOME'), 'test.log')
# print("Сохраняем лог в", logging_file)
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename = logging_file,
#     filemode = 'w',
# )
# logging.debug("Начало программы")
# logging.info("Какие-то действия")
# logging.warning("Программа умирает")


# def sumaa(a):
#     suma = 0
#     for key in a:
#         suma += a[key]
#     return suma
#
#
# dict = {'a': 10, 'b': 11}
# print(sumaa(dict))
# # print(sum('a', 10, 'b', 11))
#
#
# def display(**name):
#     print(name["fname"] + " " + name["mname"] + " " + name["lname"])
#
#
# # passing dictionary key-value
# # pair as arguments
# display(fname="John",
#         mname="F.",
#         lname="Kennedy")
'''Decorator'''
# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
#
# hello_world()


# def benchmark(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
#
#
# fetch_webpage()


# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#         return return_value
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
#
# webpage = fetch_webpage('https://google.com')
# print(webpage)


# def fibonacci(a):
#     if a < 1:
#         return 0
#     elif a == 1:
#         return 1
#     else:
#         return fibonacci(a-1) + fibonacci(a-2)
#
#
# print(fibonacci(4))

# import random
# print(random.random() * 100)
# print(random.randrange(5, 10))

# import hashlib
#
# # print(hashlib.algorithms_available)
# # print(hashlib.algorithms_guaranteed)
# #
# # hash_object = hashlib.md5(b'Hello World')
# # print(hash_object.hexdigest())
#
# mystring = input('Enter String to hash: ')
#
# # Предположительно по умолчанию UTF-8
# hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())


# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
# s_iter1 = SimpleIterator(3)
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))


# class SimpleIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
#
# s_iter2 = SimpleIterator(5)
# for i in s_iter2:
#     print(i)
# print(s_iter2.__next__())
#
#
# def simple_generator(val):
#    while val > 0:
#        val -= 1
#        yield val
#
# gen_iter = simple_generator(5)
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))


# gen = (el for el in range(1, 5))
# lst = [el*el for el in range(1, 5)]
# print(gen.__next__())
# print(gen.__next__())
# print(lst)


# def gen(r):
#     for i in range(r):
#         yield i**2
#
#
# generator = gen(10)
# print(generator.__next__())
# print(next(generator))
# print(generator.__next__())
# lst = [5, 15, 20, 8]
# print(next(lst))


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)
