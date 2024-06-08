class myclass:
    # name='Ammar'
    # surname='Nammour'
    # favorite=['reading','coffee']
    def __init__(self,name,surname,year) -> None:
        self.name=name
        self.surname=surname
        self.year=year

    def __str__(self) -> str:
        return f'{self.name}{self.surname}{self.year}'
    
    def yearsEmployed(self):
        return 2023 - self.year
# object=myclass()
# object2=myclass()
object3=myclass('Ammar','Nammour',2016)
object4=myclass('Rubin','Van dersar',2023)

emp1=myclass('Ammar','Nammour',2016)
emp2=myclass('Max','Chrestopher',2023)
print(emp1)
print(emp1.yearsEmployed())
print(emp2)
print(emp2.yearsEmployed())


#print (object3.surname)
#print(object2.favorite[0])


from dataclasses import dataclass
@dataclass
class myclass2:
    name:str
    surname:str
    year:int


obj=myclass2('Ammar','Nammour',2016)
print(obj)
obj2=myclass2.year()
print(f'Name is {obj.name}, Surname is {obj.surname}, the year of employment is {obj.year}')
print(obj2)