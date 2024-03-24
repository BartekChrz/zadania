"""
Kompilator czyta kod i potem go przeksztalca i wykonuje program
Interpreter czyta kod i od razy go wykonuje
"""

#INTRUKCJA PRINT

print('Witaj świecie')
print('Python')
# Print instrukcja, która przyjmuje jakiś napis i go wyswietla w interpreterze,
# instrukcja wypisywania informacji na ekran. Jest to funkcja wbudowana

#SEPARATOR  sep='' - domyslny to spacja ' ' 

print('napis1', 'napis2', 'napis3', sep='/')
print('linijka1', 'linijka2', sep='\n') # '\n' - znak przejscia do kolejnej lini

#PARAMENTR end='' - domyslnie end='\n'

print('napis1', 'napis2', 'napis3', end = '!')
print('jakis napis', end ='.')
print('jeszcze cos')


#TYPY DANYCH

#string - "tekst", "10"
#integer - 10 - liczba calkowita
#float - 10.0 - liczba zmienniprzecinkowa
#boolean - True False

print(10)
print(10.5)

print(0o123) # liczba osemkowa 83
print(0x1234) # liczna szesnasctkowa

print(3E8) # 3 * 10**8 - notacja naukowa

print("") # pusty string

print("'apostrofy'") #python traktuje apostrofy w apostrofach jako znak
print('"apostrofy"')

# '\'- ZNAK UCIECZKI
print("apostrfory \"3\"")
print('You\'re here')
print()

# "Uczę się"
# ""języka""
# """python"""

print('"Uczę się"', '""języka""', '"""python"""', sep = '\n')

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5) # dzielenie zawsze zwraca liczbie o typie danych float
print(2 ** 5)
print(11 // 5) #dzielenie calkowite
print(10 % 2) #modulo - zwraca reszte z dzielenia

# ^ to sa operatory dwuargumentowe
# '-' lub '+' to argumenty jednoargumentowe
print(-5)
print(+5)

#KOLEJNOSC DZIALAN JAK W MATEMATYCE
print(10 + 2 * 5)
print((10 + 2) * 5)
print(2 ** 3 ** 4) # potegowanie to wyjatek i wykonuje sie od prawej do lewej a nie od lewej do prawej

#boolean
print(True)
print(False)
print(10 > 2)
print(10 < 2)
print(True > False) # True = 1, a False = 0 
print(False > True)

#ZMIENNE
#zmienna sklada sie z nazwy, operatora przypisania '=' i dancyh przypisanych do zmiennej

wynik = 5 ** 5 ** 2
print(wynik)
#nazwa zmiennej musi zaczynac sie od litery np. a10 a nie 10a
#zmienna musi byc caloscia - zmienna druga X, zmienna_druga OK
zmienna_druga = 5
print(zmienna_druga) #pamietac o duzych literach, nie ma ZMIENNA_DRUGA albo Zmienna_druga
# zmienna nie moze byc slowem zastrzezonym np def = 11
# zmienna najpierw musi byc zdefiniowana bo inaczej bd error

zmiennaString = "tekst"
zmiennaInt = 5
zmiennaFloat = 1.2
zmiennaBoolean = False

print(zmiennaString, zmiennaInt, zmiennaFloat, zmiennaBoolean)

#zmienne mozna nadpisywac
zmiennaString = ' Inny napis'
print(zmiennaString)
zmiennaString = 2.0 # mozna zmienic wartosc zmiennej na inny typ
print(zmiennaString)

print(zmiennaInt * zmiennaFloat)

imie = 'Jan'

print('Twoje imie to', imie)

# str(x) zmienia typ danych na string
wiek = 30
print('Twoj wiek to ' + str(wiek))
# int(x) zmienia typ danych na int
wiek = '30'
print(int(wiek) + 2)
#float(x) zmienia typ danych na float

# F-STRING

liczba = 20

print(f'Liczba jest rowna {liczba}!')

#SKROTY DLA OPERATOROW

wynik = 11 +3
print(wynik)

wynik = wynik + 5 #skrocic mozna do wynik += 5
print(wynik)

wynik -= 1
print(wynik)
#wynik *= 2 = 36, wynik /= 3 = 12.0 itp itd


# Program konwertujaty temperature

celsjusz = int(input()) #input ma domyslny typ jako string wiec trzeba przkonwertowac
kelwin = celsjusz + 273.15
fahrenheit = (celsjusz * 9/5) + 32 

print(f'Temperatura w celsjuszach to {celsjusz}')
print(f'Temperatura w kelwinach to {kelwin}')
print(f'Temperature w fahrenheitach to {fahrenheit}')

imie = input('Podaj swoje imie ') 

print('napis1' + 'napis2')
print('napis' * 10)

imie = input('Wprowadz imie: ')
nazwisko = input('Wprowadz nazwisko: ')
wiek = int(input('Wprowdz wiek: '))

rok = 2024 - wiek

print(f'Twoje imie to {imie}, a nazwisko to {nazwisko}. Urodziles sie w {rok}')

