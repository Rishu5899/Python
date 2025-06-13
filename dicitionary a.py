d = {"Rishu": 54,"Urvi":41,"Dhruvi":52}
e = {"Raju": 42,"Tanisha":27, "Fenil":12}
d.update(e)
print(d)
d.pop("Rishu")
print(d)
d.popitem()
print(d)
g = d.keys()
print(g)
w = d.values()
print(w)
a = d.items()
print(a)
d["Divyesh"]= 21
print(d)
for c in d.values():
    print(c)
for c in d.keys():
    print(c)
for c in d.items():
    print(c)
x = d.copy()
print(x)
Watch ={"High Price" :{"Tommy":5000,"Rolex":100000,"Fossil":12000,"Samsung":25000}, "Medium":{"Titan":2000,"Sonata":2500},"Low":{"Fastrack":1500,"Firebott":800}}
print(Watch["High Price"]["Rolex"])
for s in Watch.items():
    print(s)
for q in Watch.values():
    print(q)