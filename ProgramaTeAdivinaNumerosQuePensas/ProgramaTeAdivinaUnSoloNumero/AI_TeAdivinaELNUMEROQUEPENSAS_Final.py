from json import loads
from json import dumps
import json5
import os
input("import json")
input("import os")
input("from os import close")


input("create finalPathJson variable")
# A la ruta de la carpeta padre le agrego la ruta del archivo json, para obtener la ruta final del archivo json
finalPathJson = "AI_TeAdivinaELNUMEROQUEPENSAS.json"

input("if not os.path.exists(finalPathJson")
if not os.path.exists(finalPathJson):
    print("no existe la ruta")
    ooopen = open(finalPathJson, "w")
    input("en la linea anterio hizo open(finalPathJson")
    ooopen2 = open(finalPathJson, "r")
    input("en la linea anterior se abrio de nuevo el archivo FinalPathJson con un read")
    loads(ooopen2)
    open(finalPathJson, "w")
    input("en la linea anterior se abrio de nuevo el achivo finalPathJson con un write")
else:
    input("si existe la ruta")

hhhhh = input("salio del if else")
listaDeNumeros1 = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

deseaRepetir = ""
username = ""
diccionarioGENERAL = dict()

input("creo las variables")


# Si el usuario pone alguna palabra o un numero que no sea el 1 al 10, le pregunta de nuevo el numero
def RomperLasBolas(datoDelUsuario):

    while datoDelUsuario.isnumeric() == False or int(datoDelUsuario) >= 11 or int(datoDelUsuario) <= 0:
        print("Acordate, el numero que pienses tiene que ser un numero entero. Cuando estes listo, pone el numero que pensaste: ", end="")
        datoDelUsuario = input()

    return datoDelUsuario


# Añade los numeros al conocimiento de la AI, osea, a las listas
def AñadirLosNumerosAlConocimientoDeLaAI(InicialOrFinal):
    if InicialOrFinal == 0:
        elIndex1 = int(numeroInicial1) - 1

    elif InicialOrFinal == 1:
        elIndex1 = int(numeroQuePensoElUsuario_1) - 1

    listaDeNumeros1[elIndex1] += 1


def RecuperarDatos():
    input("va a abrir el json: open(finalPathJson, 'r')")
    listasOpen = open(finalPathJson, "r")
    input("va a leer el archivo con un listasOpen.read()")
    listasRead = listasOpen.read()
    input("va a cargar el archivo con un json.loads(listasRead)")
    listasLoads = loads(listasRead)
    input("cargo exitosamente")

    diccionario = listasLoads
    diccionarioGENERAL = diccionario

    print("Pero antes, ya tenias una cuenta creada? Si es asi, por favor ponga la palabra LOG para recuperar su cuenta, o de lo contrario ponga la palabra CREATE para crear una nueva cuenta", end="\n\n")
    LogOrCreateAccount = input()

    while LogOrCreateAccount != "LOG" and LogOrCreateAccount != "Log" and LogOrCreateAccount != "log" and LogOrCreateAccount != "CREATE" and LogOrCreateAccount != "Create" and LogOrCreateAccount != "create":
        print("Por favor, unicamente ponga la palabra LOG para recuperar su cuenta, o la palabra CREATE para crear una nueva: ", end="")
        LogOrCreateAccount = input()

    if LogOrCreateAccount == "LOG" or LogOrCreateAccount == "Log" or LogOrCreateAccount == "log":
        print("Perfecto! Entonces introduzca su username para recuperar su cuenta. En caso de que no recuerde su username, entonces coloque la palabra CREATE para crear una nueva cuenta", end="\n\n")
        username = input()

        if username == "CREATE" or username == "Create" or username == "create":
            LogOrCreateAccount = "CREATE"

        while username == "CREATE" or username == "Create" or username == "create":
            print(
                "Su username no puede ser la palabra CREATE. Por favor coloque un username diferente")
            username = input()

        laKeyDelUsername = diccionario.get(username)

        while laKeyDelUsername == None:
            print("El username ingresado no fue encontrado, por favor ingrese nuevamente su username. O de lo contrario, coloque la palabra CREATE para crearse una nueva cuenta")
            print()
            username = input()
            if username == "CREATE" or username == "Create" or username == "create":
                LogOrCreateAccount = username
                break
            laKeyDelUsername = diccionario.get(username)

        if laKeyDelUsername != None:
            listaDeNumeros1 = diccionario[username]
            return list([listaDeNumeros1, username, diccionarioGENERAL])

    if LogOrCreateAccount == "CREATE" or LogOrCreateAccount == "Create" or LogOrCreateAccount == "create":
        print("Entonces creemos una cuenta. Lo unico que necesitas es crearte un username e introducirlo aca. IMPORTANTE: El username te permitira acceder a tu cuenta en un futuro. Si te olvidas de tu username, no podras acceder mas a tu cuenta", end="\n\n")
        username = input()

        verificandoSiLaCuentaExiste = diccionario.get(username)
        while verificandoSiLaCuentaExiste != None:
            print("El username ingresado ya existe. Por favor ponga otro username que no exista ni esté siendo usado", end="\n\n")
            username = input()
            verificandoSiLaCuentaExiste = diccionario.get(username)

        diccionario[username] = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        diccionarioGENERAL = diccionario

        cuentaParaDumpear = diccionario

        cuentaDumpeada = dumps(list([cuentaParaDumpear]))

        OpenJson = open(finalPathJson, "w")
        OpenJson.write(cuentaDumpeada)

        return list([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], username, diccionarioGENERAL])


def GuardarDatos():

    listaOpen = open(finalPathJson, "r")
    listaRead = listaOpen.read()
    listaLoads = loads(listaRead)

    diccionarioGENERAL[username] = listaDeNumeros1

    archivoParaDumpear = diccionarioGENERAL

    archivoDumpeado = dumps(archivoParaDumpear)

    listasOpen = open(finalPathJson, "w")
    listasOpen.write(archivoDumpeado)


print("Hola, soy la AI. Te voy a hacer pensar en un numero entero del 1 al 10 y yo voy a tratar de predecirlo")
print()

input("va a recuperar los datos")
datosRecuperados = RecuperarDatos()
input("recupero los datos")
listaDeNumeros1 = datosRecuperados[0]
username = datosRecuperados[1]
diccionarioGENERAL = datosRecuperados[2]


print("Pensa en un numero entero del 1 al 10 y ponelo aca:  ", end="")
# le pregunto el primer numero para empezar a calcular y tratar de adivinar
numeroInicial1 = input()
numeroInicial1 = RomperLasBolas(numeroInicial1)


# Le agrego los 5 numeros de referencia iniciales que me dio al principio
AñadirLosNumerosAlConocimientoDeLaAI(0)


while deseaRepetir != "Salir" and deseaRepetir != "salir" and deseaRepetir != "SALIR":
    # Empieza el proceso de intentar predecir los numeros
    print()
    print("Genial. Ahora si, pensa en un numero entero del 1 al 10, pero no lo pongas todavia. Tene el numero ya en mente")
    print("Una vez que lo tengas en mente, escribi la palabra 'predecir' para que intente predecir el numero: ", end="")
    palabraClave_predecir = input()

    # Mientras que no confirme, no va a poder seguir para que adivine los numeros
    while palabraClave_predecir != "predecir":
        print("No terminaste de pensar el numero? No te preocupes! Espero sin problemas. Una vez que lo tengas en mente, escribi la palabra 'predecir' para que intente predecir el numero: ", end="")
        palabraClave_predecir = input()

    print()
    # Trato de predecir su numero

    max_value = max(listaDeNumeros1)
    numeroDeLaPrediccion = listaDeNumeros1.index(max_value)
    numeroDeLaPrediccion += 1

    # Le muestro al usuario el numero que pienso que penso xd. Basicamente le digo mi adivinanza del numero
    print(numeroDeLaPrediccion)

    # Le pregunto si adivine o no, y que me ponga los numeros suyos de verdad para que despues pueda mejorar esta AI con el machine learning
    print()
    print("Adivine? Por favor pone el numero que pensaste, para poder predecirte mas eficazmente en proximos intentos")
    print()

    numeroQuePensoElUsuario_1 = input()
    numeroQuePensoElUsuario_1 = RomperLasBolas(numeroQuePensoElUsuario_1)

    AñadirLosNumerosAlConocimientoDeLaAI(1)

    GuardarDatos()

    print()
    print("Desea finalizar el programa? O queres que te siga intentando predecir tu numero? °_°")
    print("Si desea finalizar el programa, solamente cierrelo o escriba SALIR, y si desea seguir con el programa, ponga cualquier otra cosa")
    print()
    deseaRepetir = input()


else:
    print()
    print("Presiona cualquier tecla para salir")
    print()
