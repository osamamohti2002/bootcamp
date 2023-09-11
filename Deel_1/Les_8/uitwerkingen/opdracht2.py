cijfer = int(input("wat is je cijfer?"))

if cijfer >= 1 and cijfer <= 10:
    omschrijving = {
        10 :'uitmuntend',
        9: 'zeer goed' ,
        8: 'goed',
        7: 'ruim voldoende',
        6: 'voldoende',
        5: 'bijna voldoende',
        4: 'onvoldoende',
        3: 'gerimg',
        2: 'slecht',
        1: 'zeer slecht'

}
    omschrijving = omschrijving[cijfer]
    if cijfer >= 6 :
        print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}" )
    else :
        print(f"Jammer, {omschrijving} je resultaat is en {cijfer}")
else :
    print('Dit kan ik niet omzetten!')





