getal = int(input('voer een getal in'))


if getal >= 0:
    teller = getal

    while teller >= 0:
        print(teller)
        teller -=1
if getal <= 0:
    teller = getal
    while teller <= 0:
        print(teller)
        teller +=1