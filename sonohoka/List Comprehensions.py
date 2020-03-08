#1. turn into the following list to   List Comprehension


words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
print(usernames)

#answer

usernames = [word for word in words if word[0] == '@']
print(usernames)



#2.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster1=[]
for height in heights:
  if height>161:
    can_ride_coaster1.append(height)
print(can_ride_coaster1)



can_ride_coaster = [height for height in heights if height>161]
print(can_ride_coaster)


#3. by using the username list above

messages = [user + " please follow me!" for user in usernames]
print(messages)


#4. Create the list of F list by using the List comprehensive

celsius = [0, 10, 15, 32, -5, 27, 3]


fahrenheit=[temp *9/5+32 for temp in celsius]
print(fahrenheit)


#5.Create a list comprehensive from the following loop

single_digits=list(range(10))
squares=[]
for i in single_digits:
  value=i*i
  squares.append(value)
print(squares)

squares2=[i*i for i in single_digits]
print(squares2)

#6. Create a list comprehensive from the following loop:

cube=[]
for i in single_digits:
  value=i**3
  cube.append(value)
print(cube)

cubes=[value**3 for value in single_digits]
print(cubes)


#1. turn into the following list to   List Comprehension


words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
print(usernames)

#answer

usernames = [word for word in words if word[0] == '@']
print(usernames)



#2.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster1=[]
for height in heights:
  if height>161:
    can_ride_coaster1.append(height)
print(can_ride_coaster1)



can_ride_coaster = [height for height in heights if height>161]
print(can_ride_coaster)


#3. by using the username list above

messages = [user + " please follow me!" for user in usernames]
print(messages)


#4. Create the list of F list by using the List comprehensive

celsius = [0, 10, 15, 32, -5, 27, 3]


fahrenheit=[temp *9/5+32 for temp in celsius]
print(fahrenheit)


#5.Create a list comprehensive from the following loop

single_digits=list(range(10))
squares=[]
for i in single_digits:
  value=i*i
  squares.append(value)
print(squares)

squares2=[i*i for i in single_digits]
print(squares2)

#6. Create a list comprehensive from the following loop:

cube=[]
for i in single_digits:
  value=i**3
  cube.append(value)
print(cube)

cubes=[value**3 for value in single_digits]
print(cubes)



#7 Clipper's project:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#7.1 bring down current price all $5 less. Please create a new list by using List Comprehensive

new_prices = [price - 5 for price in prices]
print(new_prices)


#7.2 total revenue of last week?
revlist=[prices[i]*last_week[i] for i in range(len(hairstyles))]
total_revenue=sum(revlist)
print("Total Revenue: $%.2f" %(total_revenue) )


# 8. Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
#
# Return the amount of numbers in that list that are divisible by 10.

print(divisible_by_ten([20, 25, 30, 35, 40])) #--> answer should be 3


def divisible_by_ten(nums):
  lst = [item for item in nums if item % 10 == 0]
  return len(lst)


print(divisible_by_ten([20, 25, 30, 35, 40]))

#7.3Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.


cut_under_30_lecture = [
  hairstyles[i]  # expression
  for i in range(len(hairstyles))  # for statement
  if new_prices[i] < 30  # condition]
]
print(cut_under_30_lecture)

#
# 9.9. Create a function named add_greetings() which takes a list of strings named names as a parameter.
#
# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.
#
# Return the new list containing the greetings.

# print(add_greetings(["Owen", "Max", "Sophie"]))
#
# greetings = []
#
#
# def add_greetings(names):
#   greetings = ["Hello," + name for name in names]
#   return greetings
#

# print(add_greetings(["Owen", "Max", "Sophie"]))

# mylist=[4, 8, 10, 11, 12, 15]
# #
# # whereis=mylist.index(8)
# # print(whereis)


# 10.Write a function called delete_starting_evens() that has a parameter named lst.
#
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
#
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
#
# Make sure your function works even if every element in the list is even!


def delete_starting_evens(lst):
    while True:
      if len(lst)>1 and lst[0]%2==0:
          lst.pop(0)
      elif len(lst)==1 and lst[0]%2==0:
        emptylst=[]
        return emptylst
      else:
         return lst

         # print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
      # print(delete_starting_evens([4, 8, 10]))
# 11.Create a function named odd_indices() that has one parameter named lst.
#
# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
#
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
#
# Community Forums
# Still have questions? View this exercise's thread in the Codecademy Forums
# Report a Bug
# If you see a bug or any other issue with this page, please report it here.

def odd_indices(lst):
  newlst = []
  # whereis=0
  for i in lst:
    if len(
            newlst) == 0 and i % 2 != 0:  # it is first odd number is added.
      newlst.append(i)
      whereis = lst.index(i)
    elif len(newlst) >= 1 and whereis < len(
            lst) - 1:  # it is from second and above and whatever index of fist add is added until lst is ended.
      whereis = whereis + 2
      newlst.append(lst[whereis])
  return newlst


#
#
print(odd_indices([4, 3, 7, 10, 11, -2]))
#
# mylst = [4, 3, 7, 10, 11, -2]
#
# for num in range(mylst):
#     print (num)


# 12.Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.
#
# For example, consider the following code.
#
# exponents([2, 3, 4], [1, 2, 3])
# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.


def exponents(bases, powers):
  anslist = []
  for i in bases:
    for j in powers:
      ans = i ** j
      anslist.append(ans)
  return anslist


print(exponents([2, 3, 4], [1, 2, 3]))

13.1.
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.


def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst1) == sum(lst2):
    return lst1
  else:
    return lst2


print(larger_sum([1, 9, 5], [2, 3, 7, 4]))
#
# 14.Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
#
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
#
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.


def over_nine_thousand(lst):
  total = 0
  if lst == []:
    return 0
  for i in lst:
    if total < 9000:
      total += i
  return total


print(over_nine_thousand([8000, 900, 120, 5000]))

#
# 15 Create a function named max_num() that takes a list of numbers named nums as a parameter.
#
# The function should return the largest number in nums

def max_num(lst):
  newlst = sorted(lst)
  return newlst[-1]


print(max_num([50, -10, 0, 75, 20]))

16
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]


def same_values(lst1, lst2):
  newlst=[i for i in range(len(lst1)) if lst1[i] == lst2[i]]
  return newlst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


17
.
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.


def reversed_list(lst1, lst2):
  lst1.reverse()
  if lst1 == lst2:
    return True
  else:
    return False


print(reversed_list([1, 2, 3], [3, 2, 1]))


18:
You're a programmer working for Copeland's Corporate Company. At this company, each employee's user name is generated by taking the first five letters of their last name.

A new employee, Rodrigo Villanueva, is starting today and you need to create his account. His first_name and last_name are stored as strings in script.py.

Create a variable new_account by slicing the first five letters of his last_name.

19.

Temporary passwords for new employees are also generated from their last names.


Create a variable called temp_password by creating a slice out of the third through sixth letters of his last_name.
first_name = "Rodrigo"
last_name = "Villanueva"
first_name = "Rodrigo"
last_name = "Villanueva"





first_name = "Rodrigo"
last_name = "Villanueva"

#new_account=last_name[:5]
#print(new_account)

def new_account(name):
  return name[:5]

print(new_account(last_name))

temp_password=last_name[2:6]
print(temp_password)
def temp_password(name):
  return name[2:6]

print(temp_password(last_name))


20
Copeland's Corporate Company has realized that their policy of using the first five letters of an employee's last name as a user name isn't ideal when they have multiple employees with the same last name.

Write a function called account_generator that takes two inputs, first_name and last_name and concatenates the first three letters of each and then returns the new account name.


first_name = "Julie"
last_name = "Blevins"

def account_generator(first,last):
  return first[:3]+last[:3]

print(account_generator(first_name,last_name))



21
Copeland's Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator that takes two inputs, first_name and last_name and then concatenate the last three letters of each and returns them as a string.
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first,last):
  #length=len(first)
  return first[(len(first))-3:]+last[(len(last))-3:]


print(password_generator(first_name,last_name))


22
.
Use negative indices to find the the second to last character in company_motto. Save this to the variable second_to_last.

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

23.
Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word.

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"


def Sec2Last(mystring):
  return mystring[-2]

second_to_last=Sec2Last(company_motto)

def finalword(mystring):
  return mystring[-4:]
final_word=finalword(company_motto)




24
The most recent hire at Copeland's Corporate Company is a fellow named Rob Daily. Unfortunately, Human Resources seem to have made a bit of a typo and sent over the wrong first_name.

Try changing the first character of first_name by running

first_name = "Bob"
last_name = "Daily"


fixed_first_name="R"+first_name[1:]
print(fixed_first_name)


25
password = "theycallme\"crazy\"91"


26.
sentence = 'Mary had a little lamb'
print(sentence.count('a'))


27
Write a function called letter_check that takes two inputs, word and letter.

This function should return True if the word contains the letter and False if it does not.

def letter_check(word,letter):
    letter=letter.lower()
    word=word.lower()
    if letter in word:
        return True
    else:
        return False


print(letter_check("Apple","a"))


28
Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

The letters in the returned list should be unique. For example,

def common_letters(string_one,string_two):
    string_one=string_one.lower()
    string_two=string_two.lower()
    list_string1 = list(string_one)
    list_string2 = list(string_two)
    commonlist=[]
    for i in list_string1:
        for j in list_string2:
            if i==j:
                commonlist.append(i)
    commonlist=set(commonlist)
    commonlist=list(commonlist)
    return commonlist



29,
tile ka "Hello world"
split
join
replace
strip
format


"Hello world".title()
"Hello world".split()
''.join(["Hello world"])
"Hello World".replace("H","J")
"  Hello world".strip() #space will be stripped
"{} {}".format("Hello","World")


