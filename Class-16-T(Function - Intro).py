def add():
    x = 56
    y = 14
    global z
    z = x+y
    print("Sum of x and y is",z)

print(z)
add()

#Arguments
# 1.positional arguments
# 2.default arguments
# 3.keyword arguments
# 4.variable-length arguments
# 4.1 arbitrary arguments
# 4.2 arbitrary keyword arguments

#.positional arguments
def add(x,y,q):
    z = x+y+q
    print(z)

add(20,30,61)

#keyword arguments
def add(a,b,c):
    z = a+b+c
    print(z)
add(a = 2,b = 6,c = 8)
add(b = 6,a = 8,c = 2)
add(x = 5,y = 6,z = 3)

#default arguments
def add(a = 1,b = 32,c = 68):
    z = a+b+c
    print(z)

add(5,6,2)#13
add(2,3)#
add(8)#
add()#100

#variable-length arguments
def add(*args):
     print(sum(args))
# it return tuple
add(2,3,65,9,6,3,1)

def add(**kwargs):
    print(kwargs)
add(a = 23,b = "khushi",c=2.3)
#it returns dictionary

def add():
    x = 52
    y = 65
    z = x+y
    
    return x,y,z

a,b,c = add()
print(a,b,c)















    
