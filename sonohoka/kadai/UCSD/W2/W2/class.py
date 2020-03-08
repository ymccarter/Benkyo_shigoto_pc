#
# fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
# # Function 3
# def last_n_reversed(sequence, n ):
#     """Given a sequence and a number n, return the last n elements of the
#         sequence in reversed order"""
#     sequence = sequence[::-1]
#     return sequence[:n]
#
# print(last_n_reversed(fruits, 3))

# # test_power_list1 = [2, 2, 2, 2, 2, 2]
# # test_power_list1 = [2, 2, 2, 2, 2, 2]
# #
# # my_list_index=[i for i in range(len(test_power_list1))]
# # new_list = [test_power_list1[i]**my_list_index[i] for i in range(len(test_power_list1))]
# # print(new_list)
#
#
# # from greet import greet
# # help(greet)
#
# # greet('mi amor')
#
# my_string ="yes"
# my_string=list(my_string)
# each_word = [ord(item) for item in my_string]
# #print(each_word)
#
# my_list = ['yes','no']
# #print(my_list)
# big_list = []
# for item in my_list:
#     each_list=[]
#     item_list = list(item)
#     print(item)
#     for i in range(len(item)):
#         each_list.append(ord(item[i]))
#     big_list.append(each_list)
# print(big_list)
#
# word_list = [ ]
#
# #Function 7
# def get_word_codes(words_list):
#
#     """Given a list of words, return a dictionary where the words are keys,
#         and the value for each key is a list of the character codes of the
#         letters of the word that is its key"""
#
#     result_dic = { k: v for k, v in zip(words_list, values=[ord(item)for item in words_list])
#     }
#     return result_dic
# ans = ["yes", "no"]
# get_word_codes(ans)

# my_list = ['yes','no']
# #print(my_list)
# big_list = []
# for item in my_list:
#     each_list=[]
#     item_list = list(item)
#     print(item)
#     for i in range(len(item)):
#         each_list.append(ord(item[i]))
#     big_list.append(each_list)
# #print(big_list)
#

words = ['yes', 'no']
def get_word_codes(words):
    return {
        word:[ord(word[i])
              for i in range(len(word))]
        for word in words}


print(get_word_codes(words))
print(get_word_codes(['hello','python','bye']))
print(get_word_codes(['Python is fun!']))
