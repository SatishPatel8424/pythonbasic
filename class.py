'''1) Defining a Class in Python'''

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: 'This is my second class'
print(Person.__doc__)

''' 2) class example'''


class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

'''OutPut: Name :  Zara , Salary:  2000
                    Name :  Manni , Salary:  5000
                    Total Employee 2'''

'''3) Class Inheritance example'''

class Parent:

   parentAttr = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent):

   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()


''' Output: Calling child constructor
            Calling child method
            Calling parent method
            Parent attribute : 200'''

'''4) Overloading Operators '''


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print (v1 + v2)

'''Output: Vector (7, 8) '''


class Base:
    def __init__(self):
        self.a = "satish"
        self.__c = "Patel"


'''5) encapsulation-in-python'''
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print(self.__a)
    # Driver code


obj1 = Base()
print(obj1.a)
''' Output: satish'''