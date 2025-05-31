y = [5,3,6,4,2]
print(y)
y.append(1)
print(y)
y.sort()
print(y)
y.sort(reverse=True)
print(y)
y.reverse()
print(y)
print (y.index(3))
print(y.count(5))
y.insert(3,65)
print(y)
z = [4,2,5,7,12]
#for joining  two list  
# y.extend(z)
# print(y)
# other way of joining list
f = y + z
print(f)