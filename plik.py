kredyt = input('Podaj kwotę kredytu: ')
rata = input('Podaj wysokość raty: ')
procent = input('Podaj wysokość oprocentowania w %: ')


styczen1_inflacja = 1.59282448436825
styczen1_pozostalo = (1 + ((styczen1_inflacja + float(procent))/1200)) * float(kredyt) - float(rata)
styczen1_roznica = float(kredyt) - styczen1_pozostalo

luty1_inflacja = -0.453509101198007
luty1_pozostalo = (1 + ((luty1_inflacja + float(procent))/1200)) * styczen1_pozostalo - float(rata)
luty1_roznica = styczen1_pozostalo - luty1_pozostalo

marzec1_inflacja = 2.32467171712441
marzec1_pozostalo = (1 + ((marzec1_inflacja + float(procent))/1200)) * luty1_pozostalo - float(rata)
marzec1_roznica = luty1_pozostalo - marzec1_pozostalo

kwiecien1_inflacja = 1.26125440724877
kwiecien1_pozostalo = (1 + ((kwiecien1_inflacja + float(procent))/1200)) * marzec1_pozostalo - float(rata)
kwiecien1_roznica = marzec1_pozostalo - kwiecien1_pozostalo

maj1_inflacja = 1.78252628571251
maj1_pozostalo = (1 + ((maj1_inflacja + float(procent))/1200)) * kwiecien1_pozostalo - float(rata)
maj1_roznica = kwiecien1_pozostalo - maj1_pozostalo

czerwiec1_inflacja = 2.32938454145522
czerwiec1_pozostalo = (1 + ((czerwiec1_inflacja + float(procent))/1200)) * maj1_pozostalo - float(rata)
czerwiec1_roznica = maj1_pozostalo - czerwiec1_pozostalo

lipiec1_inflacja = 1.50222984223283
lipiec1_pozostalo = (1 + ((lipiec1_inflacja + float(procent))/1200)) * czerwiec1_pozostalo - float(rata)
lipiec1_roznica = czerwiec1_pozostalo - lipiec1_pozostalo

sierpien1_inflacja = 1.78252628571251
sierpien1_pozostalo = (1 + ((sierpien1_inflacja + float(procent))/1200)) * lipiec1_pozostalo - float(rata)
sierpien1_roznica = lipiec1_pozostalo - sierpien1_pozostalo

wrzesien1_inflacja = 2.32884899407637
wrzesien1_pozostalo = (1 + ((wrzesien1_inflacja + float(procent))/1200)) * sierpien1_pozostalo - float(rata)
wrzesien1_roznica = sierpien1_pozostalo - wrzesien1_pozostalo

pazdziernik1_inflacja = 0.616921348207244
pazdziernik1_pozostalo = (1 + ((pazdziernik1_inflacja + float(procent))/1200)) * wrzesien1_pozostalo - float(rata)
pazdziernik1_roznica = wrzesien1_pozostalo - pazdziernik1_pozostalo

listopad1_inflacja = 2.35229588637833
listopad1_pozostalo = (1 + ((listopad1_inflacja + float(procent))/1200)) * pazdziernik1_pozostalo - float(rata)
listopad1_roznica = pazdziernik1_pozostalo - listopad1_pozostalo

grudzien1_inflacja = 0.337779545187098
grudzien1_pozostalo = (1 + ((grudzien1_inflacja + float(procent))/1200)) * listopad1_pozostalo - float(rata)
grudzien1_roznica = listopad1_pozostalo - grudzien1_pozostalo

styczen2_inflacja = 1.57703524727525
styczen2_pozostalo = (1 + ((styczen2_inflacja + float(procent))/1200)) * grudzien1_pozostalo - float(rata)
styczen2_roznica = grudzien1_pozostalo - styczen2_pozostalo

luty2_inflacja = -0.292781442607648
luty2_pozostalo = (1 + ((luty2_inflacja + float(procent))/1200)) * styczen2_pozostalo - float(rata)
luty2_roznica = styczen2_pozostalo - luty2_pozostalo

marzec2_inflacja = 2.48619659017508
marzec2_pozostalo = (1 + ((marzec2_inflacja + float(procent))/1200)) * luty2_pozostalo - float(rata)
marzec2_roznica = luty2_pozostalo - marzec2_pozostalo

kwiecien2_inflacja = 0.267110317834564
kwiecien2_pozostalo = (1 + ((kwiecien2_inflacja + float(procent))/1200)) * marzec2_pozostalo - float(rata)
kwiecien2_roznica = marzec2_pozostalo - kwiecien2_pozostalo

maj2_inflacja = 1.41795267229799
maj2_pozostalo = (1 + ((maj2_inflacja + float(procent))/1200)) * kwiecien2_pozostalo - float(rata)
maj2_roznica = kwiecien2_pozostalo - maj2_pozostalo

czerwiec2_inflacja = 1.05424326726375
czerwiec2_pozostalo = (1 + ((czerwiec2_inflacja + float(procent))/1200)) * maj2_pozostalo - float(rata)
czerwiec2_roznica = maj2_pozostalo - czerwiec2_pozostalo

lipiec2_inflacja = 1.4805201044812
lipiec2_pozostalo = (1 + ((lipiec2_inflacja + float(procent))/1200)) * czerwiec2_pozostalo - float(rata)
lipiec2_roznica = czerwiec2_pozostalo - lipiec2_pozostalo

sierpien2_inflacja = 1.57703524727525
sierpien2_pozostalo = (1 + ((sierpien2_inflacja + float(procent))/1200)) * lipiec2_pozostalo - float(rata)
sierpien2_roznica = lipiec2_pozostalo - sierpien2_pozostalo

wrzesien2_inflacja = -0.0774206903147018
wrzesien2_pozostalo = (1 + ((wrzesien2_inflacja + float(procent))/1200)) * sierpien2_pozostalo - float(rata)
wrzesien2_roznica = sierpien2_pozostalo - wrzesien2_pozostalo

pazdziernik2_inflacja = 1.16573339872354
pazdziernik2_pozostalo = (1 + ((pazdziernik2_inflacja + float(procent))/1200)) * wrzesien2_pozostalo - float(rata)
pazdziernik2_roznica = wrzesien2_pozostalo - pazdziernik2_pozostalo

listopad2_inflacja = -0.404186717638335
listopad2_pozostalo = (1 + ((listopad2_inflacja + float(procent))/1200)) * pazdziernik2_pozostalo - float(rata)
listopad2_roznica = pazdziernik2_pozostalo - listopad2_pozostalo

grudzien2_inflacja = 1.49970852083123
grudzien2_pozostalo = (1 + ((grudzien2_inflacja + float(procent))/1200)) * listopad2_pozostalo - float(rata)
grudzien2_roznica = listopad2_pozostalo - grudzien2_pozostalo




print('Twoja pozostała kwota kredytu to:', styczen1_pozostalo,', to:', styczen1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', luty1_pozostalo,', to:', luty1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', marzec1_pozostalo,', to:', marzec1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', kwiecien1_pozostalo,', to:', kwiecien1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', maj1_pozostalo,', to:', maj1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', czerwiec1_pozostalo,', to:', czerwiec1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', lipiec1_pozostalo,', to:', lipiec1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', sierpien1_pozostalo,', to:', sierpien1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', wrzesien1_pozostalo,', to:', wrzesien1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', pazdziernik1_pozostalo,', to:', pazdziernik1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', listopad1_pozostalo,', to:', listopad1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', grudzien1_pozostalo,', to:', grudzien1_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', styczen2_pozostalo,', to:', styczen2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', luty2_pozostalo,', to:', luty2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', marzec2_pozostalo,', to:', marzec2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', kwiecien2_pozostalo,', to:', kwiecien2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', maj2_pozostalo,', to:', maj2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', czerwiec2_pozostalo,', to:', czerwiec2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', lipiec2_pozostalo,', to:', lipiec2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', sierpien2_pozostalo,', to:', sierpien2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', wrzesien2_pozostalo,', to:', wrzesien2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', pazdziernik2_pozostalo,', to:', pazdziernik2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', listopad2_pozostalo,', to:', listopad2_roznica, 'mniej niż w poprzednim miesiącu.')
print('Twoja pozostała kwota kredytu to:', grudzien2_pozostalo,', to:', grudzien2_roznica, 'mniej niż w poprzednim miesiącu.')
