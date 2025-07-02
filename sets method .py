sp = {"Rishu","Isha","Sola","Vibrant"}
si = {"Dhavanit","Rushi","Yash","Vibrant"}
print(sp.union(si))
# sp.intersection_update(si)
print(sp.issuperset(si))
print(sp.issubset(si))
o=sp.intersection(si)
print(o)
print(sp.isdisjoint(si))
f = sp.difference(si)
print(f)
sp.add("Tisu")
print(sp)
sp.update(si)
print(sp)
sp.remove("Sola")
print(sp)
u = sp.pop()
print(u)
print(sp)
q = {"Sae","wea","qq"}
q.clear()
print(q)
e = {"Ro","Se","Sa"}
print(e)
n = str(input("Enter Your option"))
print(n)
if n in e:
    print("yes")
else:
    print("no")
