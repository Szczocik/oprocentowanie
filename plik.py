
kredyt = input('Podaj kwotę kredytu: ')
rata = input('Podaj wysokość raty: ')
procent = input('Podaj wysokość oprocentowania w %: ')


styczen1_inflacja = 1.59282448436825
styczen1_pozostalo = (1 + ((styczen1_inflacja + float(procent))/1200)) * float(kredyt) - float(rata)
styczen1_roznica = float(kredyt) - styczen1_pozostalo




print('Twoja pozostała kwota kredytu to:', styczen1_pozostalo,', to:', styczen1_roznica, 'mniej niż w poprzednim miesiącu.')




