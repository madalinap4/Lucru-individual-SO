def primul_potrivit(procese, blocuri_libere):
    for proces in procese:
        for i in range(len(blocuri_libere)):
            if blocuri_libere[i] >= proces:
                blocuri_libere[i] -= proces
                break
    return blocuri_libere

def urmatorul_potrivit(procese, blocuri_libere):
    ultima_pozitie = 0
    for proces in procese:
        numar_blocuri = len(blocuri_libere)
        for i in range(numar_blocuri):
            index = (ultima_pozitie + i) % numar_blocuri
            if blocuri_libere[index] >= proces:
                blocuri_libere[index] -= proces
                ultima_pozitie = index + 1
                break
    return blocuri_libere

def cel_mai_potrivit(procese, blocuri_libere):
    for proces in procese:
        cel_mai_bun_index = -1
        for i in range(len(blocuri_libere)):
            if blocuri_libere[i] >= proces:
                if cel_mai_bun_index == -1 or blocuri_libere[i] < blocuri_libere[cel_mai_bun_index]:
                    cel_mai_bun_index = i
        if cel_mai_bun_index != -1:
            blocuri_libere[cel_mai_bun_index] -= proces
    return blocuri_libere

def cel_mai_nepotrivit(procese, blocuri_libere):
    for proces in procese:
        cel_mai_rau_index = -1
        for i in range(len(blocuri_libere)):
            if blocuri_libere[i] >= proces:
                if cel_mai_rau_index == -1 or blocuri_libere[i] > blocuri_libere[cel_mai_rau_index]:
                    cel_mai_rau_index = i
        if cel_mai_rau_index != -1:
            blocuri_libere[cel_mai_rau_index] -= proces
    return blocuri_libere

if __name__ == "__main__":
    procese = list(map(int, input("Introduceti procesele (separate prin virgula): ").split(',')))
    blocuri_libere_initiale = list(map(int, input("Introduceti blocurile de memorie libere (separate prin virgula): ").split(',')))

    print("\nPrimul Potrivit:")
    blocuri_libere = blocuri_libere_initiale.copy()
    rezultat = primul_potrivit(procese, blocuri_libere)
    print("Blocuri libere finale:", rezultat)

    print("\nUrmatorul Potrivit:")
    blocuri_libere = blocuri_libere_initiale.copy()
    rezultat = urmatorul_potrivit(procese, blocuri_libere)
    print("Blocuri libere finale:", rezultat)

    print("\nCel Mai Potrivit:")
    blocuri_libere = blocuri_libere_initiale.copy()
    rezultat = cel_mai_potrivit(procese, blocuri_libere)
    print("Blocuri libere finale:", rezultat)

    print("\nCel Mai Nepotrivit:")
    blocuri_libere = blocuri_libere_initiale.copy()
    rezultat = cel_mai_nepotrivit(procese, blocuri_libere)
    print("Blocuri libere finale:", rezultat)
