Dic = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'zero':'0'}

num = input("Enter the numbers")
#one three five nine
num = num.split()
result = []
for val in num:
    result.append(Dic.get(val))
print(" ".join(result))
    
