""" CLI program to test HW3 homework """
# Yukie McCarter
# For each test function, test *all* the cases shown in the instructions
import argparse
from HW3 import words_containing, len_safe, unique


def test_words_containing():
    """Return True or False if the test of len_safe passes/fails"""
    TEST_PASSED = True  # Assume the test will succeed
    SENTENCE_TEST = '''Anyone who has never made
     a mistake has never tried anything new'''
    result = words_containing(SENTENCE_TEST, 'a')
    if result != ['Anyone', 'has', 'made', 'a', 'mistake', 'has', 'anything']:
        TEST_PASSED = False
    SENTENCE_TEST = ""
    result = words_containing(SENTENCE_TEST, 'x')
    if result != []:
        TEST_PASSED = False
    SENTENCE_TEST = "The cow jumped over the moon"
    result = words_containing(SENTENCE_TEST, 't')
    if result != ['The', 'the']:
        TEST_PASSED = False
    SENTENCE_TEST = "The cow jumped over the moon"
    result = words_containing(SENTENCE_TEST, 'o')
    if result != ['cow', 'over', 'moon']:
        TEST_PASSED = False
    return TEST_PASSED


class Cat:
    """This is a class for len_safe test"""
    pass


def test_len_safe():
    """Return True or False if the test of len_safe passes/fails"""
    TEST_PASSED = True  # Assume the test will succeed
    my_dict = {'a': 23, 'b': 8}
    result = len_safe(my_dict)
    if result != 2:
        TEST_PASSED = False
    OBJECT = []
    result = len_safe(OBJECT)
    if result != 0:
        TEST_PASSED = False
    OBJECT2 = 0.25
    result = len_safe(OBJECT2)
    if result != -1:
        TEST_PASSED = False
    OBJECT3 = 'cat'
    result = len_safe(OBJECT3)
    if result != 3:
        TEST_PASSED = False
    OBJECT4 = ''
    result = len_safe(OBJECT4)
    if result != 0:
        TEST_PASSED = False
    ANIMALS = ['dog', 'cat', 'bird', 'cat', 'fish']
    result = len_safe(ANIMALS)
    if result != 5:
        TEST_PASSED = False
    cat = Cat()
    result = len_safe(cat)
    if result != -1:
        TEST_PASSED = False
    return TEST_PASSED


def test_unique():
    """Return True or False if the test of unique passes/fails"""
    TEST_PASSED = True  # Assume the test will succeed
    numbers = [4, 5, 2, 6, 2, 3, 5, 8]
    nums = unique(numbers)
    counter = 0
    for x in range(6):
        try:
            next(nums)
            counter += 1
        except StopIteration:
            pass
    if counter == 6:
        return True
    else:
        return False

    things = unique(['dog', 'cat', 'bird', 'cat', 'fish'])
    counter = 0
    for x in range(4):
        try:
            next(things)
            counter += 1
        except StopIteration:
            pass
    if counter != 4:
        TEST_PASSED = False
    return TEST_PASSED


if __name__ == "__main__":
    # Main program
    unique_text = ("flag to test the unique function " +
                   "from HW3")
    words_text = ("flag to test the words_containing function " +
                  "from HW3")
    len_text = ("flag to test the len_safe function " +
                "from HW3")
    # Set up argparse information here
    # Based on user input, run test(s) requested and print results
    # The ONLY printing should happen here. No other parts of the code
    # should print things.
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--unique",
                        action="store_true",
                        help=unique_text)
    parser.add_argument("-w", "--words",
                        action="store_true",
                        help=words_text)
    parser.add_argument("-l", "--len",
                        action="store_true",
                        help=len_text)
    args = parser.parse_args()

    if args.words is True:
        word_containing_test = test_words_containing()
        if word_containing_test is True:
            print("words containing passed")
        else:
            print("words containing failed")

    if args.len is True:
        len_safe_test = test_len_safe()
        if len_safe_test is True:
            print("len_safe passed")
        else:
            print("len_safe failed")

    if args.unique is True:
        unique_test = test_unique()
        if unique_test is True:
            print("unique passed")
        else:
            print("unique failed")
