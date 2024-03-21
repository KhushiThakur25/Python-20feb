#Zip
name = ["Ram","Aman","Om","Yash","Hariom"]
Sir_name = ["Tyagi","Thakur","Singh","Sharma","Mishra","Gupta"]
#zip(name,Sir_name)
print(list(zip(name,Sir_name)))


#enumerate
for i in name:
    print(i)

for i in enumerate(name,101):
    print(i)

#map
def c_to_f(c):
    return 9/5*c + 32

def k_to_m(k):
    return k*1000
temp_c = [23.2,56.2,123.1,85.3,42.6]
k = [2,3,56,8,9,4]
#map(Func_name,iterable_name)
print(list(map(c_to_f,temp_c)))


#filter
def even(n):
    return n%2 == 0

def odd(n):
    return n%2 != 0


li = [2,3,56,8,9,4]

print(list(filter(even,li)))
print(list(filter(odd,li)))















