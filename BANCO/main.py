from modulos.transacciones import *
from modulos.usuario import *

def opciones():
    print("")
    print()
    print("       ¡ Bienvenido a Acme Bank !       ")
    print("╒═〨══════════════════════════════〨═╕")
    print("|       1. Crear una cuenta          |")
    print("|       2. Consignar dinero          |")
    print("| ⌗     3. Retirar dinero        ⌗   |")
    print("|       4. Pagar servicios           |")
    print("|       5. Lista de movimientos      |")
    print("|       0. Salir                     |")
    print("╘════════════════════════════════════╛")
    print("")
    opc = input()
    return opc

while True:
    menu = opciones()
    match menu:
        case "1":
            
            print("    「 ✦ 1. ✦ 」  ── 📋 ˙  Registro !!  ")
            registrar()
        case "2":
            print("  「 ✦ 2. ✦ 」  ── 📮 ˙  Consignar Dinero !!  ")
            consignar(dbCuentas)
        case "3":
            print("    「 ✦ 3. ✦ 」  ── 💰 ˙  Retirar Dinero !!  ")
            print("★ ! Para retirar:")
            acceso(menu)
        case "4":
            print("    「 ✦ 4. ✦ 」  ── 💳 ˙  Pago de Servicios !!  ")
            print("★ ! Pago de servicios")
            acceso(menu)
        case "5":
            print("    「 ✦ 5. ✦ 」  ── 🗒️ ˙  Ver Movimientos !!      ")
            print("★ ! Listado de movimientos")
            acceso(menu)
        case "0":
            print("    「 ✦ 6. ✦ 」  ── ⌛ ˙  Fin !!      ")
            print("★ ! Gracias Por Preferir nuestro banco")
            break
        case _:
            print("( X ) opcion incorrecta")
    print("")
    input("-- PRESIONE ENTER PARA CONTINUAR --")