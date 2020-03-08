mytu = [1,2,3]
#print(type(mytu))
mytup = (1,2,3)

if mytu == True:
    print("yes")




class YukieTest:
    @classmethod
    def from_tuple(cls, input):
        if type(input) == tuple:
            return input
        else:
            raise TypeError


point=YukieTest.from_tuple(mytup)
print(point)