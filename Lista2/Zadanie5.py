########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 - if
## np 50% to 3.0, 61% to 3.5, ...., 91% to 5.0 - match
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)

def procenty():

    x = int(input("Podaj liczbę procentów uzyskanych na kolowkium: "))

    if x >= 90 and x <= 100:
        print("ocena: 5")
    elif x >= 80 and x <= 89:
        print("ocena: 4,5")
    elif x >= 70 and x <=79:
        print("ocena: 4")
    elif x >= 60 and x <= 69:
        print("ocena: 3,5")
    elif x >= 50 and x <= 59:
        print("ocena: 3")
    elif x >= 40 and x <= 49:
        print("ocena: 2")
    elif x >= 30 and x <= 39:
        print("ocena: 1")

def main():

    procenty()

if __name__ == '__main__':
    main()