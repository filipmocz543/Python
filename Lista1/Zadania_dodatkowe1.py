# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania:
# "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.

def ankieta():

    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    wiek = int(input("Podaj wiek: "))
    jedzenie = input("Czy zdrowo się odżywiasz?: ")
    sport = input("Czy lubisz sport?: ")
    miejsce_urodzenia = input("Podaj miejsce urodzenia: ")
    hobby = input("Podaj hobby: ")
    rodzenstwo = input("Czy masz rodzeństwo: ")

    print("\nPodsumowanie ankiety:")
    print("Imię:", imie)
    print("Nazwisko:", nazwisko)
    print("Wiek:", wiek)
    print("Czy zdrowo się odżywiasz?:", jedzenie)
    print("Czy lubisz sport?:", sport)
    print("Podaj miejsce urodzenia: ", miejsce_urodzenia)
    print("Podaj hobby: ", hobby)
    print("Czy masz rodzeństwo: ", rodzenstwo)

def main():

    ankieta()

if __name__ == '__main__':
    main()