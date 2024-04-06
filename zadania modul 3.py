# zadanie 3.1.1.4

n = int(input("Podaj liczbe: "))
print(n >= 100)

# zadanie 3.1.1.10

tekst = input('Podaj tekst: ')

if tekst == 'Skrzydłokwiat':
    print("Skrzydłokwiat jest najlepszą rośliną w historii!")
else:
    print('Nie, ja chcę Skrzydłokwiat...!')

#zadanie 3.1.1.11

dochod = float(input("Wprowadź swój roczny dochód: "))

if dochod < 85528:
    podatek = (dochod * 0.18) - 556.02
    if podatek < 0:
        podatek = 0.0

else:
    podatek = 14839.02 + (dochod - 85528) * 0.32



podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)

#zadanie 3.1.1.12

rok = int(input("Wprowadź rok: "))

if rok > 1582:

    if rok % 4 != 0:
        print('Rok zwykly')
    
    else:
        if rok % 100 != 0:
            print('Rok przestepny')
        elif rok % 400 != 0:
            print('Rok zywkly')
        else:
            print('Rok przestepny')
            
else:
    print('Nie w kalendarzy gregorianskim')

# zadanie 3.2.1.3

tajny_numer = 777

print(
'''
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
''')
flag = True
while flag:
    liczbaUzytkownika = int(input('Zgadnij liczbe maga: '))
    if liczbaUzytkownika != tajny_numer:
        print('Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!')
    else:
        print('Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.')
        flag = False


# zadanie 3.2.1.6

import time # LINIA I

for sec in range(1, 6):
    print(f'{sec} Mississippi')
    time.sleep(1) # LINIA II

print("Ready or not, here I come!")



# zadanie 3.2.1.9

slowo = 'pumpernikiel'

while True:
    slowoUzytkownika = input('Podaj swoje slowo: ')
    if slowoUzytkownika == slowo:
        print('Udalo ci sie opuscic petle.')
        break 

#zadanie 3.2.1.10

slowo = input('Podaj slowo: ')
slowo_uzytkownika = slowo.upper()

for litera in slowo_uzytkownika:
    samogloski = 'AEIOU'
    if litera in samogloski:
        continue
    print(litera)


# zadanie 3.2.1.11

slowo_bez_samoglosek = ""

slowo_uzytkownika = input('Podaj slowo: ')
slowo_uzytkownika = slowo_uzytkownika.upper()



for litera in slowo_uzytkownika:
    samogloski = 'AEIOU'
    if litera in samogloski:
        continue
    slowo_bez_samoglosek += litera

print(slowo_bez_samoglosek)



#zadanie 3.2.1.14

blokow = int(input("Wprowadź liczbę bloków: "))


wysokosc = 0
iloscKlockow = 0

while iloscKlockow + 1 <= blokow:
    iloscKlockow += 1
    blokow -= iloscKlockow
    wysokosc += 1
    
    
    
    
    

print("Wysokość piramidy wynosi:", wysokosc)


#zadanie 3.2.1.15
c0 = int(input('Podaj liczbe: '))
counter = 0
while c0 != 1:
    

    if c0 % 2 == 0:
        c0 = c0 / 2    
    elif c0 != 1:
        c0 = 3 * c0 + 1
    else:
        c0 = 3 * c0 + 1
    counter +=1
    print(int(c0))
print('liczba krokow =', counter)




















