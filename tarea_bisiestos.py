x = int(input("Inserte un año entre 1900 y 2200 \n"))
base = 1900

if x%4 == 0 and x%100!=0 or x%400==0:
    print('El año', x, 'es bisiesto')
    totala = (x-base)//4
    print('En total hay', totala, 'años bisiestos entre 1900 y ', x)
else:
    print('El año', x, 'no es bisiesto')
    totala = (x-base)//4
    print('En total hay', totala, 'años bisiestos entre 1900 y ', x)




y = int(input("Inserte un año entre 1900 y 2200 \n"))
yb = y
totalb = 0
while yb > base:
    if yb%4 == 0 and yb%100!=0 or yb%400==0:
        totalb += 1
        yb -= 1
    else:
        yb -= 1

if y%4 == 0 and y%100!=0 or y%400==0:
    print('El año', y, 'es bisiesto')
else:
    print('El año', y, 'no es bisiesto')
print('En total hay', totalb,  'años bisiestos entre 1900 y', y)
