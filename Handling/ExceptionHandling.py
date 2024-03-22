#Exception Handling
'''try - logic
except - error(Exception)
else - code
finally - always execute'''
try:
    a = int(input("Enter the value.."))
    b = int(input("Enter the value.."))

    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    

except ValueError as msg:
    print("There is an error 404..")
except ArithmeticError as msg:
    print(msg)
except Exception as msg:
    print(msg)

else:
    print("Sum is:",add)
    print("Sub is:",sub)
    print("Mul is:",mul)
    print("Div is:",div)

finally:
    print("I'm always executed...")


