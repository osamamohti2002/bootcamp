cijfer = [1,2,3,4,5,6,7,8,9,10]

# Definieer een functie om de omschrijving te bepalen
def bepaal_omschrijving(cijfer):
    if cijfer == 10:
        return "uitmuntend"
    elif cijfer == 9:
        return "zeer goed"
    elif cijfer == 8:
        return "goed"
    elif cijfer == 7:
        return "ruim voldoende"
    elif cijfer == 6:
        return "voldoende"
    elif cijfer == 5:
        return "bijna voldoende"
    elif cijfer == 4:
        return "onvoldoende"
    elif cijfer == 3:
        return "gering"
    elif cijfer == 2:
        return "slecht"
    elif cijfer == 1:
        return "zeer slecht"
    else:
        return "Ongeldig cijfer"

# Roep de functie aan om de omschrijving te verkrijgen en af te drukken
omschrijving = bepaal_omschrijving(cijfer)
print(f"Omschrijving: {omschrijving}")