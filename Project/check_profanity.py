#-*- coding:utf-8 -*-
import urllib.request

letter = open('./letter.txt')
letter_str = letter.read()
letter.close()
print(letter_str)

connection = urllib.request.urlopen(
    'https://activity.lagou.com/activityapi/basic/ifLogin')
data = connection.read()
connection.close()
print(data.decode("utf8"))
















