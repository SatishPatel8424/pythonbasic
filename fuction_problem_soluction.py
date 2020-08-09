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
n=int(input())
print(fact(n))