#dictionary: 1 
mydict={
    "mango": 100,
    "apple": 50,
    "banana": 40,
    "orange": 70
    }
print(mydict)
def sum(mydict):
    sum = 0
    for i in mydict.values():
        sum= sum+i
    return sum
print("total cost of all the fruits: ",sum(mydict))

#dictionary 2
def word_frequency(fruits):
    if fruits in dictionary:
        dictionary[fruits] += 1
    else:
        dictionary.update({fruits: 1})
lst=list(input("enter a space-seperated fruits names: ").split())
dictionary = {}
for fruits in lst:
    word_frequency(fruits)
for allKeys in dictionary:
    print ("Frequency of ", allKeys, end = " ")
    print (":", end = " ")
    print (dictionary[allKeys], end = " ")
    print()
