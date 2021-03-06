import turtle
t = turtle.Turtle()
def hcn(dai, rong):
    for i in range(2):
        t.fd(dai)
        t.left(90)
        t.fd(rong)
        t.left(90)
def tam_giac(canh):
    for i in range(3):
        t.fd(canh)
        t.left(120)
        t.fd(canh)
def ong_khoi(canh1, canh2):
    t.left(90)
    t.fd(canh1)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(canh2)
def move_cursor(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def than_cay(dai):
    t.fd(dai)
    t.rt(85) 
    t.fd(dai * 5)
    t.rt(95)
    t.fd(dai * 3)
    t.rt(95)
    t.fd(dai * 5)
    t.rt(85)
    t.fd(dai)

if __name__ == '__main__':
    t.speed(10)
    t.fillcolor('yellow')
    t.begin_fill()
    hcn(200, 100)
    move_cursor(75, 0)
    t.end_fill()
    t.fillcolor('white')
    t.begin_fill()
    hcn(50, 50)
    t.end_fill()
    move_cursor(50, 100)
    t.fillcolor('red')
    t.begin_fill()
    tam_giac(50)
    t.end_fill()
    move_cursor(75, 145)
    ong_khoi(40, 25)
    move_cursor(75, 205)
    t.fd(15)
    move_cursor(70, 220)
    t.fd(20)
    move_cursor(250, 100)
    t.lt(90)
    t.fillcolor('green')
    t.begin_fill()  
    tam_giac(20)
    move_cursor(250, 55)
    tam_giac(25)
    move_cursor(250, 0)
    tam_giac(30)
    t.end_fill()
    t.fillcolor('brown')
    t.begin_fill()
    than_cay(10)
    t.end_fill()

    
    move_cursor(-100, 55)
    t.fillcolor('teal')
    t.begin_fill()       
    tam_giac(20)
    move_cursor(-100, 0)
    tam_giac(30)

    move_cursor(-100, -65)
    tam_giac(35)
    t.end_fill()

    t.fillcolor('brown')
    t.begin_fill()
    than_cay(5)
    t.end_fill()

    move_cursor(200, 200)
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    turtle.bgcolor('wheat')
    t.pensize(5)
    t.shape('turtle')
    print(t.position())
turtle.done()