# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:56:29 2020

@author: lukin
"""
"""
Проверка вводимых данных с обработкой ошибок. Вводиться должно только число
1 или 2. Все остальное отсекается и обрабатывается, до тех пор, пока не будут 
введены нужные значения
"""

number = input('Введите число: ')
try:
    number = int(number)
    if number != 1 or number != 2:
        while not(type(number) == int and (number == 1 or number == 2)):
            number = input('Enter number: ')
            if number != 1 or number != 2:
                try:
                    number = int(number)
                except:
                    print('Введите не строку, а число, но не меньше 1 и не больше 2.')
        print(number)
except ValueError:
    while not(type(number) == int and (number == 1 or number == 2)):
        number = input('Enter number: ')
        if number != 1 or number != 2:
            try:
                number = int(number)
            except:
                print('Введите не строку, а число, но не меньше 1 и не больше 2.')
    print(number)
