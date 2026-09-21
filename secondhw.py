#Задача 3.1
f = open('input.txt', 'r')
c = open('output.txt', 'w')
a =''
op = ''
for i in range(2):
  if i == 1:
    op = f.readline()
  if i == 0:
    a = f.readline().split()
if op == '*':
  c.writelines(f'Result of {op} operation with {a[0]} and {a[1]}:' + '\n')
  c.writelines(str(int(a[0])*int(a[1])))
if op == '+':
  c.writelines(f'Result of {op} operation with {a[0]} and {a[1]}:' + '\n')
  c.writelines(str(int(a[0])+int(a[1])))
if op == '/':
  c.writelines(f'Result of {op} operation with {a[0]} and {a[1]}:' + '\n')
  c.writelines(str(int(a[0])/int(a[1])))
if op == '-':
  c.writelines(f'Result of {op} operation with {a[0]} and {a[1]}:' + '\n')
  c.writelines(str(int(a[0])-int(a[1])))
c.close()
#Задача 3.2
a = int(input())
b = [i for i in range(2, a+1)]
c = []
for j in b:
    c.append(j)
    for k in range(2*j, a+1, j):
        if k%j == 0 and k in b:
            b.remove(k)
print(str(c)[1:-1])
#Задача 3.4
s = input().split()
for i in range(0, 2*(len(s)//2), 2):
    s[i], s[i+1] = s[i+1], s[i]
print(s)
#Задача 3.5
s = input().split()
a = 0
ans = 0
for i in range(len(s)):
    c = 0
    for j in range(i+1, len(s)):
        if s[j] == s[i] and j != '':
            c += 1
            s[j]=''
    if c> a:
        a = c
        ans = s[i]
print(ans)
#Задача 3.6
s = input().split()
for i in range(len(s)):
    c = 0
    for j in range(len(s)):
        if s[j] == s[i] and j != i:
            c = 1
    if c == 0:
        print(int(s[i]), end=' ')
