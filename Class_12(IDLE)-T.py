Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [2,3,5,6,2,3,2,3,1]
>>> li
[2, 3, 5, 6, 2, 3, 2, 3, 1]
>>> lis = list()
>>> lis
[]
>>> li[3]
6
>>> li[6]
2
>>> len(li)
9
>>> lis.append(56)
>>> lis
[56]
>>> lis.append(63)
>>> lis
[56, 63]
>>> lis.append(96)
>>> lis
[56, 63, 96]
>>> lis.index(63)
1
lis[1] = 65
lis
[56, 65, 96]
lis.insert(1,60)
lis
[56, 60, 65, 96]
li.count(2)
3
sum(li)
27
max(lis)
96
min(lis)
56
sum(lis)
277
sum(lis)/len(lis)
69.25
liss = [23,56,41]
del liss
liss
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    liss
NameError: name 'liss' is not defined. Did you mean: 'lis'?
liss = [23,56,41]
liss.clear()
liss
[]
li.remove(3)
li
[2, 5, 6, 2, 3, 2, 3, 1]
li.remove(3,2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    li.remove(3,2)
TypeError: list.remove() takes exactly one argument (2 given)
li.pop()
1
li.popitem(2)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    li.popitem(2)
AttributeError: 'list' object has no attribute 'popitem'
li.sort()
li
[2, 2, 2, 3, 3, 5, 6]
li.sort(reverse = True)
li
[6, 5, 3, 3, 2, 2, 2]
lis.reverse()
lis
[96, 65, 60, 56]
li.extend(lis)
li
[6, 5, 3, 3, 2, 2, 2, 96, 65, 60, 56]
g = li
g
[6, 5, 3, 3, 2, 2, 2, 96, 65, 60, 56]
li
[6, 5, 3, 3, 2, 2, 2, 96, 65, 60, 56]
g[1] = 51
g
[6, 51, 3, 3, 2, 2, 2, 96, 65, 60, 56]
li
[6, 51, 3, 3, 2, 2, 2, 96, 65, 60, 56]
m.copy(li)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    m.copy(li)
NameError: name 'm' is not defined
m = li.copy()
m
[6, 51, 3, 3, 2, 2, 2, 96, 65, 60, 56]
m[0]=100
m
[100, 51, 3, 3, 2, 2, 2, 96, 65, 60, 56]
li
[6, 51, 3, 3, 2, 2, 2, 96, 65, 60, 56]
m[2:6:1]
[3, 3, 2, 2]
m[::-1]
[56, 60, 65, 96, 2, 2, 2, 3, 3, 51, 100]
for i in range(len(li)):
    print(li[i])

6
51
3
3
2
2
2
96
65
60
56
for i in li:
    print(i)

6
51
3
3
2
2
2
96
65
60
56
sums = 0
for i in li:
    sums+=i

sums
346
