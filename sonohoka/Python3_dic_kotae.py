sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
#1 you want to update the with multiple entris to this dictionary.. such as :  {"pantry": 22, "guest room": 25, "patio": 34}
#what can you used to do this?

#answer - you can use update

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

print(sensors)


#2 Combines two lists by using comprehension:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
print(students)

# 2.1You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is a list of pairs between the drinks list and the caffeine list.

# 2.2 Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item.
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}
print(zipped_drinks)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

#4. create the dictionary called plays zipped songs and playcounts.

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key :value for key, value in zip(songs, playcounts)}

#5. Create the dictionary called "library"
#two pair of key and value
# 1. key "The Best Songs" and values is the dictionary plays you created above.
# 2.Key  "Sunday Feelings" and value is empty dictionary
library = {}
library["The Bsst Songs"]= plays
library["Sunday Feelings"]= {}
print(library)

