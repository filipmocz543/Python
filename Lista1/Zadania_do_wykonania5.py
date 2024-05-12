## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą
# wyświetl właściwy komunikat
##   użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0

def sprawdz():

    x = int(input("Podaj liczbe x: "))
    y = int(input("Podaj liczbe y: "))

    suma = x + y

    print("Suma jest równa: ",suma)

    if suma%2==0:
        print("Suma jest parzysta")
    else:
        print("Suma jest nieparzysta")


def main():

    sprawdz()

if __name__ == '__main__':
    main()