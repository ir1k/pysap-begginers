# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:44:20 2017

@author: leno
"""

def is_leapyear(year):
    """check whether year is leap year or not"""
    if year % 400 == 0:
        return True
    elif (year % 100 != 0) and (year % 4 == 0):
        return True
    else:
        return False

def leapyear(this_year, width):
    """show leap years"""
    result = []
    for year in range(this_year, this_year + width):
        if is_leapyear(year):
            result.append(year)

    return result

def run():
    """entry point of this program"""
    this_year = 2017
    width = 400
    for year in leapyear(this_year, width):
        print(year)

run()
