from rectangle import Rectangle
width=float(input('Enter the width of Rectangle please: '))
height=float(input('Enter the height of Rectangle please: '))
if width>height:
    a=width
    width=height
    height=a

myRectangle=Rectangle(width,height)
myRectangle.getWidth()
myRectangle.getHeight()
myRectangle.getArea()
myRectangle.getPerimeter()
myRectangle.getDiagonal()
