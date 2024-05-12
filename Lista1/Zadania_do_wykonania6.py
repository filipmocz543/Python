## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.

def kalkulator():

    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))

    suma = x+y
    roznica = x-y
    iloczyn = x*y
    iloraz = x/y
    potega = x^y

    print("Suma jest równa: ",suma)
    print("Roznica jest równa: ",roznica)
    print("Iloczyn jest równy: ",iloczyn)
    print("Iloraz jest równy: ",iloraz)
    print("Potega jest równa: ",potega)


def main():

    kalkulator()

if __name__ == '__main__':
    main()