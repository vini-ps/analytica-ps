def angulo_ponteiros(horario):
    horas = int(horario[:2])
    minutos = int(horario[3:])
    angulo = abs(abs(horas-12)*30 - minutos*6)
    replementar = 360 - angulo
    if angulo > 180:
        return replementar
        #replementar = 360 - angulo
    return angulo

def verifica_horario(horario):
    if len(horario) != 5:
        return False
    elif int(horario[:2]) not in range(25):
        return False
    elif int(horario[3:]) not in range(60):
        return False
    elif horario[2] != ':':
        return False
    return True

def main ():
    horario = input("Digite o horario: ")
    while verifica_horario(horario) != True:
        print("\nhorario inválido!\n")
        horario = input("Digite o horario: ")
        if horario == 'f':
            exit()
    menor_angulo = angulo_ponteiros(horario)
    print(f"{menor_angulo}º")

main()
