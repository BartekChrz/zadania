#zadanie 4.1.36

def czy_przestepny(rok):
    if rok % 4 == 0 and rok % 100 != 0:
        return True
    elif rok % 400 == 0:
        return True
    else:
        return False
    
dane_testowe = [1900, 2000, 2016, 1987]
wyniki_testow = [False, True, True, False]
for i in range(len(dane_testowe)):
	r = dane_testowe[i]
	print(r,"->",end="")
	wynik = czy_przestepny(r)
	if wynik == wyniki_testow[i]:
		print("OK")
	else:
		print("Nie powiodło się")

#zadanie 4.3.1.7
def czy_przestepny(rok):
    if rok % 4 == 0 and rok % 100 != 0:
        return True
    elif rok % 400 == 0:
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    if type(rok) == int and type(miesiac) == int:
        days31 = [1, 3, 5, 7, 8, 10, 12]
        days30 = [4, 6, 9, 11]
        if miesiac in days31:
            return 31
        elif miesiac in days30:
            return 30
        elif miesiac == 2:
            if czy_przestepny(rok) == True:
                return 29
            else:
                return 28
    else:
        return None
        
testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")

#zadanie 4.3.1.8

def czy_przestepny(rok):
    if rok % 4 == 0 and rok % 100 != 0:
        return True
    elif rok % 400 == 0:
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    if type(rok) == int and type(miesiac) == int:
        days31 = [1, 3, 5, 7, 8, 10, 12]
        days30 = [4, 6, 9, 11]
        if miesiac in days31:
            return 31
        elif miesiac in days30:
            return 30
        elif miesiac == 2:
            if czy_przestepny(rok) == True:
                return 29
            else:
                return 28
    else:
        return None

def dzien_w_roku(rok, miesiac, dzien):
    if type(rok) == int and type(miesiac) == int and type(dzien) == int:
        dni = ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek', 'Sobota', 'Niedziela']
        sumaDni = 0
        dniOd0 = 1
        for i in range(rok):
            if czy_przestepny(rok):
                dniOd0 += 365
            else:
                dniOd0 += 366
        for msc in range(12):
            dniOd0 += dni_w_miesiacu(rok, miesiac)

        dniOd0 += dzien
        dzienTygodnia = dniOd0 % 7
        return dni[dzienTygodnia]
    return None
    
    
        

#zadanie 4.3.1.9


def czy_pierwsza(liczba):
    if all(liczba % i != 0 for i in range(2, int(liczba**0.5) + 1)):
        return True
    
for i in range(1, 20):
	if czy_pierwsza(i + 1):
			print(i + 1, end=" ")
print()

#zadanie 4.3.1.10

def l100kmtompg(litry):
    galon = 3.785411784
    mila = 1609.344 
    dystansWMilach = 100000 / mila
    galonyPrzejechane = litry / galon
    mpg = dystansWMilach / galonyPrzejechane
    return mpg
    

def mpgtol100km(mile):
    mila = 1609.344
    galon = 3.785411784
    dystansWM = mile * mila
    gp100km = 100000 / dystansWM  
    l100km = gp100km * galon
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))


#Obliczanie bmi

def oblicz_bmi(wzrost, waga):
    if isinstance(wzrost, int) == True or isinstance(wzrost, float) == True and isinstance(waga, int) == True or isinstance(waga,float) == True:
        if wzrost < 0 or waga < 0:
            print('Wzrost lub waga nie moga byc mniejsze od 0')
        elif wzrost == 0:
            print('Nie dziel przez zero!')
        else:
            bmi = waga/wzrost**2
            print(f'Twoje BMI to {bmi}.')
    else:
        print('Podane wartosci musza byc liczbami calkowitymi lub zmiennoprzecinkowymi.')

#Trojkat pit
        
def oblicz_trojkat_pit(a, b, c):
    try:
        twPit = a ** 2 + b ** 2 == c **2
    except TypeError as err:
        print(err)
    else:
        if twPit:
            print(f'Trojkat o bokach a {a}, b {b} i c {c} tworza trojkat pitagorasa')
        else:
            print(f'Trojkat o bokach a {a}, b {b} i c {c} nie tworza trojkata pitagorasa')


#Silnia ver z petla

def oblicz_silnie(n):
    if n == 1:
        return 1
    suma = 1
    for i in range(1, n +1):
        suma *= i
    return suma

#Silnia ver z rekurencja

def oblicz_silnieV2(n):
    if n == 1:
        return 1
    return n * oblicz_silnieV2(n - 1)



