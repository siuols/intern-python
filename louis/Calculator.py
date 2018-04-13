class Calculator:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def addition(self):
		return int(self.num1 + self.num2)

	def subtraction(self):
		return int(self.num1 - self.num2)

	def multiplication(self):
		return int(self.num1 * self.num2)

	def division(self):
		return int(self.num1 / self.num2)

#converted from string to integer
num1 = input("Input first number: ")
operator = input("Mathematical operator: ")
num2 = input("Input second number: ")

#pass input data to class
obj = Calculator(num1,num2)

if operator == "+":
	print ("The Sum {} and {} is: ".format(num1,num2),obj.addition())
elif operator == "-":
	print ("The Diffirence {} and {} is: ".format(num1,num2),obj.subtraction())
elif operator == "*":
	print ("The Product {} and {} is: ".format(num1,num2),obj.multiplication())
elif operator == "/":
	print ("The Quotient {} and {} is: ".format(num1,num2),obj.division())
else:
    print("Invalid operator")