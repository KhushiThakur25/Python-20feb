st = "There is a flower pot"
#program for even length words
st = st.split()
for i in st:
    if len(i)%2 == 0:
        print(i)
#program for reverse the string

st = st.split()
st = st[::-1]
print(" ".join(st))

    
