import logging
#  function practice problems and solutions
logging.basicConfig(level=logging.DEBUG)


# problem: 1) Write a Python function using find max number
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)
a = 10
b = 14
c = 12

'''output: maximum number is : 14'''

# problem: 2) sum all the numbers in a list. lst:(6,8,6,7,8)
def sum_num(num):
    total=0
    for x in num:
        total += x
    return total

'''OutPut: sum of list : 35'''

# problem: 3) python reverse a string using function. String : "1234satish"
def reverse_string(x):
  return x[::-1]

String = reverse_string("1234satish")

# problem : 4) Write a Python function to calculate the factorial of a number (a non-negative integer).
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# problem : 5)Define a function which can print a dictionary where the keys are numbers between 1 and 5 (both included) and the values are square of keys.
def printDict():
    d = dict()
    for i in range(1, 4):
        d[i] = i ** 2
        logging.debug(d)


'''
output: {1: 1, 2: 4, 3: 9}
'''

# problem 6) Python program to access a function inside a function.
def fuction_s(msg):
    def inside_f():
        print(msg)
    return inside_f

def another():
    another = fuction_s("satish")

# problem : 7) Write a Python program to detect the number of local variables declared in a function.
def demo():
    x = 1
    y = 2
    str1= "satish"
    logging.debug("satish patel")

#problem :8)Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

def binary_search(array, target):
    lower = 0
    upper = len(array)
    print("Array Length:", upper)
    while lower < upper:
        x = (lower + upper) // 2
        print("Middle Value:", x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x


Array_List = [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99]








