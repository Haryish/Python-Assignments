# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:14:33 2023

@author: haryi
"""

import random

def check_cipher(plain,cipher):
    if len(plain) != len(cipher):
        return False
    
    indices = list(range(len(plain)))
    random.shuffle(indices)
    
    for i,c in enumerate(cipher):
        j=indices[i]
        plain_char = plain[j]
        cipher_char = chr((ord(plain_char) - ord('A') +5) % 26 + ord('A'))
        if c!= cipher_char:
            return False
        
    return True

plain='PYTHON'#input("Enter the Plain Text: ").capitalize()
cipher='TDMSUY'#input("Enter the Random text for Cipher Verification: ").capitalize()
print(check_cipher(plain, cipher))