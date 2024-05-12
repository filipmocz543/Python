# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna

def sprawdz():

    imie = input("Podaj imię: ")

    if imie == 'Janusz' or imie == 'Grażyna':
        print("To poprawne imie !")
    else:
        print("To nie jest poprawne imię")


def main():

    sprawdz()

if __name__ == '__main__':
    main()