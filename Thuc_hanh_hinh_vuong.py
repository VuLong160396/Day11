import turtle
import math
t = turtle.Turtle()
t.pencolor('red')
#Khai báo các hàm
def chuyen_do_C(do_f):
    return (do_f - 32) / 1.8
def hinh_vuong(a):
    for i in range(4):
        t.fd(a)
        t.rt(90)
def da_giac_deu(n, width):
    angle = (n-2) * 180 / n
    for i in range(n):
        t.fd(width)
        t.rt(180 - angle)
def dien_tich():
    'Hàm tính diện tích hình tròn'
    return math.pi * r * r
def hinh_tron(r):
    t.hideturtle()
    t.pencolor('green')
    t.circle(r)
r = float(input('Nhập vào bán kính: '))
a = dien_tich()
print(f'Diện tích của hình tròn có bán kính = {r} là: {a}')
c = chuyen_do_C(100)
print(c)
hinh_vuong(100)
t.penup()
t.goto (200, 200)
t.pendown()
da_giac_deu(6, 100)
hinh_tron(r)
turtle.done()
