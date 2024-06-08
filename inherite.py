class car:
    year='2015'
    color='Black'
    material='Iron'
    name='Toyota'

    def getName(self):
        print(self.color+self.year)
        return self.color+self.year

class Corola(car):
    pass

car_a=car()
car_b=car()

corollaA=Corola()
CorollaB=Corola()

# print(car_a.color)
# print(car_b.color)

# print(corollaA.color)
# print(CorollaB.color)
# print(corollaA.getName())

class corolla4x4(car):
    color='red'
    def getName(self):
        # return super().getName()
        print('test')
    def getColor (self):
        print('nice color! ')


class furniture:
    chairType='leather'
    chairDesign='topnotch'

corollaA=corolla4x4()
CorollaB=corolla4x4()

print(car_a.color)
print(car_b.color)

print(corollaA.color)
print(CorollaB.color)
print(corollaA.getName())
print(corollaA.getColor())
