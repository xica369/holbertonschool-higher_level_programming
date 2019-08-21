#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """find peak function"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return(list_of_integers[0])
    return(None)
