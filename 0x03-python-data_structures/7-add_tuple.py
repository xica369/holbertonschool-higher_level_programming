#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    listA = list(tuple_a)
    listB = list(tuple_b)
    lis = []
    if len(tuple_a) == 0:
        listA.append(0)
        listA.append(0)
    if len(tuple_a) == 1:
        listA.append(0)
    if len(tuple_b) == 0:
        listB.append(0)
        listB.append(0)
    if len(tuple_b) == 1:
        listB.append(0)
    lis.append(listA[0] + listB[0])
    lis.append(listA[1] + listB[1])
    return (tuple(lis))
