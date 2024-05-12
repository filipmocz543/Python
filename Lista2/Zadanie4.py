########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta

def dowolna():

    x = int(input("Podaj liczbe: "))

    if x%2 ==0:
        print("Parzysta")
    else:
        print("Nie parzysta")

def main():

    dowolna()

if __name__ == '__main__':
    main()