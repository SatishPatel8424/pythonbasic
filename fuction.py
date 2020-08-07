def absolute_value(num):

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))
# output :
'''2
4'''
""" 2) Scope and Lifetime of variables """
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

""" output:
 Value inside function: 10
Value outside function: 20 """


''' 3) Arguments '''
def greet(name, msg):
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")

'''OutPut : Hello Monica, Good morning! '''

''' 4)Python Default Arguments'''

def greet(name, msg="Good morning!"):


    print("Hello", name + ', ' + msg)


greet("satish")
greet("satish", "How do you do?")

'''
OutPut: Hello satish, Good morning!
        Hello satish, How do you do?'''

''' 5) Python Arbitrary Arguments'''
def satish(*names):

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

#tuple
satish("Monica", "Luke", "Steve", "John")

'''
Output: Hello Monica
Hello Luke
Hello Steve
Hello John'''

'''6) Example of a recursive function '''

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 4
print("The factorial of", num, "is", factorial(num))
''' The factorial of 4 is 24 '''

'''7) Example of Lambda Function in python'''

double = lambda x: x * 2

print(double(5))

''' Output: 10 '''

''' 8) Example use with filter() '''
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

''' Output : [4, 6, 8, 12] '''

''' 9) Global variable and Local variable with same name'''

x = 5
def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)

'''OutPut: local x: 10
            global x: 5'''

'''Using *args to pass the variable length arguments to the function'''
def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:", sum)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

'''
output: Sum: 8
        Sum: 22
        Sum: 17 '''
''' Using **kwargs to pass the variable keyword arguments to the function '''
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

'''Output:
Data type of argument: <class 'dict'>
Firstname is Sita
Lastname is Sharma
Age is 22
Phone is 1234567890

Data type of argument: <class 'dict'>
Firstname is John
Lastname is Wood
Email is johnwood@nomail.com
Country is Wakanda
Age is 25
Phone is 9876543210'''



''' Functions as Parameters'''


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")


def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()


f(g)

