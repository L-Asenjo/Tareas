import random

def leer(defensa):
    defensa-=10
    
    if defensa <= 0:
        defensa=1
    
    return defensa

def tackle(vida, defensa):
    vida-= 35/(defensa/100)
    return vida

def ember(vida, defensa):
    vida-=40/(defensa/100)
    return vida

def tail_whip(defensa):
    defensa-=10
    
    if defensa <= 0:
        defensa=1
    
    return defensa

def water_gun(vida, defensa):
    vida-=40/(defensa/100)
    return vida



ps_J=100
ps_O=100
def_J=100
def_O=100
movimientos={
    "atk_J":[
        "leer",
        "tackle",
        "ember"
        ],
    "atk_O":[
        "tail whip",
        "tackle",
        "water gun"
        ]
}

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

while ps_J>0 and ps_O>0:
    if ps_J>0:
        for i, m in enumerate(movimientos['atk_J']):
            print(i+1, m)

        x = input("Estos son tus movimientos, qué hará tu pokemon? ")
        x.lower()
        if x in movimientos["atk_J"]:
            if x == movimientos["atk_J"][0]:
                def_O = leer(def_O)
                dmgJ=0
            elif x == movimientos["atk_J"][1]:
                dmgJ = ps_O - tackle(ps_O, def_O)
                ps_O = tackle(ps_O,def_O)
            else:
                dmgJ = ps_O - ember(ps_O, def_O)
                ps_O = ember(ps_O,def_O)
            print(msj["atk_J"][x.lower()].format(dmgJ))
        else:
            print("Tu pokemon no conoce ese ataque")
            continue
    else:
        break
    if ps_O>0:  
        y = random.randrange(0, 3)
        y = movimientos["atk_O"][y]
        if y == movimientos["atk_O"][0]:
            def_J = tail_whip(def_J)
            dmgO=0
        elif y == movimientos["atk_O"][1]:
            dmgO=ps_J - tackle(ps_J, def_J)
            ps_J = tackle(ps_J, def_J)
        elif y == movimientos["atk_O"][2]:
            dmgO=ps_J - water_gun(ps_J, def_J)
            ps_J = water_gun(ps_J, def_J)
        print(msj["atk_O"][y].format(dmgO))
    else:
        break

if ps_J>0:
    print("Felicidades! Has ganado!")
elif ps_O>0:
    print("Oh, no! Tu pokemon ha sido debilitado!")