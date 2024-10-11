from .validaciones import *
from datetime import datetime

dbMovimiento = [] 
numRef = 1

def consignar(dbCuentas):                  
    print("|❜ ⌗ . . . . . . . . . . . . . . . . . . .⌗ ❜|")                                                           
    print("|   ⌗ Para consignar por favor seleccione ⌗  |")
    print("|                                            |")
    print("|     ( 0. ) 🏷️  Número de cuenta             |")
    print("|     ( 1. ) 🔖  Número de documento         |")
    print("|❜ ⌗ . . . . . . . . . . . . . . . . . . .⌗ ❜|")
    print("")
    opc = input() 
    cliente = buscar(opc, dbCuentas) #se llama la funcion buscar para buscar los datos del usuario en los diccionarios que se han dado como parametros
    if cliente:
        print(" ( 💸 ) ")
        dinero = input(" ¿ Cuanto dinero desea consignar ? -> ")
        if validar(dinero):
            movimiento(cliente, int(dinero), "2")
def movimiento(cliente, dinero, menu):                                                   # menu = toma el valor segun 
    global numRef                                                                   # la eleccion del menu principal
    registrar = False             
    if menu == "2":                           # ---------------------------------------------------------------\
        cliente["saldo"] += dinero                                                   #     | Se ejecuta solo si 
        tipo = "Consignación"                                                        #     | La opcion del menu es 2
        desc = "Consignación a cuenta"
        registrar = True                # -------------------------------------------------------/
    if menu == "3": 
        if cliente["saldo"] < dinero:                 # -----------------------------------------------\
            print("( X ) dinero insuficiente")                                                 #     |
        else:                                                                            #     | Cuando la opcion es 3
            cliente["saldo"] -= dinero                                                   #     |
            tipo = "Descuento"                                                           #     |
            desc = "Retiro en efectivo"
            registrar = True                # --------------------------------------------------------------/
    if menu == "4":                          # -------------------------------------------------------------------\
        print("|❜ ⌗Escriba el servicio a pagar⌗ ❜|")                                         #     |
        print("|     Energía                     |")                                         #     |
        print("|     Agua                        |")                                         #     |
        print("|     Gas                         |")                                         #     |
        print("|❜ ⌗ . . . . . . . . . . . . . ⌗ ❜|")
        print("")
        opc = input().lower()                                                                #     |
        if (opc == "energia") or (opc == "agua") or (opc == "gas"):                          #     |
            ref = input("★ ! Escriba el número de referencia -> ") 
            if validar(ref):                                                                 #     | Si la opción es 4
                dinero = input("★ ! Digite el valor a pagar -> ")
                if validar(dinero):
                    dinero = int(dinero)        #se declara la variable como entero para poder realizar operaciones                                             #     |
                    if cliente["saldo"] < dinero:                                            #     |
                        print("( X ) dinero insuficiente")                                         #     |
                    else:                                                                    #     |
                        cliente["saldo"] -= dinero                                           #     |
                        tipo = "Descuento"                                                   #     |
                        desc = "Pagó un recivo de " + opc + " Ref: " + ref 
                        registrar = True                                                     #     |
        else:                                                                                #     |
            print("( X ) opcion incorrecta")             # ---------------------------------------------------------------/
    if registrar == True: 
        fecha = datetime.now()           # ------------------------------------------------------------------------\
        dbMovimiento.append({
            "numCuenta": cliente["numCuenta"],
            "fecha": fecha.strftime("%c"),
            "tipo": tipo, 
            "numRef": numRef,
            "desc": desc,
            "valor": dinero,
            "saldo": cliente["saldo"]})                                                      #     | Aqui se crea un Movimiento y
        numRef += 1         
        print("────────────────────── ༯ ──────────────────────")                                                          #     | Se agrega a la bdMovimiento
        print("¡¡ TRANSACCION EXITOSA !!")                                                         #     |
        print("-ˏˋ Su nuevo saldo es: $", cliente["saldo"])              # ---------------------------------------------/
