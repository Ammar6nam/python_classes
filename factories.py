def vehicleFactory(hasWheels,numWheels):
    class vehicle:
        # def test():
        #     pass
        def __init__(self,**kwargs) -> None:
            self.hasWheels=hasWheels
            self.numWheels=numWheels
            self.properties=kwargs
        pass
    return vehicle
    
truck=vehicleFactory(True,4)
truck1=truck(name='Mercedes',tonnage=50000)
formula=vehicleFactory(True,4)
formula1=formula(name='Ferrari',engineType='Non Electric')
print(type(truck))
# print(type(formula.test))
print(truck1.properties['name'])
print(formula1.properties)
print(type(truck1))

anylist=[]
print(type(anylist))

newObj=type('New Class',(object,),dict(var1='GeekForGeeks',b=2009))
print(type(newObj.var1))
print(type(newObj.b))
class NewClass:
    def __init__(self,var1,b) -> None:
        self.var1=var1
        self.b=b

newObj2=NewClass('GeekForGeeks',2009)
print(type(newObj2.var1))
print(type(newObj2.b))
print(type(newObj))
print(type(newObj2))