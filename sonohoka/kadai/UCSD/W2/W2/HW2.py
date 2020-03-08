"""Homework 2 for CSE-41273"""
# Replace this with your name

# example list
first = [1, 2, 3]
second = [4, 5, 6]
fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
numbers = [41, 25, 54, 15, 76, 68, 32, 38]
test_power_list1 = [2, 2, 2, 2, 2, 2]
test_power_list2 = [9, 6, 5, 4]
test_power_list3 = [33, 700, 82.25, 16, 2, 3, 9.5]
test_power_list4 = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
rotation_list = [1, 2, 3, 4]


# Function 1
def combine_lists(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list"""
    return one+two

# print(combine_lists(first,second))
# print(combine_lists(first,fruits))


# Function 2
def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence"""
    return sequence[-n:]

# print(last_n_elements(fruits,3))
# print(last_n_elements(fruits,1))
# print(last_n_elements(numbers,4))


# Function 3
def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order"""
    sequence = sequence[::-1]
    return sequence[:n]

# print(last_n_reversed(fruits,3))
# print(last_n_reversed(fruits,1))
# print(last_n_reversed(numbers,4))


# Function 4
def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of the list index"""
    my_list_index = [i for i in range(len(numbers))]
    new_list = [
        numbers[i] ** my_list_index[i]
        for i in range(len(numbers))]
    return new_list
# print(power_list(test_power_list1))
# print(power_list(test_power_list2))
# print(power_list(test_power_list3))
# print(power_list(test_power_list4))


# Function 5
def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved"""
    some_list.append(some_list[0])
    return some_list.pop(0)  # ,some_list

# print(rotate_list(rotation_list))
# print(rotate_list(fruits))


# Function 6
def matrix_fill(n_rows, n_cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    return [
        [(i + 1)+n_rows*j for i in range(n_cols)]
        for j in range(n_rows)]
# print(matrix_fill(3, 4))
# print(matrix_fill(5,3))
# Function 7


def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value for each key is a list of the character codes of the
        letters of the word that is its key"""
    return {
        word: [ord(word[i])
               for i in range(len(word))]
        for word in words}

# words = ['yes', 'no']
# print(get_word_codes(words))
# print(get_word_codes(['hello', 'python', 'bye']))
# print(get_word_codes(['Python is fun!']))
