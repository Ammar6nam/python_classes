import math
class Rectangle:
    def __init__(self,width,height) -> None:
        self.width=float(width)
        self.height=float(height)
        
    def getArea (self):
        print(f'The square of the Rectangle is: {float(self.width)*float(self.height)}')
    
    def getPerimeter(self):
        print(f'The perimeter of Rectangle is: {2*float(self.width)+2*float(self.height)}')
    
    def getDiagonal(self):
        print(f'The Diagonal of Rectangle is: {math.sqrt((float(self.width))**2+(float(self.height))**2)}')
    
    def getWidth (self):
        print(f'The Width is: {float(self.width)}')
    
    def getHeight(self):
        print(f'The Height is: {float(self.height)}')


