#factorial prgram

'''num = int(input("Enter the value to get factorial value.."))
product = 1
for i in range(1,num+1):
    product *= i

print("The factorial is..",product)'''


#fibonacci series - 0 1 1 2 3 5 8 13 21......

'''d_1 = 0
d_2 = 1

num = int(input("Enter the terms.."))
print(d_1 , d_2 ,end = " ")
for i in range(2,num+1):
    
    d_3 = d_1 + d_2
    
    print(d_3,end = " ")
    
    d_1 = d_2
    d_2 = d_3'''
    
#reverse the number

'''num = int(input("Enter the number.."))
rev = 0
while num > 0:
    rem = num%10
    rev = rev*10 + rem
    num//=10
print(rev)'''

#Prime number

num = int(input("Enter the number.."))
prime = False
for i in range(2,num//2+1):
    if num%i == 0:
        prime = False
        break
    else:
        prime = True
if prime:
    print("number is prime")
else:
    print("number is not prime")
        











    
  
    
    
