#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    post_fields = {'email': argv[2]}
    data = parse.urlencode(post_fields)
    data = data.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode())
