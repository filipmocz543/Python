######################Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika


def slownik():

    information = {'imie': ['Filip','Adam','Patryk'],
                   'nazwisko': ['Moczydlowski','Przeździecki', 'Warchol'],
                   'wiek': ['21','18','22']
                   }

    osoba = int(input("Podaj numer osoby, której chcesz zobaczyć informacje: "))

    if osoba >= 1 and osoba <= len(information['imie']):
        index = osoba-1
        print("Imię:",information['imie'][index])
        print("Nazwisko:",information['nazwisko'][index])
        print("Wiek:",information['wiek'][index])
    else:
        print("W słowniku nie ma takiej osoby")
def main():

    slownik()

if __name__ == '__main__':
    main()