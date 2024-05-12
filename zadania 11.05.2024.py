# zadanie 5.11.1.4

def readint(prompt, min, max):
    if isinstance(prompt, str):
        print('Blad: wprowadzono nieprawidlowa liczbe')
    elif prompt < min or prompt > max:
        print(f'Blad: podana liczba jest spoza dozwolonego zakresu ({min}..{max})')
    else:
        global flag
        flag = False
        
        return prompt
flag = True
while flag:
    try:
        liczba = int(input("Podaj liczbe od -10 do 10: "))
    
        v = readint(liczba, -10, 10)
        
        
    
    except ValueError:
        print('Blad: wprowadzono nieprawidlowa liczbe')
    
print("Liczba to:", v)
"""
#zadanie 5.8.1.7
"""
print('Program, ktory sprawdza czy podane slowo/zdanie jest palindromem')
daneUzytkownika = input('Podaj zdanie/slowo, ktore chcesz sprawdzic: ')
if daneUzytkownika:
    daneUzytkownika = daneUzytkownika.replace(' ','')
    if daneUzytkownika.lower() == daneUzytkownika[-1::-1].lower():
            
        print(f'Slowo/zdanie jest palindromem')
    else:
        print(f'Slowo/zdanie nie jest palindromem')
else:
    print('Podales pusty ciag znakow')
"""
#zadanie 5.8.1.8
"""
slowo1 = input('Podaj pierwsze slowo: ')
slowo2 = input('Podaj drugie slowo: ')

anagram = True
for char in slowo1:
    if char not in slowo2.lower():
        anagram = False
        

for char in slowo2:
    if char not in slowo1.lower():
        anagram = False

if anagram:
    print('Anagram')
else:
    print('Nie anagram')
"""
#zadanie 5.8.1.10
"""
arg1 = input('Podaj pierwszy wyraz: ')
arg2 = input('Podaj drugi wyraz: ')

def slowoWSlowie(arg1, arg2):
    if arg1 in arg2:
        return 'Tak'
    else:
        return 'Nie'

print(slowoWSlowie(arg1, arg2))

#zadanie 5.7.1.6

line1 = "  # ### ### # # ### ### ### ### ### ### "
line2 = "  #   #   # # # #   #     # # # # # # # "
line3 = "  # ### ### ### ### ###   # ### ### # # "
line4 = "  # #     #   #   # # #   # # #   # # # "
line5 = "  # ### ###   # ### ###   # ### ### ### "

szablon = [line1, line2, line3, line4, line5]

def wyswietl_liczbe(liczba):
    liczba = str(liczba)
    
    for char in szablon:
        liczba1 = char[0:4]
        liczba2 = char[4:8]
        liczba3 = char[8:12]
        liczba4 = char[12:16]
        liczba5 = char[16:20]
        liczba6 = char[20:24]
        liczba7 = char[24:28]
        liczba8 = char[28:32]
        liczba9 = char[32:36]
        liczba0 = char[36:40]
        wynik = []
        for el in liczba:
            if el == '1':
                wynik.append(liczba1)
            
            if el == '2':
                wynik.append(liczba2)
    
            if el == '3':
                wynik.append(liczba3)
           
            if el == '4':
                wynik.append(liczba4)

            if el == '5':
                wynik.append(liczba5)

            if el == '6':
                wynik.append(liczba6)

            if el == '7':
                wynik.append(liczba7)

            if el == '8':
                wynik.append(liczba8)
            if el == '9':
                wynik.append(liczba9)
            if el == '0':
                wynik.append(liczba0)
                
            
        print(''.join(wynik))
        
print(wyswietl_liczbe(1239483) 
