Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = 2,3,65,2,52,4
>>> type(tup)
<class 'tuple'>
>>> t = (5,6,98,9,56,2,3)
>>> type(t)
<class 'tuple'>
>>> m = tuple()
>>> m
()
>>> temp = list(m)
>>> temp
[]
>>> temp.append(56)
>>> temp
[56]
>>> temp.extend([5,6,98,3,2,44,6,24])
>>> temp
[56, 5, 6, 98, 3, 2, 44, 6, 24]
>>> m = tuple(temp)
>>> m
(56, 5, 6, 98, 3, 2, 44, 6, 24)
>>> len(m)
9
m.count(6)
2
if 98 in m:
    print("It is present")

It is present
#Set
sets = {2,365,6,25,3,2,32,3,2,4}
sets
{32, 2, 3, 4, 6, 25, 365}
se = {}
type(se)
<class 'dict'>
se = set()
se
set()
set1 = {2,3,65,6,59,4,5,4,5621}
set2 = {5,6,9,2,4,2,325,3,25,2,3}
set1.union(set2)
{65, 2, 3, 4, 5, 6, 325, 9, 5621, 25, 59}
set1
{65, 2, 3, 4, 5, 6, 5621, 59}
set2
{2, 3, 4, 5, 325, 6, 9, 25}
set1.update(set2)
set1
{65, 2, 3, 4, 5, 6, 325, 9, 5621, 25, 59}
set1.intersection(set2)
{2, 3, 4, 325, 5, 6, 9, 25}
set1
{65, 2, 3, 4, 5, 6, 325, 9, 5621, 25, 59}
set1.intersection_update(set2)
set1
{2, 3, 4, 325, 5, 6, 9, 25}
set1 = {2,3,65,6,59,4,5,4,5621}
set1.difference(set2)
{65, 59, 5621}
set1.issuperset(set2)
False
set1.issubset(set2)
False
set1.isdisjoint(set2)
False
del set1
set1
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    set1
NameError: name 'set1' is not defined. Did you mean: 'sets'?
set2.remove(2)
set2
{3, 4, 5, 325, 6, 9, 25}
set2.remove(91)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    set2.remove(91)
KeyError: 91
set2.discard(91)
sets
{32, 2, 3, 4, 6, 25, 365}
sets.add(91)
sets
{32, 2, 3, 4, 6, 25, 91, 365}
set2.clear()
set2
set()
sets.pop()
32
