#zadanie nr 1

import math

class Shape:
    def __init__(self):
        print(f'Utworzono figure o klasie {type(self).__name__}.')

    def oblicz_pole(self):
        pass
    def oblicz_obwod(self):
        pass

class Circle(Shape):
    def __init__(self, promien):
        Shape.__init__(self)
        self.promien = promien

    def oblicz_pole(self):
        self.pole = math.pi * self.promien ** 2
        return round(self.pole, 4)
    
    def oblicz_obwod(self):
        self.obwod = 2 * math.pi * self.promien
        return self.obwod

class Rectangle:

    def __init__(self, a, b):
        Shape.__init__(self)
        self.a = a
        self.b = b

    def oblicz_pole(self):
        self.pole = self.a * self.b
        return self.pole
    def oblicz_obwod(self):
        self.obwod = 2 * self.a + 2 * self.b
        return self.obwod

class Triangle:

    def __init__(self, a, b, c, h):
        Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def oblicz_pole(self):
        self.pole = self.a * self.h / 2
        return self.pole

    def oblicz_obwod(self):
        self.obwod = self.a + self.b + self.c
        return self.obwod

#zadanie nr 2

class Task:

    def __init__(self, numer_zadania, opis, priorytet, termin_wykonania):
        self.numer_zadania = numer_zadania
        self.opis = opis
        self.priorytet = priorytet
        self.termin_wykonania = termin_wykonania

class TM:

    def __init__(self):
        self.listaZadan = []

    def dodaj_zadanie(self, numer_zadania, opis, priorytet, termin_wykonania):
        zadanie = Task(numer_zadania, opis, priorytet, termin_wykonania)
        self.listaZadan.append(zadanie)
        print('Dodano pomyslnie zadanie numer', numer_zadania)

    def wyswietl_zadania(self):
        for task in range(len(self.listaZadan)):
            print('Zadanie numer: ', self.listaZadan[task].numer_zadania)
            print('Opis:', self.listaZadan[task].opis)
            print('Priorytet:', self.listaZadan[task].priorytet)
            print('Termin wykonania:', self.listaZadan[task].termin_wykonania)
            print()

    def usun_zadanie(self, numerZadania):
        del taskManager.listaZadan[numerZadania - 1]
        print('Usunieto pomyslnie')
        
        

taskManager = TM()

taskManager.dodaj_zadanie(1, 'opis1', 'priorytet1', 'termin1')
taskManager.dodaj_zadanie(2, 'opis2', 'priorytet2', 'termin2')
taskManager.dodaj_zadanie(3, 'opis3', 'priorytet3', 'termin3')

taskManager.wyswietl_zadania()

taskManager.usun_zadanie(1)
taskManager.wyswietl_zadania()

