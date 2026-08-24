from student import Student
RESET = '\033[0m'
RED = '\033[31m'

nameStudent = input(RED +"Student Name: " + RESET)
rollStudent = input(RED + "Student's Roll: " +RESET)
ageStudent = int(input(RED + "Student's age: " + RESET))
qttGrades = int(input(RED +"Number of grades: "+ RESET))
myStudent = Student(nameStudent,rollStudent,ageStudent,qttGrades)
print(myStudent.__str__())

print("\nTesting: ")
print(myStudent.name)
print(myStudent.getRoll)
print(myStudent._roll)
print(myStudent.getAge)
print(myStudent.__age)