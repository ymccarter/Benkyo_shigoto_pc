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