# -*- coding: utf-8 -*-
from test_strings import *

Angelicas_str = "5237iDHUWDJA378lASG6TDo62734BvHD)/(%WeSJDKyDAKLD8723oJHJD7uHJDSK"

alphabet_lower_case_and_dot = "abcdefghijklmnopqrstuvwxyzåäö_."
alphabet_upper_case_and_pipe = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ| "

### UPPGIFT 4A ###  
def split_rec(str, lower = "", upper = ""):
    if not str:
        return lower, upper
    elif str[0] in alphabet_lower_case_and_dot:
        lower = lower + str[0]
        return split_rec(str[1:], lower, upper)
    elif str[0] in alphabet_upper_case_and_pipe:
        upper += str[0]
        return split_rec(str[1:], lower, upper)
    else:
        return split_rec(str[1:], lower, upper)

def split_it(str):
    index = 1
    lower = ""
    upper = ""

    for character in str:
        if character in alphabet_lower_case_and_dot:
            lower += character
            index += 1
        elif character in alphabet_upper_case_and_pipe:
            upper += character
            index += 1

    return lower, upper

### UPPGIFT 4B ###  
def converter(expression, interpretation):
    index = -1
    for element in expression:
        index += 1
        if type(element) == list:
            converter(element, interpretation)
        elif element in interpretation:
            expression[index] = interpretation[element]

    return expression

def not_replacer(converted_expression, counter, replaced_expression = []):
    for element in converted_expression:
        if element == "NOT":
            counter += 1
            ##print(counter)
        elif type(element) == list:
            not_replacer(element, counter)
        elif element == "false":
            if counter%2 == 0:
                replaced_expression.append("false")
            else:
                replaced_expression.append("true")
        elif element == "true":
            if counter%2 == 0:
                replaced_expression.append("true")
            else:
                replaced_expression.append("false")
        else:
            replaced_expression.append(element)
    
    return replaced_expression

def boolean_converter(final_expression):
    result = ""
    if "OR" in final_expression:
        if "true" in final_expression:
            return result + "true"
    elif "AND" in final_expression:
        if "false" in final_expression:
            return result + "false"
        else:
            return result + "true"
    else:
        return False
    
    return result

def interpret(expression, interpretation):
    expression_cp = list(expression)
    interpretation_cp = dict(interpretation)

    if type(expression) == list:
        final_expression = not_replacer(converter(expression_cp, interpretation_cp), 0)
    else:
        final_expression = interpretation[expression]
    
    return boolean_converter(final_expression)

print(interpret(ex1, int1))
#print(interpret(ex2, int2))
#print(interpret(ex3, int3))
#print(interpret(ex4, int4))
#print(interpret(ex5, int5))
#print(interpret(ex6, int6))
#print(interpret(ex7, int7))

#print(interpret(['door_open', 'AND', 'cat_gone'], {'door_open': 'false', 'cat_gone': 'true', 'cat_asleep': 'true'}))



