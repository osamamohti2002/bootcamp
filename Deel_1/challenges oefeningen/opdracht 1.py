jou_cijfer = float(input('wat is je cijfer'))
#letter_cijfer = ('A' , 'B', 'C' , 'D' 'F')
cijfers = (1,2,3,4,5,6,7,8,9,10)
if 8.5 <= jou_cijfer <= 10:
    print('je cijfer is een A')
elif 7.5<= jou_cijfer <= 8:
    print('je cijfer is een B')
elif 6.5 <= jou_cijfer <= 7:
    print('je cijfer is eem C')
elif 5.5 <= jou_cijfer <= 6:
    print('je cijfer is een D')
elif 5 >= jou_cijfer:
    print('je cijfer is een F')
else:
    print('ongeldige cijfer')