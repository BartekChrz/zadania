
#zadanie 6.9.1.15

fileName = input('Podaj nazwe pliku, ktory chcesz otworzyc:\n>>>')
import collections

try:
    plik = open(fileName, 'r')
except FileNotFoundError:
    print('Nie znaleziono takiego pliku')

else:
    
    chars = [char.lower() for char in plik.read() if char.isalnum()]
    sortedChars = collections.Counter(chars)

    for key, value in sortedChars.items():
        print(f'{key} -> {value}')
        

#zadanie 6.9.1.16

fileName = input('Podaj nazwe pliku, ktory chcesz otworzyc:\n>>>')
import collections

try:
    plik = open(fileName, 'r')
except FileNotFoundError:
    print('Nie znaleziono takiego pliku')

else:
    
    chars = [char.lower() for char in plik.read() if char.isalnum()]
    sortedChars = collections.Counter(chars)

    result = [f'{key} -> {value}' for key, value in sorted(sortedChars.items(), key=lambda x: x[1], reverse=True)]
     
    file = (',').join(result).replace(',','\n')

    zapis = open('his.' + fileName, 'w')
    zapis.write(file)
    zapis.close()



#zadanie 6.9.1.17

class WyjatekZleDaneStudenta(Exception):
        pass

        
        
class ZlaLinia(WyjatekZleDaneStudenta):
    def __init__(self, uczen):
        WyjatekZleDaneStudenta.__init__(self)
        self.uczen = uczen


class PustyPlik (WyjatekZleDaneStudenta):
    def __init__(self, odczyt):
        WyjatekZleDaneStudenta.__init__(self)
        self.odczyt = odczyt
        
nazwaPliku = input('Podaj nazwe pliku prof. Miodka, ktora chcesz otworzyc:\n>>>')


def otworz_plik(nazwaPliku):
    odczyt = open(nazwaPliku, 'r')           
      
    if not len(odczyt.read()) > 0:
        raise PustyPlik('Plik jest pusty')
    else:
        odczyt = open(nazwaPliku, 'r')
        dane = odczyt.read().split('\n')
    
    uczniowie = [x.split(' ') for x in dane]
    
    daneUczniow = dict()
    
    for uczen in uczniowie:
        if len(uczen) != 3:
            raise ZlaLinia('Ktoras z linii w pliku zawiera niepoprawna ilosc danych')
        
        if uczen[0] + ' ' + uczen[1] not in daneUczniow:
            daneUczniow[uczen[0] + ' ' + uczen[1]] = float(uczen[2])
        else:
            daneUczniow[uczen[0] + ' ' + uczen[1]] = float(daneUczniow[uczen[0] + ' ' + uczen[1]]) + float(uczen[2])
    
    print(f'Dane uczniow z pliku {nazwaPliku}:')
    print('\n')
    for uczen, wynik in sorted(daneUczniow.items(), key=lambda x: x[0]):
        print(uczen, wynik)

    
    odczyt.close()
try:
    otworz_plik(nazwaPliku)
except PustyPlik as er1:
    print(er1.odczyt)
except ZlaLinia as er2:
    print(er2.uczen)
except WyjatekZleDaneStudenta as er3:
    print(er3.message)
except FileNotFoundError:
    print('Nie znalezioni takiego pliku')
except:
    print('Cos poszlo nie tak')


    
