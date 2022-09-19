# -*- coding: utf-8 -*-
from budskap import *

alphabet_lower_case = "abcdefghijklmnopqrstuvwxyzåäö"
alphabet_upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

def split_it(str):
    split_it_str = ""
    split_rec_str = ""
    
    for letter in str:
        if letter in alphabet_lower_case:
            split_it_str += letter
        elif letter in "_.":
            split_it_str += letter 
        elif letter in alphabet_upper_case:
            split_rec_str += letter
        elif letter in " |":
            split_rec_str += letter

    new_str = (split_it_str, split_rec_str)
    return new_str

def split_rec(str):
    str_1 = split_it(str)[0]
    str_2 = split_it(str)[1]

    return str_1, str_2




