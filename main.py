import sys
sys.path.append('/home/satish/PycharmProjects/pythonbasic/')

import fuction_problem_solution

# call the function
fuction_problem_solution.printDict()
fuction_problem_solution.another()
fuction_problem_solution.n = int(input("enter the number:"))


# print the variable
print("maximum number is : " + str(fuction_problem_solution.maximum(fuction_problem_solution.a,fuction_problem_solution.b,fuction_problem_solution.c)))
print("sum of list : " + str(fuction_problem_solution.sum_num((6, 8, 6, 7, 8))))
print("print the reverse string : " + fuction_problem_solution.String)
print("factorial is : "+str(fuction_problem_solution.fact(fuction_problem_solution.n)))
print(fuction_problem_solution.demo.__code__.co_nlocals)

