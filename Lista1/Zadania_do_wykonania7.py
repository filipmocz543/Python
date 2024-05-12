## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)

def dowolny():

    x = int(input("Podaj x: "))

    if x > 1 and x < 13 and x != 5 or x < 0:
        print("Jest")
    else:
        print("Nie jest")

def main():

    dowolny()

if __name__ == "__main__":
    main()