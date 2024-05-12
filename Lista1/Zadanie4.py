######################Zadanie 4
# Wyświetl nazwy kluczy poprzednio utworzonego słownika, oraz ilość jego elementów

def slownik():

    information = {'imie': ['Filip','Adam','Patryk'],
                   'nazwisko': ['Moczydlowski','Przeździecki', 'Warchol'],
                   'wiek': ['21','18','22'],
                   }
    osoba = int(input("Podaj numer osoby, której chcesz zobaczyć informacje: "))
    kierunek = input("Podaj kierunek studiów: ")
    information['kierunek studiow'] = kierunek

    if osoba >= 1 and osoba <= len(information['imie']):
        index = osoba-1
        print("Imię:",information['imie'][index])
        print("Nazwisko:",information['nazwisko'][index])
        print("Wiek:",information['wiek'][index])
        print("kierunek studiow:", information['kierunek studiow'])
    else:
        print("W słowniku nie ma takiej osoby")

    print("Nazwy kluczy:", list(information.keys()))
    print("Ilość elementów w słowniku:", len(information))

def main():

    slownik()

if __name__ == '__main__':
    main()