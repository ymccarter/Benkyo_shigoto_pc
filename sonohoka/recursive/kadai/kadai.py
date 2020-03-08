#1. how can I unpack them flat?

#matrix4 = [[[[1, 2, 3], [4, 5, 6]], [7, 8, 9]], [10, 11, 12], 13, 14,[15, 16, 17]]

matrix4 = [[1,2],[4,5]]
#targetting outcome is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def flatten(mylist):
    print("starting function")
    main_flat_result =[]
    for item in mylist:
        print("current item is {}".format(item))
        ans = isinstance(item, list)
        if ans:
            flat_list =flatten(item)
            print("main_result {}".format(main_flat_result))
            #print("flat_list is {}".format(flat_list))
            main_flat_result += flat_list
            print("after flat_list is added, main_result is now {}".format(main_flat_result))
        else:
            #print("ground one {}".format(item))
            main_flat_result.append(item)
            print('single item result {}'.format(main_flat_result))
    return main_flat_result

#print(flatten(matrix4))





mylist = [[['apple', 'pinapple'], ['neko', 'mickey']],'on jacuzzy']


def flatten(my_list):
    result = []
    for item in my_list:
        if isinstance(item, list):
            flat_list = flatten(item)
            result += flat_list
        else:
            result.append(item)
    return result

#print(flatten(mylist))




mydic = {'sg':[1,2,3], 'ec2-ami':[234, 455, 678], 'vpc-id':{'1234':'5678'}, 'happy':[[['mickey', 'neko'], 'jacczzy'], 'airport']}

def flatten_value(my_dictionary):
    result = []
    for k, v in my_dictionary.items():
        if isinstance(v, dict):
            new_dict = flatten_value(v)
            #print("function is called {}".format(new_dict))
            result += new_dict
        elif isinstance(v, list):
            #print("Yes {}".format(v))
            for x in v:
                if isinstance(x,list):
                    print("Yes {}".format(x))
                    new_list = flatten(x)
                    #import pdb;pdb.set_trace()
                    #result.append(new_list)
                    for y in new_list:
                        result.append(y)
                else:
                    result.append(x)
                #print(x)
                # for small in x:
                #     result.append(small)
        else:
            result.append("{0}".format(v))
    return result


print(flatten_value(mydic))

#result is [1,2,3,234,455,678, 5678]











#possible helpful example below:
#recursive?
# if what is in is islist: And run unpack process again and if not, append.

"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
flat_list = []
for each_list in matrix:
    for y in each_list:
        flat_list.append(y)
print(flat_list)

flat_list_com = [y for each_list in matrix for y in each_list]
print(flat_list_com)


matrix2 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]
flat_list2 = []
for each_list in matrix2:
    for small_list in each_list:
        for x in small_list:
            flat_list2.append(x)
print(flat_list2)


flat_list_com2 = [x for each_list in matrix2 for small_list in each_list for x in small_list ]
print(flat_list_com2)


matrix3 = [[[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]]

flat_list3 = []
for each_list in matrix3:
    for another_list in each_list:
        for small_list in another_list:
            for x in small_list:
                flat_list3.append(x)
print(flat_list3)

flat_list3_com = [x for each_list in matrix3 for another_list in each_list for small_list in another_list for x in small_list]
print(flat_list3_com)

"""