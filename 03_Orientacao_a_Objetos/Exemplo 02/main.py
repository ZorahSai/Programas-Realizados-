from student import Student
RESET = '\033[0m'
RED = '\033[31m'

nameStudent = input(RED +"Student Name: " + RESET)
qttGrades = int(input(RED +"Number of grades: "+ RESET))
myStudent = Student(nameStudent,qttGrades)
print(myStudent.__str__())