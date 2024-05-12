# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy

def names():

    list_name = ['Adam', 'Anna', 'Marcin', 'Katarzyna', 'Michał', 'Magdalena', 'Piotr', 'Joanna', 'Tomasz', 'Monika',
             'Mateusz', 'Natalia', 'Krzysztof', 'Agnieszka', 'Jakub', 'Kinga', 'Bartosz', 'Weronika', 'Łukasz', 'Karolina',
             'Paweł', 'Aleksandra', 'Robert', 'Beata', 'Grzegorz', 'Patrycja', 'Wojciech', 'Ewa', 'Żaneta', 'Daniel',
             'Adam', 'Anna', 'Marcin', 'Katarzyna', 'Michał']

    name_person = input("Podaj imię osoby, której chcesz znaleść indeks: ")

    if name_person in list_name:
        print(name_person, "znajduję się na pozycji:", list_name.index(name_person))
        print(name_person, "powtarza się", list_name.count(name_person),"razy w liście")
    else:
        print("W naszej liscie nie mamy takiego imienia")

    #pierwszy sposób
    new_person = 'Filip'
    list_name.append(new_person)
    print(list_name)

    #drugi sposób
    #list_name.append('Filip')
    #print(list_name)

    #pierwszy sposób
    secon_person = "Patrycja"
    list_name.insert(3, secon_person)
    print(list_name)

    #drugi sposób
    #list_name.insert(3,'Patrycja')
    #print(list_name)

    #sortowanie listy
    list_name.sort()
    print(list_name)

    #odwrócenie porząku listy, usunienie ostatniego(pierwszego) elementu w liscie i odwrócenie z powrotem
    list_name.reverse()
    list_name.pop(0)
    list_name.reverse()
    print(list_name)

    #rozszerzenie listy
    secon_list_name = ['Kacper', 'Remigiusz', 'Eugennia']
    merge_list = secon_list_name + list_name
    print(merge_list)

def main():

    names()

if __name__ == '__main__':
    main()