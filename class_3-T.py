'''a = 56
b = 95
c = 92
if a > b and a > c:
    print("A is greatest..")
elif b > a and b > c:
    print("B is greatest..")
else:
    print("C is greatest..")'''

#loops


'''which is used to iterate a single code many times
types of loops in python:
    2 types
    1.for loop--when we know the number of iteration
    2.while loop--when we don't know the number of iteration
    common syntax-
    -initialization
    -termination
    -updation

    range(start,stop,step)
    bydefault start value is 0
    bydefault step value is 1'''

'''for i in range(2,8,2):
    print(i)
    
j = 0
while j < 6:
    print(j)
    j += 1


n = int(input("Enter the number for table."))

for i in range(1,11,1):
    print(f"{n} * {i} = {n*i}")

m = 1
while m < 11:
    print(f"{n} * {m} = {n*m}")
    m += 1'''

#************
for i in range(50):
    print("*",end = "")

j = 1
sums = 0
while j < 11:
    sums = sums + j
    j += 1

print(sums)
