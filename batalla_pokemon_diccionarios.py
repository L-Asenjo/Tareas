import random
ps_J=100
ps_O=100
def_J=100
def_O=100
movimientos={"atk_J": ["leer", "tackle", "ember"], "atk_O" : ["tail whip", "tackle", "water gun"]}
mov_calc={"leer": 10, "tackle": 35*100, "ember": 40/(def_O/100), "tail whip": 10, "water gun":40/(def_J/100)}

while ps_J>0 and ps_O>0:
    if ps_J>0:
        print(movimientos["atk_J"])
        x = input("Estos son tus ataques, qué hará tu pokemon?")
        x.lower()
        if x == movimientos["atk_J"][0]:
            def_O-=mov_calc["leer"]
            print("Has usado leer, la defensa del pokemon oponente ha sido reducida")
            if def_O <= 0:
                def_O=1
        elif x == movimientos["atk_J"][1]:
            ps_O-= mov_calc["tackle"]/def_O
            print("Has usado tackle, has inflingido", 35/(def_O/100), "puntos de daño")
        elif x == movimientos["atk_J"][2]:
            ps_O-= mov_calc["ember"]
            print("Has usado ember, has inflingido", 40/(def_O/100), "puntos de daño")
        else:
            print("Tu pokemon no conoce ese ataque")
            continue
    else:
        break
    if ps_O>0:  
        y = random.randrange(0, 3)
        y = movimientos["atk_O"][y]
        if y == movimientos["atk_O"][0]:
            def_J-=mov_calc["tail whip"]
            print("El pokemon oponente ha usado tail whip, la defensa de tu pokemon ha sido reducida")
            if def_J <= 0:
                def_J=1
        elif y == movimientos["atk_O"][1]:
            ps_J-= mov_calc["tackle"]/def_J
            print("El pokemon oponente ha usado tackle, tu pokemon ha perdido", 35/(def_J/100), "puntos de salud")
        elif y == movimientos["atk_O"][2]:
            ps_J-= mov_calc["water gun"]
            print("El pokemon oponente ha usado water gun, tu pokemon ha perdido", 40/(def_J/100), "puntos de salud")
    else:
        break

if ps_J>0:
    print("Felicidades! Has ganado!")
elif ps_O>0:
    print("Oh, no! Tu pokemon ha sido debilitado!")