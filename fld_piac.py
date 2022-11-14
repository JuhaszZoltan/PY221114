print('''
=====árlista=====
alma     450Ft/Kg
banán    810Ft/Kg
körte   1140Ft/Kg
narancs  600Ft/Kg
''')
vegosszeg = 0
kerdes = "Jó napot kívánok, szeretne valamit vásárolni? "
while input(kerdes) == 'igen':
    termek = input('mit szeretne vásárolni? ')
    if termek in ['alma', 'banán', 'körte', 'narancs']:
        mennyiseg = float(input(f'hány kilogramm {termek}t adhatok? '))
        if termek == 'alma': vegosszeg += mennyiseg*450
        elif termek == 'banán': vegosszeg += mennyiseg*810
        elif termek == 'körte': vegosszeg += mennyiseg*1140
        elif termek == 'narancs': vegosszeg += mennyiseg*600
    else: print(f'Sajnálom, jelenleg {termek} nincs raktáron!')
    kerdes = 'szeretne valami mást vásárolni? '
print(f'Köszönöm szépen, összesen {round(vegosszeg)} forintot kérnék!')
