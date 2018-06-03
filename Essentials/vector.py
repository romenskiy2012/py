def combine(array,text):
    string = ""
    while len(list(array)) > 0:
        string += str(array.pop(0))
        if len(list(array)) > 0:
            string += text
    return string