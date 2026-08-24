#features for managing a students name and grades
class Student:
    
    def __init__(self,name,number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def __str__(self):
        return"name: " + self.name + "\nScores: " + \
            " ".join(map(str,self.scores))
        
    #represents a student
    def getname(self):
        #returns student name
        return self.name
  