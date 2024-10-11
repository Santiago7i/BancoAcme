from .validaciones import *
from .transacciones import movimiento, dbMovimiento
numCuenta = 1
dbCuentas = []

def registrar():
    global numCuenta
    cliente = {"numCuenta": str(numCuenta)}
    cliente["documento"] = input("★ ! Por favor digite el número de documento -> ")
    if validar(cliente["documento"]):
        nombre = input("★ ! Por favor escriba su nombre -> ")
        if vacio(nombre) == False:
            cliente["nombre"] = nombre
            contraseña = input("★ ! Por ingrese una contraseña -> ")
            if vacio(contraseña) == False:
                cliente["pass"] = contraseña
                cliente["saldo"] = 0
                dbCuentas.append(cliente)
                print("────────────────────── ༯ ──────────────────────")
                print("¡¡( ✓ ) CUENTA CREADA EXITOSAMENTE !!")
                print("-ˏˋ 👤 SU NÚMERO DE CUENTA ES: ", numCuenta)
                numCuenta += 1
            
def acceso(menu):
    cliente = buscar("0", dbCuentas)
    if cliente:
        contraseña = input("★ ! Por favor digite la contraseña -> ")
        print("")
        if cliente["pass"] == contraseña:
            if menu == "3":               # -------------------------------------------------------------\             # Se ejecuta solo si
                dinero = input("¿ Cuanto dinero desea retirar ? -> ")                                                  # la opcion del menu es 3
                if validar(dinero):
                    movimiento(cliente, int(dinero), menu)
            if menu == "4":               # -------------------------------------------------------------\
                dinero = 0                                                              # Se ejecuta solo si
                movimiento(cliente, dinero, menu)                                             # la opcion del menu es 4
            if menu == "5":            # ----------------------------------------------------------------/
                print("Fecha ══ Tipo  ══ Referencia ══ descripcion ══ Valor ══ saldo")            
                for mov in dbMovimiento:                                                     # Se ejecuta solo si
                    if cliente["numCuenta"] == mov["numCuenta"]:                             # la opcion del menu es 5
                        print(mov["fecha"], " -- ", mov["tipo"]," -- ",mov["numRef"]," -- ",mov["desc"]," -- ",mov["valor"]," -- ",mov["saldo"])
        else:
            print("( X ) Contraseña incorrecta")