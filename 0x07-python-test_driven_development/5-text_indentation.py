#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == ':' or text[i] == '?' or text[i] == '.':
            print("{}".format(text[i]), end="")
            if i == len(text) - 1:
                continue
            print('\n')
            continue
        if text[i - 1] == ':' or text[i - 1] == '?' or text[i - 1] == '.':
            if text[i] == " ":
                continue
        print("{}".format(text[i]), end="")
