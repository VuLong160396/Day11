def greeting(name):
    print(f'xin chào {name}')

greeting('Long')
#sử dụng hàm docstring
print(greeting.__doc__)
#hàm nặc danh
sum = lambda num1, num2: num1 + num2
print('Tổng:', sum(3,5))
def my_function():
    global x
    x = "biến toàn cục, được khai báo trong hàm!"
    print(x)
my_function()
# print(x)

def sum(*matrix):
    s = 0
    for i in range(len(matrix)):
        s += matrix[i]
    return s
# print(len(3))
d = sum(1,2,3)
# print(len(matrix))
print(d)
def max(a,b):
    if a >= b:
        return print(a)
    else:
        return print(b)
max(5,3)
# print(p)
def max(text):
    lenght = len(text)
    print('Độ dài của text là: ',lenght)
max('Long')
#Hàm trả về nhiều giá trị 
def calculator(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    print(sum, sub, mul)
x = calculator(10, 3)
print(x)
# a = None
calculator(1,2)