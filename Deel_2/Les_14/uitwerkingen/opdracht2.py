getallenLijst = [20,40,50,60,44,23,5,]
index = int(input('voer een getal tussen 0-6 om een index te verwijderen'))

if index >=0 and index < len(getallenLijst):
    getal_verwijderen = getallenLijst.pop(index)
    print(f'het verwijderd index is {getal_verwijderen}')
    print(f'het bijgewerkte lijst is: {getallenLijst}')