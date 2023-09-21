#remove duplicate using function
def remove_duplicate(x):
    return list(dict.fromkeys(x))
x=list(map(int,input("enter values in the list: ").split()))
result= remove_duplicate(x)
print(result)

