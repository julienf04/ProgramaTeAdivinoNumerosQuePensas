import json


listaDeNumeros1 = list([list([])] * 10)
listaDeNumeros2 = list([list([list([])] * 10)] * 10)
listaDeNumeros3 = list([list([list([list([])] * 10)] * 10)] * 10)
listaDeNumeros4 = list([list([list([list([list([])] * 10)] * 10)] * 10)] * 10)

deseaRepetir = ""



def RomperLasBolas(datoDelUsuario, numReferencia): # Si el usuario pone alguna palabra o un numero que no sea el 1 al 10, le pregunta de nuevo el numero
    numeritoEnString = ""
    if numReferencia == 1: numeritoEnString = "primer"
    elif numReferencia == 2: numeritoEnString = "segundo"
    elif numReferencia == 3: numeritoEnString = "tercer"
    elif numReferencia == 4: numeritoEnString = "cuarto"
    elif numReferencia == 5: numeritoEnString = "quinto"

    while datoDelUsuario.isnumeric() == False or int(datoDelUsuario) >= 11 or int(datoDelUsuario) <= 0:
        print("Acordate, los numeros que pienses tienen que ser numeros enteros. Cuando estes listo, pone el " + numeritoEnString + " numero que pensaste: ", end="")
        datoDelUsuario = input()

    return datoDelUsuario





def AñadirLosNumerosAlConocimientoDeLaAI(InicialOrFinal): #Añade los numeros al conocimiento de la AI, osea, a las listas
    if InicialOrFinal == 0:
        elIndex1 = int(numeroInicial1) - 1
        elIndex2 = int(numeroInicial2) - 1
        elIndex3 = int(numeroInicial3) - 1
        elIndex4 = int(numeroInicial4) - 1
        elIndex5 = int(numeroInicial5) - 1

    elif InicialOrFinal == 1:
        elIndex1 = int(numeroQuePensoElUsuario_1) - 1
        elIndex2 = int(numeroQuePensoElUsuario_2) - 1
        elIndex3 = int(numeroQuePensoElUsuario_3) - 1
        elIndex4 = int(numeroQuePensoElUsuario_4) - 1
        elIndex5 = int(numeroQuePensoElUsuario_5) - 1


    listaDeNumeros1[elIndex1][elIndex2] += 1
    listaDeNumeros2[elIndex1][elIndex2][elIndex3] += 1
    listaDeNumeros3[elIndex1][elIndex2][elIndex3][elIndex4] += 1
    listaDeNumeros4[elIndex1][elIndex2][elIndex3][elIndex4][elIndex5] += 1






def RecuperarDatos(numeroDeLista):
    listasOpen = open("AI_TeAdivinaLosNumerosQuePensas.json", "r")
    listasRead = listasOpen.read()
    listasLoads = json.loads(listasRead)

    listaDeNumeros1 = listasLoads["listas"][0]
    listaDeNumeros2 = listasLoads["listas"][1]
    listaDeNumeros3 = listasLoads["listas"][2]
    listaDeNumeros4 = listasLoads["listas"][3]

    if numeroDeLista == 1:
        return listaDeNumeros1
    elif numeroDeLista == 2:
        return listaDeNumeros2
    elif numeroDeLista == 3:
        return listaDeNumeros3
    elif numeroDeLista == 4:
        return listaDeNumeros4



def GuardarDatos():
    archivoParaDumpear = { "listas" : [listaDeNumeros1, listaDeNumeros2, listaDeNumeros3, listaDeNumeros4] }

    archivoDumpeado = json.dumps(archivoParaDumpear)

    listasOpen=  open("AI_TeAdivinaLosNumerosQuePensas.json", "w")
    listasOpen.write(archivoDumpeado)













print("Hola, soy la AI. Te voy a hacer pensar numeros entero del 1 al 10 y yo voy a tratar de predecirlos")
print()




listaDeNumeros1 = RecuperarDatos(1)
listaDeNumeros2 = RecuperarDatos(2)
listaDeNumeros3 = RecuperarDatos(3)
listaDeNumeros4 = RecuperarDatos(4)

print("Pensa en un numero entero del 1 al 10 y ponelo aca:  ", end="")
numeroInicial1 = input() #le pregunto el primer numero para empezar a calcular y tratar de adivinar
numeroInicial1 = RomperLasBolas(numeroInicial1, 1)

print("Pensa en otro numero del 1 al 10 y ponelo aca:  ", end="")
numeroInicial2 = input()  #le pregunto el segundo numero para empezar a calcular y tratar de adivinar
numeroInicial2 = RomperLasBolas(numeroInicial2, 2)

print("Pensa en otro numero del 1 al 10 y ponelo aca:  ", end="")
numeroInicial3 = input()  #le pregunto el tercer numero para empezar a calcular y tratar de adivinar
numeroInicial3 = RomperLasBolas(numeroInicial3, 3)

print("Pensa en otro numero del 1 al 10 y ponelo aca:  ", end="")
numeroInicial4 = input()  #le pregunto el cuarto numero para empezar a calcular y tratar de adivinar
numeroInicial4 = RomperLasBolas(numeroInicial4, 4)

print("Pensa en otro numero del 1 al 10 y ponelo aca:  ", end="")
numeroInicial5 = input()  #le pregunto el quinto numero para empezar a calcular y tratar de adivinar
numeroInicial5 = RomperLasBolas(numeroInicial5, 5)



#Le agrego los 5 numeros de referencia iniciales que me dio al principio
AñadirLosNumerosAlConocimientoDeLaAI(0)



while deseaRepetir != "Salir" and deseaRepetir != "salir" and deseaRepetir != "SALIR":
    # Empieza el proceso de intentar predecir los numeros
    print()
    print("Genial. Ahora si, pensa en 5 numeros enteros del 1 al 10, pero no los pongas todavia. Tene los 5 numeros ya en mente")
    print("Una vez que los tengas en mente, escribi la palabra 'predecir' para que intente predecir tus numeros: ", end="")
    palabraClave_predecir = input()

    while palabraClave_predecir != "predecir":  # Mientras que no confirme, no va a poder seguir para que adivine los numeros
        print("No terminaste de pensar tus numeros? No te preocupes! Espero sin problemas. Una vez que los tengas en mente, escribi la palabra 'predecir' para que intente predecir tus numeros: ", end="")
        palabraClave_predecir = input()



    print()
    print("Antes de predecir tus numeros, necesito que pongas el primer numero que pensaste, y yo intentare predecir los demas 4 numeros siguientes: ", end="")
    numeroDeLaPrediccion1_INICIAL = input()
    numeroDeLaPrediccion1_INICIAL = RomperLasBolas(numeroDeLaPrediccion1_INICIAL, 1)

    numeroDeLaPrediccion2 = 0
    numeroDeLaPrediccion3 = 0
    numeroDeLaPrediccion4 = 0
    numeroDeLaPrediccion5 = 0



    ### Operacion para predecir el segundo numero que penso el usuario
    lugarEnElArray1 = int(numeroDeLaPrediccion1_INICIAL) - 1

    max_value = max(listaDeNumeros1[lugarEnElArray1])
    index = listaDeNumeros1[lugarEnElArray1].index(max_value)

    numeroDeLaPrediccion2 = index + 1



    ### Operacion para predecir el tercer numero que penso el usuario
    lugarEnElArray2 = numeroDeLaPrediccion2 - 1

    lista_n = listaDeNumeros2[lugarEnElArray1]

    max_value = max(lista_n[lugarEnElArray2])
    index = lista_n[lugarEnElArray2].index(max_value)

    numeroDeLaPrediccion3 = index + 1



    ### Operacion para predecir el cuarto numero que penso el usuario
    lugarEnElArray3 = numeroDeLaPrediccion3 - 1

    lista_n = listaDeNumeros3[lugarEnElArray1]
    lista_h = lista_n[lugarEnElArray2]

    max_value = max(lista_h[lugarEnElArray3])
    index = lista_h[lugarEnElArray3].index(max_value)

    numeroDeLaPrediccion4 = index + 1



    ### Operacion para predecir el cuarto numero que penso el usuario
    lugarEnElArray4 = numeroDeLaPrediccion4 - 1

    lista_n = listaDeNumeros4[lugarEnElArray1]
    lista_h = lista_n[lugarEnElArray2]
    lista_x = lista_h[lugarEnElArray3]

    max_value = max(lista_x[lugarEnElArray4])
    index = lista_x[lugarEnElArray4].index(max_value)

    numeroDeLaPrediccion5 = index + 1



    #Le muestro al usuario los numeros que pienso que penso xd. Basicamente le digo mi adivinanza de numeros
    print(numeroDeLaPrediccion2)
    print(numeroDeLaPrediccion3)
    print(numeroDeLaPrediccion4)
    print(numeroDeLaPrediccion5)




    ###Le pregunto si adivine o no, y que me ponga los numeros suyos de verdad para que despues pueda mejorar esta AI con el machine learning
    print()
    print("Adivine? Por favor pone los 5 numeros que pensaste, para en proximos intentos poder predecir con mas eficacia")
    print()

    numeroQuePensoElUsuario_1 = input()
    numeroQuePensoElUsuario_1 = RomperLasBolas(numeroQuePensoElUsuario_1, 1)


    numeroQuePensoElUsuario_2 = input()
    numeroQuePensoElUsuario_2 = RomperLasBolas(numeroQuePensoElUsuario_2, 2)


    numeroQuePensoElUsuario_3 = input()
    numeroQuePensoElUsuario_3 = RomperLasBolas(numeroQuePensoElUsuario_3, 3)

    numeroQuePensoElUsuario_4 = input()
    numeroQuePensoElUsuario_4 = RomperLasBolas(numeroQuePensoElUsuario_4, 4)

    numeroQuePensoElUsuario_5 = input()
    numeroQuePensoElUsuario_5 = RomperLasBolas(numeroQuePensoElUsuario_5, 5)


    AñadirLosNumerosAlConocimientoDeLaAI(1)


    GuardarDatos()


    print()
    print("Desea finalizar el programa? O queres que te siga intentando predecir los numeros? °_°")
    print("Si desea finalizar el programa, solamente cierrelo o escriba SALIR, y si desea seguir con el programa, ponga cualquier otra cosa")
    print()
    deseaRepetir = input()


else:
    print()
    print("presiona cualquier tecla para salir")
    print()