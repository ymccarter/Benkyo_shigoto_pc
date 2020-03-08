"""HW7 answers for CSE-41273 file_stats.py
    Module file_stats that includes the stats function.
    $ python file_stats.py filename
    Prints out file statistics.
"""
import sys


def stats(filename):
    """Given a text file name, return file statistics in a tuple:
        number of characters in the file,
        number of words in the file (as defined by whitespace),
        number of lines in the file,
        number of characters of the longest line in the file.
    """
    with open(filename, mode='rt', encoding='utf-8') as stat_file:
        contents = stat_file.read()
    char_count = len(contents)
    word_count = len(contents.split())
    lines = contents.splitlines()
    line_count = len(lines)
    max_line_length = max(len(line) for line in lines)
    return char_count, word_count, line_count, max_line_length


if __name__ == '__main__':
    char_count, word_count, line_count, max_line_length = stats(sys.argv[1])
    print(f'Characters: {char_count}')
    print(f'Words: {word_count}')
    print(f'Lines: {line_count}')
    print(f'Longest line: {max_line_length}')
