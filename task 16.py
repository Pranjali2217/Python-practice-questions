#tuples: 1 
countries=("India","America","Japan","Austrelia")
print(countries[2])

#tuples:2
def calculate_statistics():
    print("sum of all numbers in tuple: ",sum(x))
    print("average of all numbers in tuple:",sum(x)/len(x))
numbers = input('Enter space-separated integers: ')
x = tuple(int(item) for item in numbers.split())
print(x)
calculate_statistics()
