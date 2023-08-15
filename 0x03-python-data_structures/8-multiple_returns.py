#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if sentence == "":
        return (0, None)
    else:
        return (count, sentence[0])
