"""Homework 2 for CSE-41273"""


# Function 1
# Idiomatic:
def combine_lists(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list"""
    return one + two


# Longer:
def combine_lists2(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list"""
    new_list = []
    new_list += one
    new_list += two
    return new_list


# Or, Using Methods:
def combine_lists3(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list"""
    new_list = []
    new_list.extend(one)
    new_list.extend(two)
    return new_list


# Function 2
def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence"""
    return sequence[-n:]


# Note this (above) does not work the way you might expect it to work if n is
# zero. You will get all the elements. You might argue that having n as zero
# is invalid input - after all, it doesn’t really make sense!
# If you want to handle this input condition, you can use:
def last_n_elements2(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence"""
    if n > 0:
        return sequence[-n:]
    return []


# Function 3
def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order"""
    return sequence[:-n-1:-1]


# Function 4
def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of the list index"""
    return [
        n ** i
        for i, n in enumerate(numbers)
    ]


# Function 5
def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved"""
    item = some_list.pop(0)
    some_list.append(item)
    return item


# Function 6
def matrix_fill(n_rows, n_cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    return [
        [row * n_cols + col for col in range(1, n_cols + 1)]
        for row in range(n_rows)
    ]


# Function 7
def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value is a list of the character codes of the letters
        of the word that is its key"""
    return {
        word: [ord(letter) for letter in word]
        for word in words
    }
