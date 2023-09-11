# Initialisatie van variabelen voor het grootste, kleinste en aantal deelbare getallen
grootste = float("-inf")
kleinste = float("inf")
aantal_deelbaar_door_3 = 0

# Vraag de gebruiker om 10 getallen in te voeren
for i in range(10):
    getal = int(input(f"Voer getal {i + 1} in: "))

    # Update het grootste en kleinste getal
    if getal > grootste:
        grootste = getal
    if getal < kleinste:
        kleinste = getal

    # Controleer of het getal deelbaar is door 3
    if getal % 3 == 0:
        aantal_deelbaar_door_3 += 1

# Druk de resultaten af
print(f"Het grootste getal is: {grootste}")
print(f"Het kleinste getal is: {kleinste}")
print(f"Het aantal getallen deelbaar door 3 (zonder rest) is: {aantal_deelbaar_door_3}")
