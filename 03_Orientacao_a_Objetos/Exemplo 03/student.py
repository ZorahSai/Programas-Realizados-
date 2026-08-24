BLUE = '\033[34m'
RESET = '\033[0m'
#features for managing a students name and grades
class Student:
    
    def __init__(self,name,roll,age,number):
        self.name = name
        self._roll = roll
        self.__age = age
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def __str__(self):
        return BLUE + "name: " + RESET + self.name + BLUE + "\nScores: " + RESET + \
            " ".join(map(str,self.scores))
        
    #represents a student
    def getname(self):
        #returns student name
        return self.name

    def getRoll(self):
        return self._roll
    
    def getAge(self):
        return self.__age
  