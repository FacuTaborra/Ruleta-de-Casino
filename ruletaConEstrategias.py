import random
import matplotlib.pyplot as plt
# ---------------------------------------------------------
## Variables para metodo Capital Finito
todaslastiradas = []
frecuencia_relativa = []
capital_por_tirada = []
cantidad_tiradas = 0
# ---------------------------------------------------------
## Variables para metodo Capital Infinito

# Número de tiradas
num_tiradas = 50

# Lista para almacenar los resultados de las tiradas
resultados = []
montosM = []
montosD = []
montosA = []
apuesta = random.randint(0, 36)
cajaM = []
cajaD = []
cajaA =[]
monto1 = 1
monto2 = 1

# ---------------------------------------------------------

def ConCapitalInFinito():
    # Realizar las tiradas
    global monto1
    global monto2
    global apuesta
    for i in range(num_tiradas):
        resultados.append(random.randint(0, 36))

        # monto sin estrategia
        montosA.append(random.randint(1, 12000))

        # Modificar apuesta segun resultados
        if apuesta != resultados[i]:
            if i > 0:
                cajaM.append(cajaM[i - 1] - monto1)
                cajaD.append(cajaD[i - 1] - monto2)
                cajaA.append(cajaA[i - 1] - montosA[i])
            else:
                cajaM.append(-monto1)
                cajaD.append(-monto2)
                cajaA.append(-montosA[i])
            montosM.append(monto1)
            monto1 *= 2

            montosD.append(monto2)
            monto2 += 1

        else:
            if i > 0:
                cajaM.append(cajaM[i - 1] + monto1)
                cajaD.append(cajaD[i - 1] + monto2)
                cajaA.append(cajaA[i - 1] + montosA[i])
            else:
                cajaM.append(+monto1)
                cajaD.append(+monto2)
                cajaA.append(+montosA[i])
            montosM.append(monto1)
            monto1 = 1

            montosD.append(monto2)
            monto2 -= 1

    # Muestra de monto apostado y resultado
    print("Metodo: La Martingala")
    for i in range(num_tiradas):
        print("Numero de tirada: ", i + 1, "     Resultado: ", resultados[i], "     Caja: ", cajaM[i],
              "      Monto apostado: ", montosM[i])
    print("")
    print("Metodo: D'Alembert")
    for i in range(num_tiradas):
        print("Numero de tirada: ", i + 1, "     Resultado: ", resultados[i], "     Caja: ", cajaD[i],
              "      Monto apostado: ", montosD[i])
    print("")

    print("numero aleatoreo para la apuesta sin estrategia" + str(apuesta))
    print("Metodo: Creado")
    for i in range(num_tiradas):
        print("Numero de tirada: ", i + 1, "     Resultado: ", resultados[i], "     Caja: ", cajaA[i],
              "      Monto apostado: ", montosA[i])

    plt.plot(cajaM)
    plt.title('Capital por tirada Martingala')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Capital')
    plt.show()

    plt.plot(cajaD)
    plt.title("Capital por tirada D'Alambert")
    plt.xlabel('Número de tiradas')
    plt.ylabel('Capital')
    plt.show()
    plt.plot(cajaA)
    plt.title('Capital por tirada aleatorio')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Capital')
    plt.show()

def ConCapitalFinito():
    print("El metodo consiste en apostar 10 fichas a los primeros 12 numeros en la casilla unica y de igual forma a la tercera bandeja")
    print("Luego apostamos a 10 numeros de la bandeja del medio pero solo una ficha por numero")
    print("Vamos a dejar unicamente libres los numeros 19 y 16, es decir que solo perderemos con esos numeros")

    capital = int(input('Cuanto capital desea apostar: '))
    capitalFinal = tiradas(capital)

    print(' ------------------------------------------ ')
    if capitalFinal > 30:
        print("Usted gano, su capital final es de " + str())
    else:
        print("Usted perdio, capital fina: " + str(capitalFinal))


def tiradas(capital):
    global cantidad_tiradas
    print(
        "Vamos a fijar que la apuesta minima de una ficha tiene que ser 30, una vez que la apuesta sea menor a eso se corta la apuesta inmediatamente")

    capitalMaximo = capital * 2

    print('El capital con el que nos retiramos es ' + str(capitalMaximo))

    numeros_perdedores = [0, 16, 19]

    while capital >= 30 and capitalMaximo >= capital:
        cantidad_tiradas = + 1
        ## descontamos la tirada
        capital = capital - 30
        tirada = random.randint(0, 36)
        todaslastiradas.append(tirada)
        print('Numero de la tirada: ' + str(tirada))
        if numeros_perdedores.__contains__(tirada):
            print("perdida, se restan 30 fichas, capital actual: " + str(capital))
        else:
            if [12, 14, 15, 17, 18, 20, 21, 22, 23, 24].__contains__(tirada):
                capital = capital + 36
                print('Ganaste, se suman 36 fichas, capital actual ' + str(capital))
            else:
                capital = capital + 30
                print('Ganaste, se suman 20 fichas, capital actual ' + str(capital) + 'Se recupera lo apostado')

        capital_por_tirada.append(capital)

    frecuencia_relativa = [todaslastiradas.count(i) / cantidad_tiradas for i in range(37)]
    graficar(frecuencia_relativa, capital_por_tirada)
    return capital


def graficar(fr, cxt):
    # grafica frecuencia relativa por el numero de tiradas
    plt.bar(range(37), fr)
    plt.title('Frecuencia relativa - Numero de Tiradas')
    plt.xlabel('Número')
    plt.ylabel('Frecuencia relativa')
    plt.show()

    # capital por aca tirada
    plt.plot(cxt)
    plt.title('Capital por tirada')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Capital')
    plt.show()



def elegir_estrategia():
    print("Elige una estrategia ")
    print("1 - Capital Finito ")
    print("2 - Capital Infinito")

    op = 0
    while 2 <= op <= 1 or op == 0:
        op = int(input('Elige una opcion: '))

    if op == 1:
        ConCapitalFinito()
    else:
        ConCapitalInFinito()


elegir_estrategia()

