#Creating a constant, use all uppercase
import math
PI = math.pi
CONSTANT = 35

#Dictionaries are similar to arrays
#ary   0 1 2
ary = [1,2,3]


dic = {
    "12345": "Braden",
    "term2": "Idiot",
    "term3":  "stupid",
    "player": {
        "name": "James",
        "number": "35" #you can embed dictionaries inside dictionaries
    }
}
#dictionaries are accessed via keys which is "12345" for the word Braden , term2 for the word Idoit and so on and are called as below
print(dic["player"]["name"])

#touples
person = ("Billy", 69)
print(person)
print(person[0])
print(person[1])
#person[1] = 10 this will crash the code touples cannot be changed because person is written with () not []