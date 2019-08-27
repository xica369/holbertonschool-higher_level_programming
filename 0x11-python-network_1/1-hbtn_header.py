#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """


if __name__ == "__main__":
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as response:
        html = response.read()
        print ("{}".format(response.info().get('X-Request-Id')))
