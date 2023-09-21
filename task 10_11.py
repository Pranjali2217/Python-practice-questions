#Functions and Function Scope:1
def calculate_average(numbers):
    print(sum(numbers)/len(numbers))
numbers=[1,2,3,4,4,5]
calculate_average(numbers)

#Functions and Function Scope:2
def calculate_factorial(num):
    return 1 if(num==1 or num==0) else num*calculate_factorial(num-1);
num=int(input("enter a number: "))
print('factorial of number is: ',calculate_factorial(num))
