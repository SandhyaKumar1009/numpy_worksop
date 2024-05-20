# create a list as below
#output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]
d.append(e)
c.append(d)
output = []
output.append(a)
output.append(b)
output.append(c)
print(output)
