namenlijst = ['osama', 'lithe' , 'ahmed' , 'firas' , 'abood']
naam = input('voer een naam in')

if naam in namenlijst:
    namenlijst.remove(naam)
    print(f'de verwijderd naam is {naam}')
    print(f'de bijgewerkte namenlijst is : {namenlijst}')
else:
    namenlijst.append(naam)
    print(f'de toegevoegde naam is {naam}')
    print(f'de bijgewerkte namenlijst: {namenlijst}')