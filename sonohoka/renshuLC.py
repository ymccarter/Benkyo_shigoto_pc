
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)

username2=[word for word in words if word[0]=='@']

print(usernames)
print(username2)


#2. Turn the follwoing conditional loop list creation to List comprehension:

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster1=[]
for height in heights:
  if height>161:
    can_ride_coaster1.append(height)
print(can_ride_coaster1)


can_ride_coaster=[height for height in heights if height>161]
print(can_ride_coaster)


#3
followme=[name + " please follow me!" for name in usernames ]
print(followme)


#f-->c
celsius = [0, 10, 15, 32, -5, 27, 3]

kashi=[temp*9/5+32 for temp in celsius]
print(kashi)


#5
single_digits=list(range(10))
squares=[]
for i in single_digits:
  value=i*i
  squares.append(value)
print(squares)

squareslc=[i*i for i in single_digits]
print(squareslc)


#6
cube=[]
for i in single_digits:
  value=i**3
  cube.append(value)
print(cube)

cubelc=[i**3 for i in single_digits]
print(cubelc)

#7

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

new_price=[price-5 for price in prices]
print(new_price)

total_revenu=[prices[i]*last_week[i] for i in range(len(hairstyles))]
total_revenu=sum(total_revenu)
print("Total revenue: $%.2f" %(total_revenu))

cuts_under_30=[hairstyles[i] for i in range(len(hairstyles)) if new_price[i]<30]
print(cuts_under_30)



def delete_starting_evens(lst):
    while True:                                             
      if len(lst)>1 and lst[0]%2==0:                      
          lst.pop(0)                                      
      elif len(lst)==1 and lst[0]%2==0: 
        emptylst=[]
        return emptylst                                
      else:                                               
         return lst                                       
                                                  
