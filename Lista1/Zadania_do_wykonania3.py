## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)

def zdanie():

    print("Jestem a b mam c lat studiuję d")

    a = input("Podaj imię: ")
    b = input("Podaj nazwisko: ")
    c = input("Podaj wiek: ")
    d = input("Podaj co studiujesz: ")

    print("Jestem", a , b , "mam", c , "lat", "studiuję", d)

def main():

    zdanie()

if __name__ == '__main__':
    main()
