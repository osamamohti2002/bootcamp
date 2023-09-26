fruiten_lijst = ['appel' , 'druiven' , 'bananen']
fruiten_soort = input('voer een soort fruit in')

if fruiten_soort in fruiten_lijst:
    fruiten_lijst.remove(fruiten_soort)
    print(f'{fruiten_soort} is verwijderd uit de fruitenlijst')
    print(f'het bijgewerkte fruitenlijst is {fruiten_lijst}')
else:
    print('dit soort staat niet in de lijst')