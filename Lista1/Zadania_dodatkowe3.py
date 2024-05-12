# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie

def lista_samoglosek():

    spolgloska = input("Podaj spolgloske: ")

    samogloski = ['a', 'e', 'i', 'o', 'u']

    print("Zestaw sylab: ")
    for samogloska in samogloski:
        sylaba = spolgloska + samogloska
        print(sylaba)


def main():

    lista_samoglosek()

if __name__ == '__main__':
    main()