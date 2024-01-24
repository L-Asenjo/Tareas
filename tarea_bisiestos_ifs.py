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
