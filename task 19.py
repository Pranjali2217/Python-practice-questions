#class and object 1:
class rectangle:
    def __init__(self,width,height):
       self.width= width 
       self.height= height
    def area(self):
        print("area= ",self.width*self.height)
obj=rectangle(8,4)
obj.area()

#class and object 2:
class student:
    def __init__(self):
        self.name="leena"
        self.age=22
        self.gender="female"
        
    def students_details(self):
        print("name of student: ",self.name)
        print("age of student: ",self.age)
        print("gender of student: ",self.gender)
details=student()
details.students_details()
