#!/usr/bin/python3
def weight_average(my_list=[]):
    prom = 0
    div = 0
    for score, weight in my_list:
        prom = prom + (score * weight)
        div = div + weight
    return prom / div
