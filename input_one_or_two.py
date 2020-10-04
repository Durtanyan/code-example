# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:56:29 2020
@author: lukin
Проверка вводимых данных с обработкой ошибок. Вводиться должно только число
1 или 2. Все остальное отсекается и обрабатывается, до тех пор, пока не будут 
введены нужные значения
"""
print('####################################################')
print(__doc__)

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

#ТОЖЕ САМОЕ, НО ПОВТОРЯЮЩИЙСЯ КОД ВЫДЕЛЕН В ФУНКЦИЮ error_handling()
print('########################################################')
print('ТОЖЕ САМОЕ, НО ПОВТОРЯЮЩИЙСЯ КОД ВЫДЕЛЕН В ФУНКЦИЮ error_handling()')
def error_handling(number):
    while not(type(number) == int and (number == 1 or number == 2)):
            number = input('Enter number: ')
            if number != 1 or number != 2:
                try:
                    number = int(number)
                except:
                    print('Введите не строку, а число, но не меньше 1 и не больше 2.')
    print(number)
    

number = input('Введите число: ')
try:
    number = int(number)
    if number != 1 or number != 2:
        error_handling(number)
except ValueError:
    error_handling(number)

#ТОЖЕ САМОЕ, НО ВСЕ РЕАЛИЗОВАНО НА ФУНКЦИЯХ    
print('########################################################')
print('ТОЖЕ САМОЕ, НО ВСЕ РЕАЛИЗОВАНО НА ФУНКЦИЯХ')

def checking_for_a_number():
    number = input('Введите число: ')
    while type(number) != int:
        try:
            number = int(number)
        except ValueError:
            print('Вы ввели строку, а надо число: ')
            number = input('Введите число, пожалуйста: ')
    return number


def number_one_or_two():
    number = checking_for_a_number()
    while number != 1 or number != 2:
        if number == 1 or number == 2:
            return number
        else:
            print('Введите число 1 или 2: ')
            number = checking_for_a_number()
            
            
print(number_one_or_two())
