#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None

    rets = len(sentence), sentence[0]
    return rets
