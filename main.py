def kalkulator():
    print("Üdvözöllek a kalkulátorban!")
    print("Választhatsz a következő műveletek közül:")
    print("1. Összeadás (+)")
    print("2. Kivonás (-)")
    print("3. Szorzás (*)")
    print("4. Osztás (/)")

    while True:
        # Felhasználó által választott művelet
        muvelet = input("\nAdd meg a művelet számát (1/2/3/4) vagy 'q' a kilépéshez: ")

        if muvelet.lower() == 'q':
            print("Köszönöm, hogy használtad a kalkulátort! Viszlát!")
            break

        if muvelet not in ['1', '2', '3', '4']:
            print("Érvénytelen választás. Próbáld újra.")
            continue

        try:
            # Számok bekérése
            szam1 = float(input("Add meg az első számot: "))
            szam2 = float(input("Add meg a második számot: "))

            # Művelet végrehajtása
            if muvelet == '1':
                eredmeny = szam1 + szam2
                print(f"Eredmény: {szam1} + {szam2} = {eredmeny}")
            elif muvelet == '2':
                eredmeny = szam1 - szam2
                print(f"Eredmény: {szam1} - {szam2} = {eredmeny}")
            elif muvelet == '3':
                eredmeny = szam1 * szam2
                print(f"Eredmény: {szam1} * {szam2} = {eredmeny}")
            elif muvelet == '4':
                if szam2 == 0:
                    print("Hiba: Nullával nem lehet osztani.")
                else:
                    eredmeny = szam1 / szam2
                    print(f"Eredmény: {szam1} / {szam2} = {eredmeny}")
        except ValueError:
            print("Hiba: Kérlek számot adj meg!")


if __name__ == '__main__':
    kalkulator()