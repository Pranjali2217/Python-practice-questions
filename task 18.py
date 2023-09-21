#sets 1
list1=[1,2,3,4,5]
list2=[2,4,6,5,8]
set1= set([1,2,3,4,5])
print(set1)
set2=set([2,4,6,5,8])
print(set2)
common=set1.union(set2)
print(common)

#set2
def unique_character():
    character=set(input("enter the names of games: ").split())
    print(character)
unique_character()
