# Functions with numeric inputs
#Author:Yoshiki Hoshinaga
#Date: May 21 2020
#Title: Problem Set2, Part 2
#


#problem 1
def yahoo(x,y):
    x = x + 6
    z = x +y
    y = z % 3
    print('yahoo', x, y)
    return x
x = 11
y = 5
print(x, y)
x = yahoo(x,y)
print (x,y)
yahoo(y,x)
print(x,y)

#problem 2
def foo(a,b):
    b = b - 2
    a = a - b
    print('foo', a, b)
    return a
a = 5
b = 3
print(a,b)
a = foo(a,b)
print(a,b)
foo(b,a)
print(a,b)

#problem 3
def wow(a):
    b = a  * 2
    print('wow', a, b)
    return b

def yay(b):
    a = wow(b) + wow(b+2)
    print('yay:',a, b)
    return a
a = 4
b = 3
print(a,b)
b = wow(b)
print(a, b)
yay(a)
print(a,b)
