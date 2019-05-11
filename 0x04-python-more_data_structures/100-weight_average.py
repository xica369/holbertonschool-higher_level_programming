#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    prom = 0
    div = 0
    for score, weight in my_list:
        prom = prom + (score * weight)
        div = div + weight
    return prom / div
