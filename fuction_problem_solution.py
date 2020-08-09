#  function practice problems and solutions

# problem: 1) Write a Python function using find max number
from fuction import num


def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

a = 10
b = 14
c = 12
print("maximum number is : " +str(maximum(a, b, c)))
'''output: maximum number is : 14'''

# problem: 2) sum all the numbers in a list. lst:(6,8,6,7,8)

def sum_num(num):
    total=0
    for x in num:
        total += x
    return total
print("sum of list : " + str(sum_num((6, 8, 6, 7, 8))) )

'''OutPut: sum of list : 35'''

# problem: 3) python reverse a string using function. String : "1234satish"
def Reverse_string(x):
  return x[::-1]

String = Reverse_string("1234satish")

print(String)

# problem : 4) Write a Python function to calculate the factorial of a number (a non-negative integer).

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
n=int(input("enter the number:"))
print(fact(n))

# problem : 5)Define a function which can print a dictionary where the keys are numbers between 1 and 5 (both included) and the values are square of keys.

def printDict():
    d = dict()
    for i in range(1, 4):
        d[i] = i ** 2
    print(d)


printDict()
'''
output: {1: 1, 2: 4, 3: 9}
'''

# Problem 6) make a chain of function decorators (bold, italic, underline etc.).
def bold(function):
    def apply():
        return "<b>" + function() + "</b>"
    return apply

def italic(function):
    def apply():
        return "<i>" + function() + "</i>"
    return apply

def underline(function):
    def apply():
        return "<u>" + function() + "</u>"
    return apply
@bold
@italic
@underline
def test():
    return "satish patel"
print(test())

# problem 7) Python program to access a function inside a function.
def fuction_s(msg):
    def inside_f():

        print(msg)

    return inside_f



another = fuction_s("satish")
another()

# problem : 8) Write a Python program to detect the number of local variables declared in a function.

def demo():
    x = 1
    y = 2
    str1= "satish"
    print("satish patel")

print(demo.__code__.co_nlocals)
