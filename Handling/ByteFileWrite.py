file = open('img23.jpg','rb')
file1 = open('img232.jpg','wb')
data = file.read()
file1.write(data)
file.close()

