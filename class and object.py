class person:
    name = "Rishu"
    Age = "21"
    profession = "Student"
    def info(self):
        print(f"{self.name}  Age is {self.Age} and profession is {self.profession}")
s = person()
q = person()
t = person()
q.name = "DJ"
q.profession = "party DJ"
t.name = "JD"
t.profession = "Engineer"
s.name = "Isha"
s.profession = "Recepenist"
# print(s.name,"is",s.profession,".")
s.info()
q.info()
t.info()