import sys
import logging
sys.path.append('/home/satish/PycharmProjects/pythonbasic/')
logging.basicConfig(level=logging.DEBUG)

import fuction_problem_solution
import class_problem_solution

# call the function
fuction_problem_solution.n = int(input("enter the number:"))
fuction_problem_solution.printDict()
fuction_problem_solution.another()

# call the class using instance
Asqr = class_problem_solution.Square(5)
logging.debug("area is : "+str(Asqr.area()))
logging.debug("area of square : "+str(class_problem_solution.Square().area()))






# print the variable
logging.debug("maximum number is : " + str(fuction_problem_solution.maximum(fuction_problem_solution.a,fuction_problem_solution.b,fuction_problem_solution.c)))
logging.debug("sum of list : " + str(fuction_problem_solution.sum_num((6, 8, 6, 7, 8))))
logging.debug("print the reverse string : " + fuction_problem_solution.String)
logging.debug(fuction_problem_solution.demo.__code__.co_nlocals)
logging.debug("factorial is : "+str(fuction_problem_solution.fact(fuction_problem_solution.n)))

if __name__ == "__main__":
	class_problem_solution.BankAccount.main(self=True)




