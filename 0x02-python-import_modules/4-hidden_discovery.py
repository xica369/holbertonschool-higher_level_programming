#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)
    for i in range(len(lista)):
        if not lista[i].startswith("__"):
                print(lista[i])
