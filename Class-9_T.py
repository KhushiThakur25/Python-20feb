Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "Hello world"
st[6]
'w'
a = str()
a
''
st.lower()
'hello world'
st.upper()
'HELLO WORLD'
st.title()
'Hello World'
st.capitalize()
'Hello world'
"Hello"=="hello"
False
"Hello".casefold()=="hello".casefold()
True
st.islower()
False
st.isupper()
False
False
False



st.istitle()
False
len(st)
11
st[5]
' '
st.count("l")
3
st.strip()
'Hello world'
st = "Hello world   "
st.rstrip()
'Hello world'
>>> st = "    Hello world"
>>> st.strip()
'Hello world'
>>> st = "*****Hello world"
>>> st.strip()
'*****Hello world'
>>> st.strip("*")
'Hello world'
>>> st = "this is a python programming language."
>>> st.split()
['this', 'is', 'a', 'python', 'programming', 'language.']
>>> st.replace("l","q")
'this is a python programming qanguage.'
>>> st = "ashgdasdjashddasdsa"
>>> st.replace("a","q",3)
'qshgdqsdjqshddasdsa'
>>> st = "this is a python programming language."
>>> a = st.split()
>>> a
['this', 'is', 'a', 'python', 'programming', 'language.']
>>> " ".join(a)
'this is a python programming language.'
>>> "-".join(a)
'this-is-a-python-programming-language.'
