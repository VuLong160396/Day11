def print_message(message, count):
    for i in range(1, count + 1):
        print(message)
print_message('xin chào', 2)

def sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total
print('Tổng các số từ 1 đến 10: ', str(sum(1, 10)))
result1 = sum(1, 10)
print(result1)

def sum1(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    print(f'Tổng của số {start} đến {end} là: {total}')
sum1(1, 5)

##Đệ quy
def my_function(a):
    if a <0 :
        return 0
    return a + my_function(a - 1)
print(my_function(10))

for i in range(5):
    if i == 2:
        continue
        # print('add')
    print(i,end=' ')