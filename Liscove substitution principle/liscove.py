#liscove substitution principle states that a subclass
#should be able to susbstitute a superclass whenever it is needed
   
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height =height
        
    def area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def set_width(self , width):
        self.width = width
        self.height = width
        
    def set_height(self,height):
        self.width = height
        self.height = height
        
def print_area(rectangle):
    rectangle.set_width(4)
    rectangle.set_height(5)
    area = rectangle.area()
    print("Area:", area)
#since square inheri rectangle we can pas print area functionality

rectangle =Rectangle(0,0)
square =Square(0,0)


print_area(rectangle)
print_area(square)