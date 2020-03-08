#Sorted
#1. clean the list
number_list = [2,5,1,3,4]
#how to make to looks like [1.2.3.4.5]

print(sorted(number_list))


#2. how to make it to be [5,4,3,2,1]

print(sorted(number_list, reverse=True))

# 3. You can use sorted based on Key.
# For example, you want to sorted the valuable based on distance from 3:

number_list2 =    [1,2,3,4,5]
# distance from 3 = 2, 1, 0, 1,2

def distance_from_3(number):
    return abs(3 - number)

Gap_from_3 = sorted(number_list2, key=lambda number:distance_from_3(number))
print(Gap_from_3)

# 4. distance from 3 but far to near expected out is 1,5,2,4,3

Gap_from_3_reverse = sorted(number_list2, key=lambda number:distance_from_3(number), reverse=True)
print(Gap_from_3_reverse)

#Enumerate
#5.
mylist = ['First', 'Second', 'Third']
# Output would be:
# 1, first
# 2, Second
# 3, Third

for element in enumerate(mylist, start=1):
    print(element)

#6. Create the list including the number. Expected output is [(1, 'First'), (2, 'Second'), (3, 'Third')]

New_num_list = list(enumerate(mylist, start=1))
print(New_num_list)

#Pretty Print
#7.
from pprint import pprint
myprint_data = [
    {
        "first" : 1,
        "second" : 2,
        "third" : 3
    },
    {
        "apple" : "red",
        "banana" : "yellow",
        "nested" : {'lvl': 2}
    },
    {'python', None}
]
print(myprint_data)
pprint(myprint_data)

#8. Show only each hirarlkey
pprint(myprint_data, depth=1)
pprint(myprint_data, depth=2)


#9. Python's Truth Testing procedure
#is any of them True?
#no
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(None))

# they are all true
print(bool(2.5))
print (bool('apple'))



# 11. You have CSV file "example.csv" YOu want to read it and output what's in rows:
#
# CSV is :
# first.row.is.header
# 1.2.3.4_
# 5.6.7
# 9.9.9.9_
# Expected output
# ['1', '2', '3', '4_']
# ['5', '6', '7']
# ['9', '9', '9', '9_']
# ['last', 'row', 'is', 'header']


import csv

with open('example.csv') as f:
    rows = csv.reader(f, delimiter= '.')
    header = next(rows); header[0] = 'last'
    for row in rows:
        print(row)
    print(header)


# 12 You want to write in CSV file
#
# What the file looks like is:
# header-to-write
#
# 1-2-3
# 1-2-3
# 1-2-3
#
# An-extra-row

wr_rows = [['header', 'to', 'write'],
           [1,2,3],
           [1,2,3],
           [1,2,3],
           ]

with open('write_example.csv', 'w') as fw:
    writer = csv.writer(fw, delimiter='-', lineterminator = '\n\n')
    writer.writerows(wr_rows)
    writer.writerow(['An', 'Extra', 'row'])

#13 List comprehension

iterable = 1,2,3,4
multiplied_list = list(map(lambda num: 5*num, iterable))
print(multiplied_list)

multiplied_list2 = [5*num for num in iterable ]
print(multiplied_list2)

multiplied_list3 = [5*num for num in range(1,5)]
print(multiplied_list3)

# 14 by uinsg set comprehension create a new set output like the below

multiplied_set = {5*num for num in iterable}
print("this is set {}".format(multiplied_set))
multiplied_set2 = {5*num for num in range(1,5)}
print("this is set with range :{}".format(multiplied_set2))


#15 15 by using generator comprehension, create a new genarator output like the follwoing

multiplied_generator = (5*num for num in iterable)
print(multiplied_generator)
print(next(multiplied_generator))
print(next(multiplied_generator))
print(next(multiplied_generator))
print(next(multiplied_generator))

