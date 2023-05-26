class Négyzet ():
    def __init__(self):
        self.a = 0
    def ter(self):
        return self.a * self.a
    def ker(self):
        return self.a*4
    def iratas(self):
        return "A maga négyzetének a területe: "+ str(Négyzet.ter(self)) + "cm és kerülete: "+ str(Négyzet.ker(self)) +"cm²"

négyzet = Négyzet()
print("Az adatok centiméterben értendőek")
négyzet.a = int(input("Kérem adja meg az oldal hosszát: "))

Lista = []
Lista.append(négyzet)

for i in Lista:
    print(i.iratas())