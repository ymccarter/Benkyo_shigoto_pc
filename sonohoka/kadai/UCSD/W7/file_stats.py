"""Homework 7 file_stats for CSE-41273"""
# Yukie McCarter
import sys


def stats(myfile):
    with open(myfile) as fh:
        contents = fh.read()

    counter = 0
    longest = 0
    try:
        fh1 = open(myfile)
        for line in fh1:
            counter += 1
            if longest < len(line.strip()):
                longest = len(line.strip())
    finally:
        fh1.close()
    c = len(contents)
    w = len(contents.split())
    l = counter
    ll = longest
    return c, w, l, ll


if __name__ == "__main__":
    try:
        myfile = sys.argv[1]
        c, w, l, ll = stats(myfile)
        print("Chracters: {}".format(c))
        print("Words: {}".format(w))
        print("Lines: {}".format(l))
        print("Longest line: {}".format(ll))
    except:
        pass
