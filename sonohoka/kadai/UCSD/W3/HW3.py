""" Homework assignment for week 3 """
# Yukie McCarter


def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    words = sentence.split()
    a = [word for word in words
         if word.find(letter.upper()) != -1
         or word.find(letter.lower()) != -1]
    return a


def len_safe(object):
    """Return length of object or -1 if object has no length."""
    try:
        return len(object)
    except:
        return -1


def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    duplicate = set()
    for item in iterable:
        if item not in duplicate:
            yield item
            duplicate.add(item)

numbers = [4, 5, 2, 6, 2, 3, 5, 8]
num = list(unique(numbers))
print(num)