testtomeg = int(input('testtömeged (Kg): '))
magassag = int(input('testmagasságod (cm): ')) / 100

tti = testtomeg / magassag ** 2

osztaly = '-'
if tti < 16: osztaly = 'súlyos soványság'
elif tti < 17: osztaly = 'mérsékelt soványság'
elif tti < 18.5: osztaly = 'enyhe soványság'
elif tti < 25: osztaly = 'normális testsúly'
elif tti < 30: osztaly = 'túlsúlyos'
elif tti < 35: osztaly = 'I. fokú elhízás'
elif tti < 40: osztaly = 'II. fokú elhízás'
else: osztaly = 'III. fokú (súlyos) elhízás'
print(f'tti = {round(tti, 1)}; testsúlyosztályod: "{osztaly}"')