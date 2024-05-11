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

#zadanie 5.7.1.6 przesle w tygodniu
