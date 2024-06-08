# class person:
#     countray='Syria'
#     language='Arabic'
#     def __init__(self,fName='firstName',lName='lastName'):
#         self.firstName=fName
#         self.lastName=lName

#     def __str__(self) -> str:
#         return f'my name is {self.firstName} {self.lastName}'
# Ammar=person('Ammar','Nammour')
# print(Ammar.countray)
# print(Ammar.language)
# print(Ammar.__dict__)
# print(Ammar)

class person:
    gender='Female'
    idNumber='testId'
    def __init__(self,fName,lName,age):
        self.firstname=fName
        self.lastName=lName
        self.Age=age
    
    def __str__(self):
        name=self.fullName()
        return name

    def fullName (self):
        return self.firstname + ' ' + self.lastName

class employee(person):
    def __init__(self, fName, lName, age,job,pay):
        super().__init__(fName, lName, age)
        self.job=job
        self.pay=pay

    def giveRaise(self,bonus):
        self.pay+=0

angella=person('Angella','Doe','67')
print(angella.gender)
print(angella.firstname)
print(angella.fullName())
print(angella)

Joo=employee('Joo','Doe',30,'python dev',40000)
print(Joo.lastName)
print(Joo.firstname)
print(Joo.fullName())
print(Joo.job)
print(Joo.pay)

class manager(employee):
    pass