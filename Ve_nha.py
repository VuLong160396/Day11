import turtle
t = turtle.Turtle()
def hcn(dai, rong):
    for i in range(2):
        t.fd(dai)
        t.rt(90)
        t.fd(rong)
        t.rt(90)
def cua_so(dai, rong):
    t.fillcolor('white')
    t.begin_fill()
    hcn(dai/3 , rong/3)
    t.end_fill()
def move_cursor(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
if __name__ == '__main__':
    t.speed(10)
#khối 1
    t.fillcolor('pink')
    t.begin_fill()
    hcn(50, 100)
    t.end_fill()
    move_cursor(50/3, -100/3)
    cua_so(50, 100)
    move_cursor(0, 100)
#khối 2
    t.fillcolor('purple')
    t.begin_fill()
    hcn(50, 100)
    t.end_fill()
    move_cursor(50/3, 2*100/3)
    cua_so(50,100)
    move_cursor(-50, 100)
#khối 3
    t.fillcolor('green')
    t.begin_fill()
    hcn(50, 100)
    t.end_fill()
    move_cursor(-2*50/3, 2*100/3)
    cua_so(50, 100)
    move_cursor(-50, 0)
#khối 4
    t.fillcolor('teal')
    t.begin_fill()
    hcn(50, 100)
    t.end_fill()
    move_cursor(-2*50/3, -100/3)
    cua_so(50, 100)

    move_cursor(50, 0)
    t.fillcolor('blue')
    t.begin_fill()
    hcn(100, 100)
    t.end_fill()
    move_cursor(50 + 100/3 , -100/3)
    cua_so(100, 200)
    a = list(t.pos())
    print(type(a))
    b = a[0]
    c = a[1]
    print(b, ' ',c)
turtle.done()