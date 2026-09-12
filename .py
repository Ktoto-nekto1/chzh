# Задача 1.1
print("Введите 1, если будете вводить сначала числа, а затем знак и 2, если число, знак, число: ")
a = int(input())
if a == 1:
    b = int(input())
    c = int(input())
    d = input()
    if d == '+': print(b+c)
    if d == '-': print(b-c)
    if d == '*': print(b*c)
    if d == '/': print(b/c)
if a == 2:
    c = input().split()
    a = int(c[0])
    b = int(c[2])
    if c[1] == '+': print(a+b)
    if c[1] == '-': print(a-b)
    if c[1] == '*': print(a*b)
    if c[1] == '/': print(a/b)
# Задача 1.2
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
n = int(input())
a=[]
for i in range(1, n+1):
    s = fibo(i)
    a.append(s)
print(a)
# Задача 1.3
print('Введите число, которое нужно найти в последовательности: ')
a = int(input())
x = a
print('Введите последовательность и end в конце ')
m = []
while a != 'end':
    a = input()
    m.append(a)
for i in range(len(m)-1):
    if m[i] == str(x):
        print(i+1)
