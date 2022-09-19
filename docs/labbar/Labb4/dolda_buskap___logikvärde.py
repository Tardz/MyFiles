# -*- coding: utf-8 -*-
### UPPGIFT 4A ###
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
flattened_expression = []

def flatlist(expression):
    for internal_list in expression:
        if type(internal_list) == list:
            flatlist(internal_list)
        else:
            flattened_expression.append(internal_list)
    return flattened_expression


def NOT(simplified_flattened_expression):
    index = 0
    NOT_counter = 0
    final_expression = []
    
    for value in simplified_flattened_expression:
        index += 1
        if "NOT" == value:
            NOT_counter += 1  
            print(NOT_counter)
            if simplified_flattened_expression[index] != "NOT":
                if simplified_flattened_expression[index] == "true":
                    if NOT_counter % 2 != 0:
                        final_expression.append("false")
                        simplified_flattened_expression.remove(simplified_flattened_expression[index])
                        NOT_counter = 0
                    else:
                        NOT_counter = 0
                elif simplified_flattened_expression[index] == "false":
                    if NOT_counter % 2 != 0:
                        final_expression.append("true")
                        simplified_flattened_expression.remove(simplified_flattened_expression[index])
                        NOT_counter = 0
                    else:  
                        NOT_counter = 0
            elif simplified_flattened_expression[index] == "NOT":
                continue
        else:
            final_expression.append(value)   

    print(final_expression)
    return final_expression

def boolean_value(expression):
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
    simplified_flattened_expression = []
    
    if type(expression) != list:
        flattened_expression = [expression]
    else:
        flattened_expression = flatlist(expression)

    print(flattened_expression)

    for value in flattened_expression:
        if value in interpretation:
            simplified_flattened_expression.append(interpretation[value])
        elif value in "ANDOR":
            simplified_flattened_expression.append(value)
        else:
            simplified_flattened_expression.append(value)
    
    print(simplified_flattened_expression)
    
    if "NOT" in simplified_flattened_expression:
        final_expression = NOT(simplified_flattened_expression)
    else:
        final_expression = simplified_flattened_expression
    
    print(boolean_value(final_expression))
    return boolean_value(final_expression)
   

interpret(["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],
               {"cat_asleep": "false"})


print(1)