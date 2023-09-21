#inheritanceand polymorphism:1
class vehicle:
    def __init__(self,make,model):
        self.make= make
        self.model= model
    
    def display(self):
        print(self.make)
        print(self.model)
        
class car(vehicle):
    def __init__(self,make,model,year):
        self.year= year
        vehicle.__init__(self,make,model)
        
    def view(self):
        print(self.year)
obj= car('robin',850,2015)
obj.display()
obj.view()

#inheritance and polymorphism :2:
import math
class Shape:
    def calculate_area(self):
        pass

class circle:   
    def __init__(self,radius):
        self.radius= radius
        
    def calculate_area(self):
        print("area of circle: ",math.pi*self.radius*self.radius)
        
class rectangle:
    def __init__(self,height,width):
        self.height= height
        self.width= width
    
    def calculate_area(self):    
        print("area of rectangle: ",self.height*self.width)
        
obj1 = circle(2)
obj1.calculate_area()
obj2 =rectangle(8,4)
obj2.calculate_area()
