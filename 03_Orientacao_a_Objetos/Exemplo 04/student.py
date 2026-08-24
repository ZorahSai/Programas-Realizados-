BLUE = '\033[34m'
RESET = '\033[0m'
#features for managing a students name and grades
class Student:
    def __init__(self,name,rg):
        self.name = name
        self.__rg = rg
        
    def __presentDocument(self):
        print(self.__rg)
    
    def toDrink(self,drink):
        if drink == 'Beer':
            self.__presentDocument()
        print("Drinking " + drink)
        