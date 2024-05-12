#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) ile zdań jest w analizowanym tekście?

def zadania():

    tekst = ['Emma rzeczywiście była szybka – dane wysłała w 12 minut. ',
            'Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. ',
            'Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu ',
            '(choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki)'
            ]

    #Ile razy występuje Emma
    licznik_Emma = 0

    for fragment in tekst:
        if 'Emma' in fragment:
            licznik_Emma += 1
            print("Słowo Emma występuje w tekscie: ",licznik_Emma)

    #Zmień całość tekstu na duże litery:
    for fragment in tekst:
        print(fragment.upper())

    #Wstawienie poszczególnych wyrazów jako elementy listy
    nowy_tekst =[]
    element = input("Podaj nowy tekst: ")
    nowy_tekst.append(element)
    koncowy_tekst = tekst + nowy_tekst
    print(koncowy_tekst)

    #Ile zdań jest w analizowanym tekście?

    liczba_kropek = 0

    for fragment in tekst:
        if '.' in fragment:
            liczba_kropek += 1

    print("W tekscie występuje:",liczba_kropek, "zdan")


def main():

    zadania()

if __name__ == '__main__':
    main()