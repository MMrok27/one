# a = 6
# b = 5
#
# if a > b:
#     print("liczba a jest większa od b")
# elif a < b:
#     print("liczba b jest większa od a")
# else:
#     print("liczba a jest równa b")

# a = input("wczytaj liczbe: ")
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))

# a = input("wczytaj liczbe 1: ")
# b = input("wczytaj liczbe 2: ")
# c = input("wczytaj liczbe 3: ")
# d = input("wczytaj liczbe 4: ")
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
#
# if (a > b) & (c > d):
#     print("liczba a jest większa od b i liczba c jest większa od d")
# else:
#     print("liczba a jest mniejsza od b lub liczba c jest mniejsza od d")

# for a in range(0,7,1):
#     print(a)

# lista = ["a", 3, 4, 5.6]
# for a in lista:
#     print(a)
# else:
#     print("wyświetlone zostały elementy z listy")
# licznik = 0

# while licznik != 11:
#     print(licznik)
#     licznik += 1

# lista = [4, 6, 2, 5, 3, 9, 8, 7]
# a = input("podaj liczbe: ")
# licznik = 0
# while licznik != len(lista):
#     if int(a) - lista[licznik] == 0:
#         print("liczba " + str(a) + " - " + str(lista[licznik]) + " = 0")
#         break
#     else:
#         licznik += 1
# else:
#     print("żadna z wartosci")

# lista1 = [1,2,3,4,5,6,7,8]
# lista2 = [9,10,1,2]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# a = input("wczytaj liczbe 1: ")
# b = input("wczytaj liczbe 2: ")
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a / b
#     print(wynik)
# except ZeroDivisionError:
#     print("sussy baka, nie dziel przez 0")
# except ValueError:
#     print("sussy baka, nie wczytano liczby całkowitej")

lista = [1,2,3,10]
slownik = {'k1':2 , 'k2':10}
slownik['k3']=6;
print(slownik['k3'])

import math


# lista = []
# for x in range(0, 10):
#     lista.append(x**2)
# print(lista)
#
# list2 = [x**2 for x in range(0, 10)]
# print(list2)
#
# list3 = [3**x for x in range(0, 6)]
# print(list3)
#
# list4 = []
# for x in list2:
#     if x % 2 == 1:
#         list4.append(x)
# print(list4)
#
# list5 = [x for x in list2 if x % 2 == 1]
# print(list5)

# lista = []
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a, b))
# print(lista)
#
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# slownik = {"PZU": "Powszechny Zakład Ubezpieczeń", "ZUS": "Zakład Ubezpieczeń Społecznych",
#            "PKO": "Powszechna Kasa Oszczędności"}
# print(slownik)
# slownik_odwr = {}
# for key, value in slownik.items():
#     slownik_odwr[value] = key
# print(slownik_odwr)
# slownik2 = {value: key for key, value in slownik.items()}
# print(slownik2)

# def rownaniek(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("Brak rozwiązań")
#         return -1
#     elif delta == 0:
#         print("Jedno rozwiązanie")
#         x = (-b) / (2 * a)
#         return x
#     else:
#         print("Dwa rozwiązania")
#         x1 = ((-b) - math.sqrt(delta)) / (2 * a)
#         x2 = ((-b) + math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
#
# print(rownaniek(6, 1, 3))
# print(rownaniek(1, -2, 1))
# print(rownaniek(1, 4, 1))


# def iseven(a):
#     if a % 2 == 0:
#         print("Parzysta")
#     else:
#         print("Nieparzysta")
#
#
# iseven(420)
# iseven(69)

def dlugosc_odc(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(dlugosc_odc())
print(dlugosc_odc(1, 2, 3, 4))
print(dlugosc_odc(2, 2, y2=2, x2=1))
print(dlugosc_odc(y1=2, x1=5, y2=2, x2=1))
print(dlugosc_odc(y2=1, x2=1))


def ciag(*liczby):
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
        for i in liczby:
            suma += i
        return suma


print(ciag())
print(ciag(1))
print(ciag(1, 2, 3, 4))

def cl(** rzeczy):
    for cos in rzeczy:
        print("to jest")
        print(cos)
        print("co lubie")
        print(rzeczy[cos])

cl(gry=['Terraria','MGR:R'])

######################ZAD 1################################
import random

lista = [1-x for x in range(1, 11)]
print(lista)

listb = [4**x for x in range(0, 6)]
print(listb)

listc = [x for x in listb if x % 2 == 0]
print(listc)

######################ZAD 2################################



list1 = [random.randint(1, 100) for x in range(0, 10)]
print(list1)

list2 = [x for x in list1 if x % 2 == 0]
print(list2)

######################ZAD 3################################
zakupy = {"mleko": "szt"}
