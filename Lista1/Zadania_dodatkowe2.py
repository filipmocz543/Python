# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.

def zyciorys():

    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    wiek = int(input("Podaj wiek: "))
    zawod = input("Podaj zawod: ")
    miejsce_urodzenia = input("Podaj miejsce urodzenia: ")
    zainteresowania = input("Podaj zainteresowania: ")

    zdanie = f"{imie} {nazwisko} ma {wiek} lat. Jest {zawod} z {miejsce_urodzenia}. Interesuje się {zainteresowania}."

    print(zdanie)


def main():

    zyciorys()

if __name__ == '__main__':
    main()