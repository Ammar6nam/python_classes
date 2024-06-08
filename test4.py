# class student:
#     role='Teacher'
#     def __init__(self,name) -> None:
#         self.name=name

#     def __new__(cls) :
#         print('Step1. Creating instance')
#         pass

# s1=student('Paul')
# s2=student('Ammar')
# s3=student('Anna')

# # print(id(s1))
# # print(id(s2))
# # print(id(s3))

# print(s1.role,s1.name)
# s2.role='student'
# print(s2.role,s2.name)

# student.role='Test'
# print(s1.role,s1.name)
# print(s2.role,s2.name)
# print(s3.role,s3.name)

class A(object):
    __instance=None
    def __new__(cls) :
        print('Step1. Creating instance')
        if not cls.__instance:
            return super().__new__(cls)
        
    def __init__(self) -> None:
        self.whatever=self.__instance

    def __str__(self) -> str:
        print('Step2. Init is called: ')
        self.whatever=self.single

    def __hash__(self) -> int:
        return 123000202

obj=A()
obj2=A()
obj3=A()
obj4=A()

print(id(obj))
print(id(obj2))
print(obj==obj2)
print(obj is obj2)