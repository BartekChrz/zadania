# zadanie 3.4.1.6

liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.

liczbaSrodkowa = int(input('Podaj liczbe, ktora zastapisz srodkowy element: '))
liczby_z_kapelusza[2] = liczbaSrodkowa

liczby_z_kapelusza.pop(-1)

print(len(liczby_z_kapelusza))

print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.


#zadanie 3.4.1.13


beatles = list()
print("Krok 1:", beatles)

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Krok 2:", beatles)

iloscCzlonkowDoDodania = int(input('Podaj liczbe czlonkow, ktorych chcesz dodac do zespolu: '))
for nowyCzlonek in range(iloscCzlonkowDoDodania):
    osoba = input('Podaj imie i nazwisko czlonka, ktorego chcesz dodac: ')
    beatles.append(osoba)
print("Krok 3:", beatles)

del beatles[-2:]
print("Krok 4:", beatles)

beatles.insert(0, 'Ringo Starr')
print("Krok 5:", beatles)


# Sprawdzanie długości listy.
print("The Fab", len(beatles))


#zadanie 3.6.1.9

moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#metoda 1
#moja_lista = list(set(moja_lista))

#metoda 2

tempList = []
for element in moja_lista:
    if element not in tempList:
        tempList.append(element)
moja_lista = tempList

print("Lista tylko z unikalnymi elementami:")
print(moja_lista)
