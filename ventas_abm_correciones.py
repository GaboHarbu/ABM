
# no usar cvs, with, negrita
# buen formato en los listados
# no usar encabezado en el archivo
# no fijarse si el archivo no existe, usar append
# menu en modificaciones
# importe con 2 decimales


import datetime

def validar_numero(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        return False

def validar_palabra(entrada):
    return entrada.strip() != "" and len(entrada) <=20

def ingresar_datos(mensaje, validador):
    while True:
        entrada = input(mensaje)
        if validador(entrada):
            return entrada.strip()
        else:
            print("Entrada no válida. Limitese a 20 caracteres.")


def ancho_columna_importe(arch):
    long_max = 0
    
    for linea in arch:
        venta = list(linea.strip().split(";"))
        if venta[0] != "0":
            long_importe = len(str(float(venta[4])))
            long_max = max(long_max,long_importe)
            
    return long_max


def alta_venta():
    
    date_time = datetime.datetime.now()
    date_time_str = date_time.strftime("%Y-%m-%d %H:%M:%S")

    sucursal = ingresar_datos("Ingrese la sucursal: ", validar_palabra).title()
    producto = ingresar_datos("Ingrese el producto: ", validar_palabra).title()
    
    importe = ingresar_datos("Ingrese el importe: ", validar_numero)

    nueva_venta = ";".join(["1", date_time_str, sucursal, producto, importe+"\n"])

    file = open("Ventas.csv", "a")
    file.write(nueva_venta)
    file.close()

    print("Venta agregada con éxito.")
    

def baja_venta():
    print("\nBorrado")
    arch = open("Ventas.csv","r+")
    posant = 0
    linea = arch.readline()
    
    Borrado = False
    while linea and not Borrado:
        if linea[0] == "0": 
            posant = arch.tell()
            linea = arch.readline()
        else:
            while True: 
                try:
                    venta = linea.strip().split(";")
                    print(f"{'Fecha y Hora':<22}{'Sucursal':<20} {'Producto':<20} {'Importe'}")
                    print(f"{venta[1]:<21} {venta[2]:<20} {venta[3]:<20} {float(venta[4]):>8.2f}")
                    print()
                    print("1. Siguiente Linea")
                    print("2. Borrar")
                    n = int(input("Ingrese opción => ")) 
                    assert n==1 or n==2 
                    break
                except (ValueError, AssertionError): 
                    print("\nIngreso invalido, el valor debe ser 1 o 2")
                
            if n==1:
                posant = arch.tell()
                linea = arch.readline()
            if n==2:
                arch.seek(posant)
                arch.write("0"+linea[1:])
                Borrado = True
    if Borrado:
        print("\nBorrado exitoso")
        print()        
    else:
        print("\nNo hay mas registros")
        print()
                           
    arch.close()

def modificacion_venta():
    print("\nModificaciones")
    arch = open("Ventas.csv","r+")
            
        
    arch.seek(0)
    posant = 0
       
    linea = arch.readline()
    
    elegido = False
    
    while linea and not elegido:
        
        venta = list(linea.strip().split(";"))
        
        if venta[0] == "0": 
            posant = arch.tell()
            linea = arch.readline()
        else:
            while True: 
                try:
                    print()
                    print(f"{'Fecha y Hora':<22}{'Sucursal':<20} {'Producto':<20} {'Importe'}")
                    print(f"{venta[1]:<21} {venta[2]:<20} {venta[3]:<20} {float(venta[4]):>8.2f}")
                    print()
                    print("1. Siguiente Linea")
                    print("2. Modificar")
                    print("3. Finalizar")
                    opcion = int(input("Ingrese opción => ")) 
                    assert opcion==1 or opcion==2 or opcion==3
                    break
                except (ValueError,AssertionError): 
                    print("\nIngreso invalido, el valor debe ser 1, 2 o 3")
                
            if opcion==1:
                posant = arch.tell()
                linea = arch.readline()
                
            if opcion==2:
                while True:
                    try:
                        print()
                        print("¿Qué campo desea modificar?")
                        print("1. Sucursal")
                        print("2. Producto")
                        print("3. Importe")
                        campo = int(input("\nIngrese opción => "))
                        assert campo==1 or campo==2 or campo==3
                        break
                    except (ValueError,AssertionError): 
                        print("\nIngreso invalido, el valor debe ser 1, 2 o 3")
                       
                                     
                print("\nCampo actual:",venta[campo+1])
                
                if campo==1:
                    modif = ingresar_datos("Ingrese la sucursal: ", validar_palabra).title()
                elif campo==2:
                    modif = ingresar_datos("Ingrese el producto: ", validar_palabra).title()
                elif campo==3:
                    modif = ingresar_datos("Ingrese el importe: ", validar_numero)
                
                venta[campo+1] = modif
                
                elegido = True
            
            if opcion==3:
                break
    
    else:
        if elegido:
            arch.seek(posant)
            arch.write(";".join(venta)+"\n")
            print("\nModificación exitosa")
            input("Presione una tecla para volver al Menú ")
                    
        else:
            print("\nNo hay mas registros")
            input("Presione una tecla para volver al Menú ")
    
    arch.close()
        
    

def listado_ventas():
    
    arch = open("Ventas.csv","r")
    
    long_max = ancho_columna_importe(arch)
    arch.seek(0)

    print(f"{'FECHA Y HORA':<22}{'SUCURSAL':<20} {'PRODUCTO':<20} {'IMPORTE ($)'}")
    
    for linea in arch:
        venta = list(linea.strip().split(";"))
        if venta[0] != "0":
            print(f"{venta[1]:<21} {venta[2]:<20} {venta[3]:<20} {float(venta[4]):>{long_max+2}.2f}")

    input("\nPresione una tecla para volver al Menú ")
    
    arch.close()

def listado_ventas_por_producto():
    ventas_por_producto = {}
    
    arch = open("Ventas.csv","r")
    
    for linea in arch:
        venta = list(linea.strip().split(";"))
        if venta[0] != "0":
            producto = venta[3]
            
            ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + 1

    productos_ordenados = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)
    
    print()
    print(f"{'PRODUCTO':<20} {'CANTIDAD':<15}")
    for producto, total_ventas in productos_ordenados:
        print(f"{producto:<20} {total_ventas:<15}")

    print("\nNo hay más registros")
    input("Presione una tecla para volver al Menú ")
    
    arch.close()


def listado_ventas_por_producto_ordenado_por_suma():
    ventas_por_producto = {}
    
    arch = open("Ventas.csv","r")
    long_max = ancho_columna_importe(arch)
    arch.seek(0)
        
    for linea in arch:
        venta = list(linea.strip().split(";"))
        if venta[0] != "0":
            producto = venta[3]
            importe = float(venta[4])

            ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + importe

    productos_ordenados = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)

    print()
    print(f"{'PRODUCTO':<20} {'INGRESOS':<15}")
    for producto, total_ventas in productos_ordenados:
        print(f"{producto:<20} {'$':>1}{total_ventas:>{long_max+2}.2f}")
                
    print("\nNo hay más registros")
    input("Presione una tecla para volver al Menú ")
                
    arch.close()


def menu():
    while True:
        print()
        print("Menú:")
        print("1. Alta de venta")
        print("2. Baja de venta")
        print("3. Modificación de venta")
        print("4. Listado de ventas")
        print("5. Listado de ventas por producto (ordenado por cantidad de ventas)")
        print("6. Listado de ventas por producto (ordenado por suma del valor de ventas)")
        print("7. Salir del programa")

        opcion = input("\nElija una opción: ")

        if opcion == "1":
            alta_venta()
        elif opcion == "2":
            baja_venta()
        elif opcion == "3":
            modificacion_venta()
        elif opcion == "4":
            listado_ventas()
        elif opcion == "5":
            listado_ventas_por_producto()
        elif opcion == "6":
            listado_ventas_por_producto_ordenado_por_suma()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

