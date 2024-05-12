# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
### Write a program that calculates the sum of the sequence: 1+1/2+1/3+...+1/m using the for loop.
### The input variable m is arbitrary. The m-parameter is provided as input by the user (use input).


def skrypt():

    a_1 = int(input("Podaj pierwsza liczbe ciagu: "))
    a_n = int(input("Podaj ostatnia liczbe ciągu: "))
    n = int(input("Podaj liczbę dlugości ciągu: "))

    S = ((a_1 + a_n) / 2) * n

    print("Suma ciągu wynosi: ",S)


def main():

    skrypt()


if __name__ == '__main__':
    main()