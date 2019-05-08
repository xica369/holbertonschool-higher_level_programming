#!/usr/bin/python3
def multiple_returns(sentence):
    lis = []
    lis.append(len(sentence))
    if not sentence:
        lis.append(None)
    else:
        lis.append(sentence[0])
    return (tuple(lis))
