#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)

    fir = list(a_dictionary)
    st = fir[0]
    tem = a_dictionary[st]

    for k, v in a_dictionary.items():
        if v > tem:
            tem = v
            st = k

    return (st)
