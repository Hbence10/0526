class Diak ():
    def __init__(self):
        self.név = 0
        self.osztály = 0
        self.év = 0
    def ev(self):
        return 2023-self.év
    def köszönés(self):
        return "Szia "+self.név+" vagyok, a "+self.osztály+" osztályba járok, "+str(Diak.ev(self))+" éves vagyok. "


diak = Diak()
diak.név = input("Kérem adja meg a nevét: ")
diak.osztály = input("Kérem adja meg az osztályát: ")
diak.év = int(input("Kérem adja meg hogy mikor született: "))


Lista = []
Lista.append(diak)

for i in Lista:
    print(i.köszönés())