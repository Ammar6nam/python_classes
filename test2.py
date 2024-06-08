class personalData:
    def __init__(self,name,surname,country) -> None:
        self.name=name
        self.surname=surname
        self.country=country
        
    def printPersonalData (self):
        print(f'Personal data: {self.name} {self.surname} {self.country}')

    def thirdFunction(self):
        return 'Nothing supper important'
    
class SensitiveData(personalData):
    def __init__(self, name, surname, country, geneticCode) -> None:
        super().__init__(name,surname,country)
        self.name=name
        self.surname=surname
        self.country=country
        self.geneticCode=geneticCode

    def printPersonalData(self):
        #print(f'Personal data: {self.name} {self.surname} {self.country} {self.geneticCode}')
        #super().thirdFunction()
        print(personalData.thirdFunction(self))
    
    def printSensitiveData(self):
        print(f'Sensetive data of yours is {self.geneticCode}')

person1=SensitiveData('Ammar','Nammour','Syria','SZKBD')
person1.printPersonalData()
# person1.printSensitiveData()

# class grandParent:
#     def print(self):
#         print('I am the grandparent ')

# class parentA(grandParent):
#     def print(self):
#         print('Im a parent A')
        
# class parentB(grandParent):
#     def print(self):
#         print('Im a parent B')

# class child(parentA,parentB):
#     pass

# child1=child()
# child1.print()
# print(child.mro())