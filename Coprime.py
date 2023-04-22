# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:13:43 2023

@author: Haryish Elangumaran
"""


def coprimenumber(a, b):
  x = set(factors(a))
  y = set(factors(b))
  hcf = x.intersection(y)
  print(a, b, hcf)
  if hcf == {1}:
    print('{} and {} are coprime'.format(a, b))
  else:
    print('{} and {} are not coprime'.format(a, b))


def factors(number):
  factor = [1]
  for j in range(2, number + 1):
    if number % j == 0:
      factor.append(j)
  return factor

print("As Per code,")
coprimenumber(14,15)
