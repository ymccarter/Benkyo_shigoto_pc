big_list =[]
my_list =list(range(1,5))
next_list = list(range(5,9))
#big_list.append(my_list)
#big_list.append(next_list)


#
# startnumber = 1
# endnumber = 5
#
# for i in range(3):
#     my_list = list(range(startnumber,endnumber))
#     big_list.append(my_list)
#     startnumber+=4
#     endnumber+=4
# print(big_list)

def matrix_fill(howmanylist, size):
    startnumber = 1
    endnumber =1+size
    big_list = []
    for i in range(howmanylist):
        my_list = list(range(startnumber, endnumber))
        big_list.append(my_list)
        startnumber += size
        endnumber += size
    return big_list

# print(matrix_fill(3,4))
# print(matrix_fill(5,3))
# print(matrix_fill(2,2))
# print(matrix_fill(2,1))
# print(matrix_fill(1,1))
# print(matrix_fill(1,2))


# def listcomp_matrix_fill(x,y):
#     startnum = 1
#     endnum = 1+y
#     big_list = []
#     small_list = [list(range(startnum, endnum) for i in range(x)]
#     return small_list

#print(listcomp_matrix_fill(3,4))
# startnum =1
# if endnum <4*3:

#flist = [list(range(startnum, startnum+4)) for x in range(0,3)]
#print(flist)


#print(big_list1)


def comp_matrix_fill(num_of_list, size):
    startnum=1
    return [[list(range(startnum, startnum+size)) ] for x in range(0,num_of_list) ]

#print(comp_matrix_fill(3,4))

matrix = [[list(range(1,5))] for row in range(3)]
#print(matrix)
#
# a_list = [1,2,3,4,5]
# for i in range(len(a_list)):
#     print (i, a_list[i])

def matrix_fill(num_list, num_size):
    return [[(i +1)+num_list*j for i in range(num_size)] for j in range(num_list)]
print(matrix_fill(3,4))
print(matrix_fill(5,3))