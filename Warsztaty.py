# Wzór na BMI to BMI = Masa / wzrost^2
"""
Wzor na BMI to ...
"""

waga = float(input('Podaj swoja wage [kg]:'))
wzrost_cm = float(input('Podaj swoj wzrost [cm]:'))
wzrost = wzrost_cm / 100.0
bmi = waga / wzrost**2
print(f'BMI dla Twojego wzrostu {wzrost} i wagi {waga} wynosi {bmi}')

