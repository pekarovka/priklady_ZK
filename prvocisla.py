"""Zadané kladné celé číslo rozloží na součin prvočísel."""


#funkce pro rozklad na prvočísla
def RozkladNaPrvocisla(n):
    print("{} - rozklad na prvočísla:\t".format(n), end=" ")
    i = 2
    while n > 1:
        if n % i == 0:          # % je zbytek po dělení
            print(i, end=" ")
            n = n // i          # // je celočíselný podíl
        else:
            i = i + 1
    print()                     # vynechá řádek po vypsaných prvočíslech


#zadání kladného čísla
k = int(input("Zadejte kladné celé číslo, jež rozložíme na prvočísla: "))

#kontrola splnění zadaných podmínek pro rozklad
if k <= 0:
    print("Nezadal(a) jste kladné celé číslo!")
    exit(1)

if k == 1:
    print("1 nelze rozložit na prvočísla!")
    exit(1)

#zavolání funkce na zadané číslo
RozkladNaPrvocisla(k)

