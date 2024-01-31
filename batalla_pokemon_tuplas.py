import random
J=(100,100)
ps_J , def_J = J
O=(100,100)
ps_O , def_O = O
movimientos={"atk_J": ["leer", "tackle", "ember"], "atk_O" : ["tail whip", "tackle", "water gun"]}
msj={
    "atk_J": {
        "leer": "Has usado leer, la defensa del pokemon oponente ha sido reducida", 
        "tackle": "Has usado tackle, has inflingido {} puntos de daño", 
        "ember": "Has usado ember, has inflingido {} puntos de daño"
    }, 
    "atk_O": {
        "tail whip": "El pokemon oponente ha usado tail whip, la defensa de tu pokemon ha sido reducida y has perdido 10 puntos de salud", 
        "tackle": "El pokemon oponente ha usado tackle, tu pokemon ha perdido {} puntos de salud", 
        "water gun": "El pokemon oponente ha usado water gun, tu pokemon ha perdido {} puntos de salud"
    }
}

while J[0]>0 and O[0]>0:
    mov_calc={
        "atk_J": {
            "leer": (ps_O, def_O-10), 
            "tackle": (ps_O-35/(def_O/100), def_O), 
            "ember": (ps_O-40/(def_O/100),def_O)
        }, 
        "atk_O": {
            "tail whip": (ps_J-10,def_J-10), 
            "tackle": (ps_J-35/(def_J/100), def_J), 
            "water gun":(ps_J-40/(def_J/100), def_J)
            }
        }
    if J[0]>0:
        print(J[0])
        for i, m in enumerate(movimientos['atk_J']):
            print(i+1, m)

        x = input("Estos son tus ataques, qué hará tu pokemon? ")

        if x.lower() in movimientos['atk_J']:
            dmgJ = O[0] - mov_calc["atk_J"][x.lower()][0]
            O=mov_calc["atk_J"][x.lower()]
            ps_O,def_O=O
            print(msj["atk_J"][x.lower()].format(dmgJ))

            if x == movimientos["atk_J"][0] and def_O <= 0:
                def_O=1

        else:
            print("Tu pokemon no conoce ese ataque")
            continue
    else:
        break
    
    if O[0]>0:  
        y = random.randrange(0, 3)
        y = movimientos["atk_O"][y]
        dmgO= J[0] - mov_calc["atk_O"][y][0]
        J=mov_calc["atk_O"][y]
        ps_J,def_J=J
        print(msj["atk_O"][y].format(dmgO))

        if y == movimientos["atk_O"][0] and def_J <= 0:
                def_J=1
    else:
        break
    print('')

if J[0]>0:
    print("Felicidades! Has ganado!")
elif O[0]>0:
    print("Oh, no! Tu pokemon ha sido debilitado!")