def absolute_value(num):

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))
# output :
#2
#4
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

