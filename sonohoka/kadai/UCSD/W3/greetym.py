#! /usr/bin/env python3
#import sys
import argparse

def greet(text = "World"):
    if not text:
        text = "World"
    print ("Hello {}".format(text))


# if __name__ == "__main__":
#     arg = sys.argv[1:]
#     if arg:
#         greet(arg[0])
#     else:
#         greet()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text',nargs='?', help="text to output after Hello")
    arguments = parser.parse_args()
    greet(arguments.text)