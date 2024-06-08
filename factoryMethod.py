class vehicle:
    @staticmethod

    def factory(type):
        if type =='Car':
            return Car()
        if type=='Bike':
            return Bike()
        if type =='Airplane':
            return Airplane()
        if type=='Whale':
            return Whale()
        
class Car:
    def start(self):
        print('The car is driving...')

class Bike:
    def start(self):
        print('The bike is riding...')

class Airplane:
    def start(self):
        print('The plane is flying...')

class Whale:
    def start(self):
        print('The whale is swimming...')


car=vehicle.factory('Car')


# class Engine:
#     @staticmethod
#     def __init__(type) -> None:
        
#         print(f'The engin type is {type}...')
#         pass
#     @staticmethod
#     def start():
#         print('The engin is running...')
# a=Engine('Gas')
# Engine.start()


# class Engine2:
#     def start (self):
#         print('The engine Num_2 is running...')

# engine=Engine2()
# engine.start()