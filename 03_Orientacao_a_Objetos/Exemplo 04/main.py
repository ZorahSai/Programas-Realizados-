from student import Student
RESET = '\033[0m'
RED = '\033[31m'

nameStudent = input(RED +"Student Name: " + RESET)
rgStudent = input(RED + "RG: " + RESET)

myStudent = Student(nameStudent,rgStudent)

print("\n")
myStudent.toDrink("Guaraná")
print()
myStudent.toDrink("Beer" + "batata")