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
  c.write(str(int(a[0])*int(a[1])))
if op == '+':
  c.write(str(int(a[0])+int(a[1])))
if op == '/':
  c.write(str(int(a[0])/int(a[1])))
if op == '-':
  c.write(str(int(a[0])-int(a[1])))
c.close()
