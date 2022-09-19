# -*- coding: utf-8 -*-
### UPPGIFT 4A ###
from multiprocessing.sharedctypes import Value
from budskap import *

alphabet_lower_case = "abcdefghijklmnopqrstuvwxyzåäö"
alphabet_upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

def split_rec(str):
    str_1 = ""
    str_2 = ""

    for letter in str:
        if letter in "_.":
            str_1 += letter
        elif letter in alphabet_lower_case:
            str_1 += letter
        elif letter in " |":
            str_2 += letter
        elif letter in alphabet_upper_case:
            str_2 += letter

    return (str_1, str_2)

### UPPGIFT 4B ###
def converter(expression, interpretation):
    converter_index = -1
    for element in expression:
        converter_index += 1
        if type(element) == list:
            converter_index = 0
            converter(element, interpretation)             
        elif element in interpretation:
            expression[converter_index] = interpretation[element]

    return expression

NOT_counter = 0
NOT_index = 0
NOT_position = 0
def NOT(converted_expression):
    for element in converted_expression:
        NOT_index += 1
        if "NOT" == element:
            NOT_counter += 1
            if type(converted_expression[NOT_index]) == list:
                NOT_index = 0
                NOT(element)
            elif range(len(element)) == NOT_position: 
                if converted_expression[NOT_index] == "true":
                    if NOT_counter % 2 == 0:
                        converted_expression[NOT_index] == "true"
                    else:
                        converted_expression[NOT_index] == "false"
                elif converted_expression[NOT_index] == "false":
                    if NOT_counter % 2 == 0:
                        converted_expression[NOT_index] == "false"
                    else:
                        converted_expression[NOT_index] == "true"
            
def boolean_element(expression):
    true_or_false = ""

    if "AND" in expression:
        if "false" in expression:
            true_or_false = "false"
        else:
            true_or_false = "true"
    elif "OR" in expression:
        if "false" and "true" in expression:
            true_or_false = "true"
        elif "true" and not "false" in expression:
            true_or_false = "true"
        else:
            true_or_false = "false"
    else:
        if "true" in expression:
            true_or_false = "true"
        else:
            true_or_false = "false"

    return true_or_false
    
def interpret(expression, interpretation):
    converted_expression = converter(expression, interpretation)
    print(converted_expression)
    
   

interpret([["NOT",["NOT", "door_open"]], "AND", "cat_gone"], 
               {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"})


