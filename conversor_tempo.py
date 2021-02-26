Seg = input("digite os segundos a serem convertidos \n")

Seg_int = int(Seg)

Segundos = Seg_int % 60

Temp_rest = Seg_int // 60

Minutos = Temp_rest % 60

Temp2_rest = Temp_rest // 60

Horas = Temp2_rest % 24

Dias = Temp2_rest // 24

print ( Dias, "dias", Horas, "horas", Minutos, "minutos e", Segundos, "segundos")
