import itertools
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#
# flat = list(itertools.chain(*matrix))
# print(flat)
#
# flat = [x for sublist in y for x in matrix]
#
#
# flat_list = []
# for sublist in l:
#     for item in sublist:
#         flat_list.append(item)


# l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
# flat_list = [item for sublist in l for item in sublist]
# flat_list_first = [item for sublist in l for item in sublist]
# #print(flat_list)
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# flat_list = []
# for each_list in matrix:
#     for x in each_list:
#         flat_list.append(x)
# print(flat_list)

# flat_list = [item for each_list in matrix for item in each_list]
# # print(flat_list)

# def special_nums():
# #     # answer = []
# #     # for x in range(301):
# #     #     if x % 6 == 0 and x % 10 == 0:
# #     #         answer.append(x)
# #     # return answer
# #     answer = [x for x in range(1,301) if x % 6 == 0 and x % 10 == 0]
# #     return answer
# #
# # print(special_nums())

#
# data = {'a': 2, 'b': 5, 'c': 6}
# #print(len(data))
#
# def switched(dict):
#     # new_dict = {}
#     # for k,v in dict.items():
#     #     new_dict[v] = k
#     # return new_dict
#     new_dict = {v:k for k,v in dict.items()}
#     return new_dict
#
# print(switched(data))

# def my_range():
#     while True:
#         yield 9
#         #current +=1
#
#nums3 = my_range()
#
# print(next(nums3))
# print(next(nums3))
# print(next(nums3))
# print(next(nums3))




# def is_prime(candidate):
#     for n in range(2, candidate):
#          if candidate % n == 0:
#              return False
#     return  True

# def is_prime(candidate):
#     for n in range(2, candidate):
#          if candidate % n == 0:
#              return False
#     return True
#
# # print(is_prime(3))
# # print(is_prime(15))
#
# def my_prime(candidate):
#     generator = (num for num in range(2,candidate))
#     for num in generator:
#         if candidate % num == 0:
#             return False
#     return True
#
# print(my_prime(11))
# print(my_prime(13))
# print(my_prime(345))
# print(my_prime(-255))
# # def getPrimes(n):
#     yield 2
#     for i in xrange(3, n, 2):
#         for x in xrange(3, int(i**0.5)+2, 2):
#             if not i % x:
#                 break
#         else:
#             yield i
# my_prime = getPrimes(11)
#
# print(next(my_prime))
# print(next(my_prime))
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


# def my_range(start,end):
#     current = start
#     while current < end:
#         yield current
#         current +=1
#
# nums2 = my_range(1,10)
# print(nums2)
# print(next(nums2))
# print(next(nums2))
# print(next(nums2))

#
# def reverse_iter(sequence):
#     generator = (sequence[::-1])
#     for num in generator:
#         yield  num
#
# # nums = [8,3,6]
# it = reverse_iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
#
# items = ('a','b', 'c')
# itemit = reverse_iter(items)
# print(next(itemit))
# print(next(itemit))
# print(next(itemit))
# # tuplet_nums = (2,3,4)
# # tupeit = reverse_iter(tuplet_nums)
# # print(next(tupeit))
# # print(next(tupeit))
# # print(next(tupeit))
# #
# #
# # nums = (1, 2, 3, 4)
# # it = reverse_iter(nums)
# # print(next(it))
# # print(next(it))
# # print(next(it))
#
# nums = [8,3,6]
# it = reverse_iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
#
# nums2 = (1, 2, 3, 4)
# it = reverse_iter(nums2)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


def my_prime(candidate):
    """Return True if candidate is a prime number. Made with one statement"""
    generator = (num for num in range(2,candidate) if candidate % num == 0)
    try:
        if generator.next():
            return False
    except:
        return True

print("a  " + str(my_prime(2)))
print(my_prime(15))
print(my_prime(53))