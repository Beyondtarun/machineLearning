 #functions

# def say_hi(name,last):
#     print('hi, {0} {1}'.format(name,last))
#     print('hi, {1} {0}'.format(name,last))
    
# say_hi('tarun','goyal')

# def defualtfun(name = 'tarun'):
#     print(name)
    
# defualtfun()
# defualtfun('ram')

# def deter(num):
#     if num % 2 == 0:
#         print('{} is even'.format(num))
#     else:
#         print('{} is odd'.format(num))

# numb = int(input('enter number: '))
        
# deter(numb)


# #List
# animals = ['cat','dog']

# print(animals[0])
# print(animals[1])
# print(animals[-1])

# animals.append('tarun')
# print(animals[-1])
# animals.extend(['loda','lassan'])
# print('++++++++++++++++++++++++++++++')
# for i in animals:
#     print(i)
# print(animals)
# animals.insert(2,'baby')
# print(animals)

# print(animals[::-1]) #reverse
# print(animals[-2:]) #last two elements

# horse = 'hores'[1:3]
# print(horse) #string slicing

# #exception handling
# try:
#     lion_index = animals.index('lion')
# except:
#     lion_index = 'not found'

# print(lion_index)

# #loop

# index = 0
# while index < len(animals):
#     print(animals[index])
#     index += 1
    
    
# newList = sorted(animals)
# print(newList)
# animals.sort()
# print("animal list : {}".format(animals))

# print(animals + newList)

# for ani in range(0 , len(animals),2):
#     print(animals[ani])
    
    
#     #dictionaris
# dict1 = {'a' : "139013", 'b':"928920"}

# print(len(dict1))

# for name in dict1:
#     print(dict1[name])

# dict1['c'] = "q9e8q9"

# for name in dict1:
#     print(dict1[name])
    
# #del dict1[key]

# dict2 = {
#     'a' : ['akdks','jbajcj'],
#     'b' : '76r92'
    
# }

# for var in dict2['a']:
#     print(var)
    
# if 'a' in dict2.keys():
#     print("all ok")
    
# for var1, var2 in dict2.items():
#     print("{} : {}".format(var1,var2))

# def highandlow(number):
#     high = max(number)
#     low = min(number)
#     return (high,low)

# lot = [10,2,3,4,23]
# (high, low) = highandlow(lot)
# print('high {}, low {}'.format(high, low))

# file = open('qr.py')
# with open('qr.py') as file:
#     print('current positon ; {}'.format(file.tell()))
#     print(file.read())
#     print('current positon ; {}'.format(file.tell()))
#     print(file.read())
#     file.seek(55)
#     print('current positon ; {}'.format(file.tell()))
#     print(file.read())

# print('file closed ? : {}'.format(file.closed))

# with open('sample.txt') as file:
#     for line in file:
#         print(line.rstrip())
# print(open('tarun.txt').read())     
# with open('tarun.txt','a') as file:
#     file.write(" \r\nsex is my hobby")

# with open('tarun.txt','r') as file2:
#     for line in file2:
#         content = line  
#         print(line.rstrip())  
#         print('----')
#         print(len(content))

# import time
# print(time.asctime())
# print((time.timezone)/3600)

# from time import *
# import time
# # print(dir(time))
# # print(asctime())
# # # sleep(3)
# # print(asctime())
# # print(tzname)
# # print(time_ns())
    
# import datetime as dt
# print(dt.date.today())
# print(dt.time)
# print(dt.datetime.now())
# print(dt.timedelta)
# print(dt.tzinfo)
# now = dt.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# date_str = "2025-05-23"
# parsed_date = dt.datetime.strptime(date_str, "%Y-%m-%d")
# print(parsed_date)
# print(time.ctime())           # Current time
# print(time.ctime(1716460544)) 
# print(time.localtime())  # Returns struct_time (like a tuple)
# data=['a','s','a','d','s','a']
# count_dict={}

# for item in data:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1

# for key, value in count_dict.items():
#     print('key {} occurs {} time'.format(key,value))
    
# for item in count_dict.items():
#     print(item)