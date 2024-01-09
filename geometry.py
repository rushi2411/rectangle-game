
import turtle
from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fall_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        length = self.upright.x - self.lowleft.x
        breadth = self.upright.y - self.lowleft.y
        return abs(int(length * breadth))


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x,self.lowleft.y)
        canvas.pendown()

        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)


class GuiPoint(Point):
    def draw(self,canvas,size=5,color='red'):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size,color)
        turtle.done()

if __name__=="__main__":

    my_rectangle = GuiRectangle(Point(randint(0, 100), randint(0, 100)), Point(randint(150, 190), randint(150, 190)))

    print("rectangle coordinates: ", my_rectangle.lowleft.x, ",", my_rectangle.lowleft.y, "and", my_rectangle.upright.x, ",", my_rectangle.upright.y)

    user_point = GuiPoint(int(input("enter X coordinate: ")), int(input("enter Y coordinate: ")))

    print("point fall in rectangle: ",user_point.fall_in_rectangle(my_rectangle))

    print("area of rectangle:", my_rectangle.area())

    my_turtle = turtle.Turtle()
    my_rectangle.draw(canvas=my_turtle)
    user_point.draw(canvas=my_turtle)



