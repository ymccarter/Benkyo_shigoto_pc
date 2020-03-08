# word = "This is a string"
#
# a = word.upper()
# print(a)
# b = a.split()
# print(b)
# new_list = [word[0].lower()+word[1:] for word in b]
# print(new_list)
# answer = ' '.join(new_list)
# print(answer)


# Function 2
# def dash_stringify(word_list):
#     """Given a list of word strings, return a single string with all the
#         strings together, with ' - ' in between the words."""
#     # Put the code here
#     return ' - '.join(word_list)
#
# print(dash_stringify(['A', 'B', 'C']))


# def squre(n):
#     y=n**0.5
#     if n%y==0:
#         return True
#     else:
#         return False
# print(squre(119025))
# print(squre(81))
# print(squre(16))
# print(squre(33))
# print(squre(20))
#

# Function 4
def is_leap_year(year):
    """Given a year, return True if it is a leap year, else return False"""
    # Put the code here
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        print(str(year/4))
        return False

print(is_leap_year(2000))
print(is_leap_year(2012))
print(is_leap_year(1900))
print(is_leap_year(2018))
print(is_leap_year(2016))