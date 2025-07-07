# f = open("te.txt","w")
# s = ["Rishu","Kiran","Sanju"]
# f.writelines(s)
# f.close()

f = open("te.txt","r")
while True:    
 sa = f.readline()
 if not sa:
  break
 print(sa)

# f = open("te.txt","w")
# aw = ["Rishu","Dhruv","Tech"]
# f.writelines(aw)
# f.close()