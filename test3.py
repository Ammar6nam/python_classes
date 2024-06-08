class car:
    color= 'red'
    name= 'Toyota'

    def fullName (self,year,otherName=""):
        self.year=year
        self.otherName=otherName
        print(self.color+self.name+otherName)

car_a=car()
car_b=car()
# print(car_a.color)i=0
j=0
while j<1:
        number1=int(input('First number: '))
        number2=int(input('second number: '))
        if number1 > 100 and number1 %2 !=0 and number2 % 2 !=0 and number1 % number2 == 0:
            i+=1
            print('you earned a point! ',' ',sep='\n')
            continue
        else:
            print("You've made a mistake!",' ',sep='\n')
        break

print (f'You gathered {i} point(s)!',' ',sep='\n')
# print(car_b.color)
# print('\n')
# print(car_a.name)
# print(car_b.name)

car_a.fullName(1991)
# car_b.fullName(2000)

# print(car_a.year)
# print(car_a.otherName)

print(car_a.__dict__,'Sorry')
print(car_b.__dict__,'OKK')