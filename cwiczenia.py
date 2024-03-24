# 2.1.1.6 LABORATORIUM: Funkcja print()


print('Wlazl kotek na plotek')
print('Bartlomiej')
#print(Bartlomiej)
"""Traceback (most recent call last):
  File "C:/TEB Edukacja Python/Wprowadzenie do pythona/cwiczeniaLab.py", line 3, in <module>
    print(Bartlomiej)
NameError: name 'Bartlomiej' is not defined"""
#print'Bartlomiej' # missing parenthesis in call to 'print'. Did you mean print(...)?
print("Bartlomiej")
#print('Bartlomiej') print('Bartlomije') invalid syntax
print('Bartlomiej')
print('Bartlomije')
print('Bartlomiej')

#2.2.1.11 LABORATORIUM: Literały - ciągi znaków
print("\"Ucze sie\"\n\"\"jezyka\"\"\n\"\"\"Python\"\"\"")

#2.4.1.7 LABORATORIUM: Zmienne

pomaranczowy_krol = 3
agnieszka = 5
adam = 6

print(pomaranczowy_krol, agnieszka, adam, sep=',')

pomaranczy_razem = pomaranczowy_krol + agnieszka + adam
print(pomaranczy_razem)
print(f'Calkowita liczba pomaraczny: {pomaranczy_razem}')

#2.4.1.9 LABORATORIUM: Zmienne: prosty konwerter
kilometry = 12.25
mile = 7.38

mile_na_kilometry =  mile / 1.61
kilometry_na_mile =  kilometry * 1.61

print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")

#2.4.1.10 LABORATORIUM: Operatory i wyrażenia
x =  1
x = float(x)
y = 3 * x ** 2 - 2 * x ** 2 + 3 * x - 1 
print("y =", y)


# 2.5.1.2 LABORATORIUM: Komentarze

#Ten program oblicza liczbę sekund w danej liczbie godzin.
#ten program został napisany dwa dni temu

a = 2 #liczba godzin
sekundy = 3600 #liczba sekund w 1 godzinie

print("Godzin: ", a) # wyświetla ilość godzin
print("Sekund w godzinach: ", a * sekundy)  # wyswietla ilość sekund w zadanej liczbie godzin

print("Do widzenia")
# to jest koniec programu, który oblicza liczbę sekund w 3 godzinach

#2.6.1.9 LABORATORIUM: Proste operacje wejścia i wyjścia

a = float(input('Podaj liczbe a: '))
b = float(input('Podaj liczbe b: '))

wynikDodania = a + b
wynikOdejmowania =  a -b
wynikMnozenia = a *b
wynikDzielenia = a / b

print(wynikDodania)
print(wynikOdejmowania)
print(wynikMnozenia)
print(wynikDzielenia)

print("\nI to by było na tyle!")

#2.6.1.10 LABORATORIUM: Operatory i wyrażenia


x = float(input("Wprowadź wartość dla x: "))

y = 1 /(x + 1 /(x + 1 / (x + 1/x)))

print("y =", y)

#2.6.1.11 LABORATORIUM: Operatory i wyrażenia

h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))


godzinaWM = h * 60
godzinaWMinutach = godzinaWM + m
godzinaKoncowaWMinutach = godzinaWMinutach + d
godzinaKoncowa = godzinaKoncowaWMinutach // 60
minutyKoncowe =  godzinaKoncowaWMinutach % 60, 2

print(f'{godzinaKoncowa}:{minutyKoncowe}')


#Zadanie

kilometry = float(input('Podaj kilometry: '))

KilometryNaMilimetry = kilometry * 1000000
KilometryNaCentymetry = kilometry * 100000
KilometryNaMetry = kilometry * 1000
KilometryNaCale = kilometry * 393700787
KilometryNaStopy = kilometry * 32808399
KilometryNaMile = kilometry * 0.621371192

print(f'{kilometry}km to {KilometryNaMilimetry}mm')
print(f'{kilometry}km to {KilometryNaMetry}m')
print(f'{kilometry}km to {KilometryNaCale}"')
print(f'{kilometry}km to {KilometryNaStopy}ft')
print(f'{kilometry}km to {KilometryNaMile} mil')



