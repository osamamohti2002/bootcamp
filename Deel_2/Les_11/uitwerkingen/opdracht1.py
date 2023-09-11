import random

name = ( input('Wat is jouw naam? '))
print('Hallo', name)
favoriteSeason = input(f'wat is je favorite seizon {name} A) lente B) zomer C) herfst D) winter  ')
answer = favoriteSeason.lower()
if answer == 'a' :
    print('ik hou van de lente')
elif answer == 'b':
    print('De zomer is voor mij te warm')
elif answer == 'c' :
    print('Mooi he, al die blaadjes die dan van de boom vallen.')
elif answer == 'd' :
    print('Is de winter niet erg koud?')
else:
    print('dit ken ik niet, graag antwoorden met A, B, C, D ')

import random

favoriteColor = input('wat is je favorite kleur?')
random_number = random.randint(0,9.)

if random_number % 2 == 0 :
    print(f'ik vind {favoriteColor} ook een mooie kleur')
else :
    print(f'TBG, ik hou niet zo van {favoriteColor} ')