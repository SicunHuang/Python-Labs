def iterable_to_string(iteobject):
    result = ""
    for element in iteobject:
        result = result + str(element) + " "
    return result 