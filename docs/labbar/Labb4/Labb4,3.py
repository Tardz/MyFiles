### UPPGIFT 4B ###
def expression_converter(expression, interpretation, converted_expression):
    for element in expression:
        if type(element) == list:
            expression_converter(element, interpretation, converted_expression)
        elif element in interpretation:
            converted_expression.append(interpretation[element])
        else:
            converted_expression.append(element)

    return converted_expression

def not_checker(expression):
    for element in expression:
        if element == "NOT":
            return True
        elif type(element) == list:
            not_checker(element)

def not_converter(converted_expression):
    not_counter = 0
    index = -1
    for element in converted_expression:
        index += 1
        if element == "NOT":
            not_counter += 1
        
        elif element == "true":
            if not_counter%2 == 0:
                converted_expression[index] = "true"
            else:
                converted_expression[index] = "false"

        elif element == "false":
            if not_counter%2 == 0:
                converted_expression[index] = "false"
            else:
                converted_expression[index] = "true"

    try:
        while True:
                converted_expression.remove("NOT")
    except ValueError:
        pass

    print(converted_expression)
    return converted_expression

def boolean_element(final_expression):
    true_or_false = ""

    if "AND" in final_expression:
        if "false" in final_expression:
            true_or_false = "false"
        else:
            true_or_false = "true"
    elif "OR" in final_expression:
        if "false" and "true" in final_expression:
            true_or_false = "true"
        elif "true" and not "false" in final_expression:
            true_or_false = "true"
        else:
            true_or_false = "false"
    else:
        if "true" in final_expression:
            true_or_false = "true"
        else:
            true_or_false = "false"

    return true_or_false


def interpret(expression, interpretation):
    converted_expression = []

    if not_checker(expression):
        final_expression = not_converter(expression_converter(expression, interpretation, converted_expression))
    elif type(expression) != list:
        final_expression = 
    else:
        final_expression = expression_converter(expression, interpretation, converted_expression)

    return boolean_element(final_expression)

#print(interpret(["door_open", "AND", "cat_gone"], 
#               {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"} ))

#print(interpret(["cat_asleep", "OR", ["NOT", "cat_gone"]],
#               {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"}))

#print(interpret(["true", "OR", "true"], {}))

print(interpret("cat_gone", {"door_open": "false", "cat_gone": "true"}))
print(expression_converter("cat_gone", {"door_open": "false", "cat_gone": "true"}))
#print(interpret(["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],
#               {"cat_asleep": "false"}))
#print(interpret(["NOT", "AND", "true"], {"NOT":"true"}))

#print(interpret(["NOT", "AND"], {"AND": "false"}))