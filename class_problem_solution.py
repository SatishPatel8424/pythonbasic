import logging
#  function practice problems and solutions
logging.basicConfig(level=logging.DEBUG)

#problem 1: create one class bankaccount and add the functionlity for the class..
class BankAccount:
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount

		return self.balance

	def main(self):

		a = BankAccount()

		logging.debug("Deposit is : "+str(a.deposit(100)))
		logging.debug("withdraw is : "+str(a.withdraw(500)))
		logging.debug("withdraw is : "+str(a.deposit(5000)))
		logging.debug("Deposit is : "+str(a.deposit(100)))
		logging.debug("Deposit is : "+str(a.deposit(200)))


# problem 2 : Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length

#problem 3:Calculate grade of five subjects and get the rollno,name.
class Student:
    def __init__(self):
        self.__roll = 0
        self.__name = ""
        self.__marks = []
        self.__total = 0
        self.__per = 0
        self.__grade = ""
        self.__result = ""

    def setStudent(self):
        self.__roll = int(input("Enter Roll: "))
        self.__name = input("Enter Name: ")
        print("Enter marks of 5 subjects: ")
        for i in range(5):
            self.__marks.append(int(input("Subject " + str(i + 1) + ": ")))

    def calculateTotal(self):
        for x in self.__marks:
            self.__total += x

    def calculatePercentage(self):
        self.__per = self.__total / 5

    def calculateGrade(self):
        if self.__per >= 85:
            self.__grade = "S"
        elif self.__per >= 75:
            self.__grade = "A"
        elif self.__per >= 65:
            self.__grade = "B"
        elif self.__per >= 55:
            self.__grade = "C"
        elif self.__per >= 50:
            self.__grade = "D"
        else:
            self.__grade = "F"

    def calculateResult(self):
        count = 0
        for x in self.__marks:
            if x >= 50:
                count += 1
        if count == 5:
            self.__result = "PASS"
        elif count >= 3:
            self.__result = "COMP."
        else:
            self.__result = "FAIL"

    def showStudent(self):
        self.calculateTotal()
        self.calculatePercentage()
        self.calculateGrade()
        self.calculateResult()
        print(self.__roll, "\t\t", self.__name, "\t\t", self.__total, "\t\t", self.__per, "\t\t", self.__grade, "\t\t",
              self.__result)


    def Call(self):
        s = Student()
        s.setStudent()
        s.showStudent()

