Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic = {"name":"khushi","age":25,"address":"Delhi"}
>>> dic
{'name': 'khushi', 'age': 25, 'address': 'Delhi'}
>>> dic["address"]
'Delhi'
>>> dic[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dic[0]
KeyError: 0
>>> dic.keys()
dict_keys(['name', 'age', 'address'])
>>> dic.values()
dict_values(['khushi', 25, 'Delhi'])
>>> dic.items()
dict_items([('name', 'khushi'), ('age', 25), ('address', 'Delhi')])
>>> dic.get("name")
'khushi'
>>> dic.clear()
>>> dic
{}
>>> del dic
dic
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dic
NameError: name 'dic' is not defined. Did you mean: 'dir'?
dic = {"name":"khushi","age":25,"address":"Delhi"}
dic.pop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 argument, got 0
dic.pop("age")
25
dic
{'name': 'khushi', 'address': 'Delhi'}
dic.popitem()
('address', 'Delhi')
d2 = {'b': 200, 'd': 400}
dic.update(d2)
dic
{'name': 'khushi', 'b': 200, 'd': 400}
d3 = {"subjects":{"maths":65,"english":96,"hindi":98,"science":100},"Record":[75,63,84,69,95]}
d3
{'subjects': {'maths': 65, 'english': 96, 'hindi': 98, 'science': 100}, 'Record': [75, 63, 84, 69, 95]}
d3["subjects"]["hindi"]
98
d3["Record"][4]
95
