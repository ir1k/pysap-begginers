# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:18:20 2017

@author: leno
"""

def fizzbuzz_one(num):
    """show fizzbuzz with an argument"""
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

def fizzbuzz(last):
    """do fizzbuzz"""
    result = []
    for i in range(0, last):
        result.append(fizzbuzz_one(i + 1))

    return result

def run():
    """entry point of this program"""
    for i in fizzbuzz(100):
        print(i)

run()
