###### Zadanie 7
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while

import math
def kalkulator():

    liczba = 1

    while liczba <= 10:
        pierwiastek = math.sqrt(liczba)
        print("Pierwiastek z liczby",liczba, "jest równy: ", pierwiastek)
        liczba += 1

def main():

    kalkulator()

if __name__ == "__main__":
    main()
