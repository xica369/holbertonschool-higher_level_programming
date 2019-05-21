#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = [0] * list_length
    for i in range(list_length):
        try:
            list[i] = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            list[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            list[i] = 0
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return list
