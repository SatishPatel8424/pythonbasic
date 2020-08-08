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

''' 6) class example'''

class Car(object):
    condition = "new"
    def __init__(self,model,color,mpg):
        self.model=model
        self.color=color
        self.mpg=mpg
my_car=Car("swift","silver",88)
print(my_car.condition)

'''Output: new'''

'''7) class example'''
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
         self.model = model
         self.color = color
         self.mpg   = mpg

    def display_car(self):
       return "This is a %s %s with %s MPG." % (self.color,self.model,str(self.mpg))

    def drive_car(self):
        self.condition="used"

class ElectricCar(Car):
    def __init__(self,model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type=battery_type

    def drive_car(self):
        self.condition="like new"

my_car=ElectricCar("swif", "silver", 88,"molten salt")
print (my_car.condition)
''' Output:new'''
my_car.drive_car()
print (my_car.condition)
'''Output:like new'''

'''8)class example'''


class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))

''' output:
            Number of instances: : 1
            Number of instances: : 2
            Number of instances: : 1
            Number of instances: : 0'''

"""
   9) iterator example
    """
class Reverse:


    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class abc:
    lst = [34, 978, 42]
    lst_backwards = Reverse(lst)
    for el in lst_backwards:
        print(el)

'''Output:42
        978
        34
'''

'''10)Motivation for Metaclasses'''


class Philosopher1(object):

    def the_answer(self, *args):
        return 42


class Philosopher2(object):

    def the_answer(self, *args):
        return 42


class Philosopher3(object):

    def the_answer(self, *args):
        return 42


plato = Philosopher1()
print(plato.the_answer())

kant = Philosopher2()
print(kant.the_answer())

''' 42
    42'''

'''11)Creating Singletons using Metaclasses'''
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonClass(Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)

x = RegularClass()
y = RegularClass()
print(x == y)

'''output:
True
False
'''

'''12)Standard Classes as Base Classes'''
class Plist(list):

    def __init__(self, l):
        list.__init__(self, l)

    def push(self, item):
        self.append(item)


if __name__ == "__main__":
    x = Plist([3,4])
    x.push(47)
    print(x)

'''Output: [3, 4, 47]'''



'''getter and setter method in python'''


# Python program showing a
# use of property() function

class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks()

mark.age = 10

print(mark.age)

'''output:
setter method called
getter method called
10

    '''
'''
Using Getters and Setters'''

class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(300)

# Get the to_fahreheit method
print(human.to_fahrenheit())
'''Output:37
98.60000000000001
572.0'''





