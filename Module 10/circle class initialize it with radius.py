print("Ahhinit tiwari 1900300100003")


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = 3.14*self.radius*self.radius
        print(f"Area is : {area}")

    def getCircumference(self):
        circ = 2*3.14*self.radius
        print(f"Circumference is : {circ}")


rad = int(input("Enter the radius : "))
circle1 = Circle(rad)
circle1.getArea()
circle1.getCircumference()
