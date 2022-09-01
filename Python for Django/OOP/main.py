class Student():


    planet = "Earth"

    def __init__(self, name, cgpa=7):
        self.name=name
        self.cgpa=cgpa

stu1 = Student(name="jose", cgpa= 8.96)
stu2 = Student(name="mimi")
#stu2.cgpa=6 #update
print(stu2.cgpa)
print(stu1.cgpa)
print(stu2.planet)

class Circle():
    pi=3.14

    def __init__(self,radius):
        self.radius=radius
    #def __str__(self): # should always return a string
        #return f"Im a circle with radius {self.radius} and pi value {Circle.pi}"

    def __len__(self):
        return 99
    def area(self):
        return Circle.pi*(self.radius*self.radius)

    def double_radius(self):
        self.radius=self.radius*2

class Oval(Circle):

    def __init__(self,radius,length):
        Circle.__init__(self,radius)
        self.length=length
    def diameter(self,newradius):
        return self.radius + newradius
    def area(self): #override
        print(self.radius)
        return Circle.pi*(self.length*self.length)
circle1=Circle(radius=6)
print(circle1.area())
circle1.double_radius()
print(circle1.area())
Oval1=Oval(radius=5,length=9)
print(Oval1.diameter(newradius=4))
print(Oval1.area())
print(circle1) #string representation of the object
print(len(circle1))

