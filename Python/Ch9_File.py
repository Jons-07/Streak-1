open(“this.txt”, “r”)

f = open(“this.txt”, “r”)    

text = f.read()       

print(text)    

f.close()       
f.read(2)     

f.readline()             

f = open(“this.txt”, “w”)

f.write(“This is nice”)      

f.close()

Class Employee:
	company = “Google” 	
harry = Employee()	
harry.company
Employee.company = “YouTube”	

class Employee:
	company = “Google”
	def getSalary(self):
		print(“Salary is not there”)

@staticmethod	
def greet():
	print(“Hello user”)
