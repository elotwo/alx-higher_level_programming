#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for x in text:
            if x  == ":" or x == "?" or x == ".":
                print("\n\n", end = " ")
            else:
                print ("{}". format(x), end = " ")

