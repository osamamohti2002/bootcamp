# Visual Studio Code is handiger omdat je makkelijker bugs kunt vinden dan in een normale notepad
# het het altijd handig om je code in github te puchen zo heb je een back-up van je code en je kan het ook met de andere delen

#Opdracht 2:
# Maak het commentaar af.
# a = 5  # dit is een voorbeeld van het datatype: int
# b = 10.5# dit is een voorbeeld van het datatype: float
# c = "Hallo wereld" # dit is een voorbeeld van het datatype: string

#Opdracht 3
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
# a = 5
# b = 10
#
# omwisselen = a
# a = b
# b = omwisselen
# # voeg jouw code toe…
# # Controleer met onderstaande code of de waarden correct zijn verwisseld
# print(f"a = {a}, b = {b}")  # Moet "a = 10 b = 5" printen
#
#
# #Opdracht 4:
#
# # Los de problemen op (zonder exception handling).
# leeftijd = int(input("Hoe oud ben je?"))
# print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")
# # Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!
#
#
# #opdracht 5
# # Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# # dat de uitkomst ervan wordt getoond in de print
# def som(a, b, c):
#     return a + b + c
#
#
# getal1 = 200
# getal2 = 5
# getal3 = 12
# antwoord = som(getal1, getal2, getal3)
#
# print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")
#
# #Opdracht 6:
# # Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
# AANTAL_GB = 20 # Aantal GB data in je bundel
# AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
#
# ONBEPERKT = False # test ook met True
#
# aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
# aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
#
#
# if not ONBEPERKT and aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB :
#     print("Let op: je moet bijbetalen!")
#
#     # print("Let op: je moet bijbetalen!")
#
# else:
#     print("Niet aan de hand gebruik je mobiel lekker verder!")
#
#
# #Opdracht 7:
# # Print onder elkaar de getallen 1-250 met max 2 regels code.
#
# for teller in range(251):
#     print(teller)



#opdracht 8

# lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']
# print('onze menukaart')
# for item in lijst_eten:
#     print(item)
#
# langste_naam = max(lijst_eten, key=len)
# print(f"\nHet eten met de langste naam op het menu is: {langste_naam}")

#opdracht 9
# while True:
#     try:
#         getal = int(input('voer getal in tussen 0 en 10'))
#
#         if 0<= getal <= 10:
#             print('je hebt het goede cijfer ', getal)
#             break
#         else:
#             print('fout voer opnieuw cijfer in tussen 0 en 10 ')
#
#     except ValueError:
#         print('Fout voer een geldige waarde in')


#opdracht 10

MAX = 20
getal = int(input("Voer een getal in"))

if getal > MAX:
    print(f"Het getal is groter dan {MAX}")
elif getal < MAX:
    print(f"Het getal is kleiner dan {MAX}")
else:
    print(f"Het getal is gelijk aan {MAX}")