#!/usr/bin/python3
def search_replace(my_list, search, replace):
    Nlist = []
    Nlist.append(list(map(lambda x: replace if (search == x) else x, my_list)))
    Nlist = Nlist[0]
    return Nlist
