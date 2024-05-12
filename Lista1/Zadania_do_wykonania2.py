## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

def oblicz():

    x = int(input("Podaj x:"))
    y = int(input("Podaj y:"))

    wzor = 2*x + 5*y

    print("Wynik: ",wzor)
def main():

    oblicz()

if __name__ == '__main__':
    main()
