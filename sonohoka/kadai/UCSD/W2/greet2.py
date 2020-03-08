#! /usr/bin/env python3
import argparse

DEFAULT_GREETING = "Hello"
DEFAULT_TEXT = "World"

def greet(text=DEFAULT_TEXT,greeting = DEFAULT_GREETING):
    """Prints 'Hello World' (default) or 'Hello {text}' """
    if not text:
        text = DEFAULT_TEXT
    if not greeting:
        greeting = DEFAULT_GREETING
    print ("{} {}".format(greeting,text))

# def greet(text=DEFAULT_TEXT):
#     """Prints 'Hello World' (default) or 'Hello {text}' """
#     if not text:
#         text = DEFAULT_TEXT
#     print ("Hello {}".format(text))


# if __name__ == "__main__":
#     arg = sys.argv[1:]
#     if arg:
#         greet(arg[0])
#     else:
#         greet()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text',nargs='?', help="text to output after Hello" )
    parser.add_argument( "--greeting","-g",
                         help="Greeting such as Hello. Default is Hello",
                         type =str)
    arguments = parser.parse_args()
    greet(arguments.text, arguments.greeting)