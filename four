class Ksztalty():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogólnych kształtów"
    def pole(self):
        return self.x * self.y
    def obwod(self):
        return 2 * self.x + 2 * self.y
    def dodaj_opis(self, text):
        self.opis = text
    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik
class Kwadrat(Ksztalty):
    def __init__(self,x):
        self.x = x
        self.y = x
    def __str__(self):
            return 'Kwadrat o boku {}'.format(self.x)

kwadrat = Kwadrat(5)
print(kwadrat)

class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]
    
    
napis = Wspak('Reks')
print(napis.__next__())
for a in napis:
    print(a)

litery = (litera for litera in "Zdzisław")
print(litery)
print(next(litery))
print(next(litery))
