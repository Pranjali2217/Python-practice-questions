with open('sample.txt','r') as file:
    data=file.read()
print(data)
lst=list((data).split())
upper = [x.upper() for x in lst]
print(upper)
