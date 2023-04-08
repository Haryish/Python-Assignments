# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:13:43 2023

@author: haryi
"""

def coprime(x,y):
    if len(set(factors(x)) & set(factors(y))) == 0:
        print('{} and {} are coprime'.format(x,y))
    else:
        print('{} and {} are not coprime'.format(x,y))
def factors(i):
    fac = []
    for j in range(2,i+1):
        if i%j == 0:
            fac.append(j)
    return fac


#eg
coprime(17,15)
coprime(10,8)