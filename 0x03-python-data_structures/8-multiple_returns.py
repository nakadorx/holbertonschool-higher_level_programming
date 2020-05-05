#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new = (len(sentence), None)
    else:
        new = (len(sentence), sentence[0])
    return new
