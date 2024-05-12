# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście

def geny():

    lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

    lista_gene2 = ['FGFR4', 'FGERA4']

    for gene in lista_gene2:
        if gene in lista_gene1:
            index = lista_gene1.index(gene)
            print("Wsytępuje", ", numer idenksu: ", index)
        else:
            print("Nie występuje")


def main():

    geny()

if __name__ == '__main__':
    main()