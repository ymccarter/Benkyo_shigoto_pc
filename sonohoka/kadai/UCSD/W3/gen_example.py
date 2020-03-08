def count(n=0):
    print("start count")
    while True:
        yield n
        n+=1
        print("loop")
    print("end")

c = count()

for x in c:
    print(x)
    if x > 3:
        break
print("in middle ")
for x in c:
    print(x)
    if x > 3:
        break

print("in middle ")
for x in c:
    print(x)
    if x > 3:
        break