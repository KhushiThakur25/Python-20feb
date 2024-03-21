#Calculator

def add(a,b):
    z = a+b
    print("Sum of a and b is",z)
def sub(a,b):
    z = a-b
    print("Subtract of a and b is",z)    
def mul(a,b):
    z = a*b
    print("Multiplication of a and b is",z)   
def div(a,b):
    z = a/b
    print("Division of a and b is",z)  
if ch == "1":
    add(a,b)
elif ch == "2":
    sub(a,b)
elif ch == "3":
    mul(a,b)
elif ch == "4":
    div(a,b)
else:
    print("Invalid choice..")   
print("""1.Add
2.Subtract
3.Multiplication
4.Division..""")
ch  = input("Enter your choice to perform operation..")
a = int(input("Enter the first operand.."))
b = int(input("Enter the second operand.."))
