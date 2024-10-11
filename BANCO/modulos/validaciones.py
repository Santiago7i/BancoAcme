def validar(numero):
    try:
        if int(numero) > 0:
            return True
        else:
            print("( X ) El dato ingresado es incorrecto")
    except:
        print("( X ) El dato ingresado es incorrecto")

def buscar(opc, dbCuentas):
    def numcuenta(dbCuentas):
        print("──────────────── ༯ ────────────────")
        num = input("★ ! Por favor digite el número de cuenta -> ")  
        sinCuenta = False                                      
        for cliente in dbCuentas:          # ------------------------------------------------------------------------                     
            if num == cliente["numCuenta"]:                          # Recorre la lista de dbCuentas
                return cliente                                  # y si encuentra num retorna   
            else:                                               # la subcadena = i 
                sinCuenta = True   # --------------------------------------------------------------------------
        if sinCuenta == True:                           # si no lo encuentra
            print("( X ) El número de cuenta no existe !! ")      # escribe un mensaje
    if opc == "1":
        print("        ──────────────── ༯ ────────────────")
        num = input("★ ! Por favor digite el número de documento -> ")
        cuentas = []
        for cliente in dbCuentas:
            if num == cliente["documento"]:
                cuentas.append(cliente)
        if len(cuentas) > 1:
            print("────────────────────── ༯ ──────────────────────")
            print("Numero de cuenta ─⁞─ Documento ─⁞─ Nombre")
            for cuenta in cuentas:
                print(cuenta["numCuenta"]," ─.✦ ", cuenta["documento"]," ─.✦ ", cuenta["nombre"])
            return numcuenta(cuentas)
        elif len(cuentas)==1:
            return cuentas[0]
        else:
            print("( X ) Numero de documento no esta registrado !!")
    elif opc == "0":
        return numcuenta(dbCuentas)
    else:
        print("( X ) Opcion incorrecta !!")
        return None

def vacio(dato):
    if dato.isspace() or dato == "":
        print("( X ) El dato ingresado es incorrecto !!")
    else:
        return False