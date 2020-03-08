"""Homework 6 for CSE-41273"""
# Yukie McCarter
import itertools


# 1.  squash
def squash(matrix):
    """Return squashed list from list of lists"""
    flat_list = [item for each_list in matrix for item in each_list]
    return flat_list


# 2. special_nums
def special_nums():
    """Return list of numbers from 1 to 300 that are divisible by 10 and 6"""
    answer = [x for x in range(1, 301) if x % 6 == 0 and x % 10 == 0]
    return answer


# 3. switch_dict
def switch_dict(dictionary):
    """Return a new dictionary with keys and values switched"""
    new_dict = {v: k for k, v in dict.items(dictionary)}
    return new_dict


# 4. is_prime
def is_prime(candidate):
    """Return True if candidate is a prime number. Made with one statement"""
    generator = (num for num in range(2, candidate) if candidate % num == 0)
    try:
        if generator.__next__():
            return False
    except StopIteration:
        return True


# 5. number_9
def number_9():
    """Return a generator that always returns the number 9"""
    return itertools.repeat(9)


# 6. reverse_iter
def reverse_iter(iterable):
    """Return a generator that yields items from iterable in reverse order"""
    for item in iterable[::-1]:
        yield item


# 7. ReverseIter class
class ReverseIter:
    """Class whose instances iterate the initial iterable in reverse order"""
    def __init__(self, iterable):
        self.iterable = iterable[::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.iterable[index]
