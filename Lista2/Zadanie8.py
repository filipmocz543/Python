###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0

def kalkulator():

    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
    c = float(input("Podaj liczbę c: "))

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Pierwiastki równania to:", x1, "i", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Równanie ma jeden pierwiastek:", x)
    else:
        print("Równanie nie ma pierwiastków rzeczywistych.")

def main():

    kalkulator()

if __name__ == '__main__':
    main()