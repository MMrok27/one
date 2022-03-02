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

