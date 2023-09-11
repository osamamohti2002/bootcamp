color_list = ('rood' ,'blouw' , 'geel' , 'groen')
naam = input('wat is je naam')
favoriteColor = input('wat is je favorite kleur')

if favoriteColor.lower() in color_list :
    print(f'Hallo {naam} ja {favoriteColor} is geweldig')
else:
    print('je kleur is niet mooi')