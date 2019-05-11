#!/usr/bin/python3
def roman_to_int(roman_string):
    num_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in roman_string:
        for key, value in num_rom.items():
            if i == key:
                num = num + value
    return num
