# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:09:57 2020

@author: lukin
"""

"""
Вам дана строка, состоящая из букв x и y, например xyxxxyxyy. Кроме того, у вас есть операция под названием flip, которая изменяет одиночный x на y или наоборот.

Определите, сколько раз вам нужно будет применить эту операцию, чтобы гарантировать, что все x предшествуют всем y. В предыдущем примере достаточно перевернуть второй и шестой символы, поэтому вы должны вернуть 2.

Начало:
def get_flip_count(string):
    # Ваше решение тут

# Тесты
assert get_flip_count("xyxxxyxyy") == 2
"""
def get_flip_count(string):
    count = 0
    for i in range(len(string)):
    	if string[0] == i - 1 and string[0] == "x" and string[i] == "y":
    		count += 1
    	else:
    		if string[i - 2] != "x" and string[i - 1] == "x" and string[i] == "y":
    			count += 1
    return count
    	
assert get_flip_count("xyxxxyxyy") == 2, f"Не верный результат.\
 Результат должен быть равен {get_flip_count('xyxxxyxyy')}"
