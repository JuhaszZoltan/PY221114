fogyasztas = float(input('autó fogyasztása (l/100Km): '))
benzin_ar = int(input('a benzin literenkénti ára (HUF): '))
ut = float(input('ennyi Km az út hossza: '))
utasok_szama = int(input('utasok száma: '))

utikoltseg = benzin_ar * fogyasztas * ut / 100 / utasok_szama

print(f'egy főre eső útiköltség: {round(utikoltseg)} Ft')