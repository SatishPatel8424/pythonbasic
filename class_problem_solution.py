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


