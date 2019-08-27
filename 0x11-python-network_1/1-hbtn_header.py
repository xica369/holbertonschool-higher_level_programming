#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """


if __name__ == "__main__":
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as response:
        html = response.read()
        print ("{}".format(response.info()['X-Request-Id']))
