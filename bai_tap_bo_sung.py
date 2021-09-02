import turtle
from typing import Sized
t = turtle.Turtle()
def circle(r):
    t.circle(r)
    t.left(360//quanty)
def square(lenght):
    for i in range (4):
        t.fd(lenght)
        t.lt(90)
    t.lt(360//quanty)
def rectangle(lenght, width):
    for i in range(2):
        t.fd(lenght)
        t.lt(90)
        t.fd(width)
        t.lt(90)
    t.lt(360//quanty)
def equilateral(lenght):
    for i in range (3):
        t.fd(lenght)
        t.lt(120)
        t.fd(lenght)
    t.lt(360//quanty)

def pentagon(side):
    for _ in range(5):
        t.fd(side)
        t.rt(360/5)
    t.lt(360//quanty)
def fill_color(color):
    t.fillcolor(color)
    t.begin_fill()
def one_side():
    if choose_shape == 1:
        lenght = int(input('Input Side: '))
        fill_color(color)
        for j in range(quanty):
            square(lenght)
        t.end_fill()
    elif choose_shape == 4:
        lenght = int(input('Input Side: '))
        fill_color(color)
        for i in range(quanty):
            equilateral(lenght)
        t.end_fill()
    elif choose_shape == 3:
        side = int(input('Input Side: '))
        fill_color(color)
        for i in range(quanty):
            pentagon(side)
        t.end_fill()
    elif choose_shape == 0:
        fill_color(color)
        r = int(input('Input R: '))
        for i in range(quanty):
            circle(r)
        t.end_fill()
    # t.position()
#_______________________MAIN______________________
if __name__ == '__main__':
    count = 0
    # quanty = 0
    # color = 0
    t.speed(10)
    while count < 3:
        try:
            choose_shape = int(input('Shape (0.circle 1.square 2.rectangle 3.pentagon 4.equilateral 5.triangle 6.oval 7.heart): '))
        except ValueError:
            print('Shape Invalid')
            count += 1
            continue
        if choose_shape <= 6:
            break 
    list_shape = ['circle', 'square', 'rectangle', 'pentagon', 'equilateral', 'oval', 'heart']
    shape = print(f'Shape chosen: {list_shape[choose_shape]}') if choose_shape <= 6 else print('Shape I') #Choice Shape
    quanty = int(input('Quanty of shape: '))                                                              #Choice Quanty
    color = input('Input color: ')                                                                        #Choice Color
#______________________Drawing Shape:______________________0-->4

    if choose_shape == 2:
        lenght, width = map(int, input('Input L and W: ').split())
        fill_color(color)
        for j in range(quanty):
            rectangle(lenght, width) 
        t.end_fill()
    else:
        one_side()
    t.position()
    turtle.done()