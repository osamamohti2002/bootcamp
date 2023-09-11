leeftijd = int(input('wat is je leetijd?'))
snor = str(input('heb je snor ja/nee'))
diploma = str(input('heb je diploma ja/nee'))

if leeftijd >= 18 and snor == 'ja':
    print('je bent aangenomen')
elif diploma == 'ja':
    print('je bent aangenomen')
else:
    print('je bent niet aangenomen')