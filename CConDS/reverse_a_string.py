
#let us say that the inout array is given as vector s

s = ['a','b','v','c','x','d']
lengthofarray = len(s)
i =0
while i < lengthofarray:
    s[lengthofarray-1],s[i] = s[i],s[lengthofarray-1]
    i+=1
    lengthofarray-=1

print(s)

