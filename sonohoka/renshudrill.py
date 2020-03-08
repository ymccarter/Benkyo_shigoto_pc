#question:
#Answer of the output should be:
#            {'Randy':['Input.txt','Output.txt'], 'Stan':['Code.py']}

#            class FileOwners:

#                @staticmethod
#                def group_by_owners(files):
#                    return None

#            files = {
#                'Input.txt': 'Randy',
#                'Code.py': 'Stan',
#                'Output.txt': 'Randy'
#            }
#            print(FileOwners.group_by_owners(files))

"""
class FileOwners:

    @staticmethod
    def group_by_owners(files):
        if not files:
            return None
        owners={}
        #for file in files:
        for i in files:
            #print(i)
            #print (file)
            #print(files)
            if files[i] not in owners:
                print(files[i])
                owners[files[i]]=[]
                print(str(files[i]))
              #  owners[files[file]]=[]
            owners[files[i]].append(i)
        return owners

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
FileOwners.group_by_owners(files)
print(FileOwners.group_by_owners(files))
#newdic=FileOwners.group_by_owners(files)
#print(type(newdic))

##

filelist = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

for i in filelist:
    #print(i)
    print(filelist[i])


class FileOwners:

#     @staticmethod
    def group_by_owners(files):
        if not files:
            return None    
        owners={}
        for file in files:
            if files[file
            
        return None

filelist = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(filelist))



bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
print(bool_one)
print(bool_two)
print(bool_three)


CodeAcademy boolen:


def age_check(age):
    if age < 13:
        return "you are only " + str(age) + " years old. Please come back with your parents."
    elif age > 13:
        return True


print(age_check(14))


def greater_than(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "These numbers are the same"


print(greater_than(3, 3))


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"
    else:
        return None


print(graduation_reqs(120))

##
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)


statement_one =(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)
statement_two =(4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)

def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa>=2.0:
    return "You meet the requirements to graduate!"


#
# The registrars office at Calvin Coolidge's Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).
#
# Write a function called graduation_mailer that takes two inputs, gpa and credits and checks if a student either has 120 or more credits or a GPA 2.0 or higher and if so returns True.

statement_one =(2 - 1 > 3) or (-5 * 2 == -10)

statement_two =(9 + 5 <= 15) or (7 != 4 + 3)


def graduation_mailer(credits,gpa):
  if credits>=120 or gpa>=2.0:
    return True

##
statement_one =not (4 + 5 <= 9)
print(statement_one)

statement_two =not (8 * 2) != 20 - 4
print(statement_two)


def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  elif (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  elif not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet either requirement to graduate!"

print(graduation_reqs(3.0, 110))
print(graduation_reqs(1.0, 120))
print(graduation_reqs(2.0, 130))
print(graduation_reqs(1.0, 90))


def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."


def grade_converter(gpa):
    if gpa >= 4.0:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"


print(grade_converter(0.2))
"""
#Except and Try

def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")

print(divides(3,0))


##
# def raises_value_error():
#  raise ValueError

#Write a try statement and an except statement around the line of code that executes the function to catch a ValueError and make the error message print You raised a ValueError!

def raises_value_error():
    try:
        raise ValueError
    except ValueError:
        print("You raised a ValueError!")


raises_value_error()

