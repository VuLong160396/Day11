lenght, width = map(int, input('Input L and W: ').split())
print(lenght)
print(width)
import turtle
t = turtle.Turtle()
side = int(input('Side: '))
for i in range(side):
    t.fd(side*20)
    t.rt(360/side)
turtle.done()