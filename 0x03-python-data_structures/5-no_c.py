#!/usr/bin/python3
def no_c(my_string):
    Nstr = ""
    if my_string is not None:
        for i in range(len(my_string)):
            if my_string[i] != "c" and my_string[i] != "C":
                Nstr = Nstr + my_string[i]
        return (Nstr)
