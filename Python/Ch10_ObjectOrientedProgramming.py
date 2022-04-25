Class Employee:		[classname is written in PascalCase]
	#methods & variables
Class Employee:
	company = “Google” 	#Specific to each class
Jon = Employee()	#Object instantiation
Jon.company
Employee.company = “YouTube”	#changing class attribute
Jon.name = “Jon”
Jon.salary = “30K”	#Adding instance attributes
Jon.getSalary()
class Employee:
	company = “Google”
	def getSalary(self):
		print(“Salary is not there”)
        @staticmethod	#decorator to mark greet as a static method
def greet():
	print(“Hello user”)

class Employee:
	def __init__(self,name):
		self.name = name
	def getSalary(self):
		#Some code…
harry = Employee(“Harry”)	#Object can be instantiated using constructor like this!
