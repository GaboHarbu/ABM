import csv
import datetime

def generar_archivo():
    try:
        with open("Ventas.csv", "r") as file:
            pass
        
    except FileNotFoundError:
        with open("Ventas.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Estado", "Fecha y Hora", "Sucursal", "Producto", "Importe"]) # Mili, le agregue el estado, sino no se deberia mostrar este campo en el listado

def validar_numero(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        return False

def validar_palabra(entrada):
    return entrada.strip() != ""

def ingresar_datos(mensaje, validador):
    while True:
        entrada = input(mensaje)
        if validador(entrada):
            return entrada
        else:
            print("Entrada no válida. Intente de nuevo.")

def alta_venta():

    estado_logico = 1 # (tomi) le agregue el estado para hacer borrado logico
    
    date_time = datetime.datetime.now()
    date_time_str = date_time.strftime("%Y-%m-%d %H:%M:%S")

    sucursal = ingresar_datos("Ingrese la sucursal: ", validar_palabra)
    producto = ingresar_datos("Ingrese el producto: ", validar_palabra)
    
    importe = ingresar_datos("Ingrese el importe: ", validar_numero)

    nueva_venta = [estado_logico, date_time_str, sucursal, producto, float(importe)]

    with open("Ventas.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(nueva_venta)

    print("Venta agregada con éxito.")
    print()

def baja_venta():
    print("\n\033[1mBorrado\033[0m")
    with open("Ventas.csv", mode="r+", newline="") as arch:
        arch.seek(0)
        posant = 0
        linea = arch.readline()
        Borrado = False
        while linea and not Borrado:
            
            venta = list(linea.strip().split(","))
            
            if venta[0] == "0": #Si quieren cambiar esto avisenme y vemos de borrar el archivo y generar uno nuevo pero estaria bueno agregar una funcion de recuperar borrados
                posant = arch.tell()
                linea = arch.readline()
            else:
                while True: 
                    try:
                        print("\n",linea)
                        print("1. \033[1mSiguiente Linea\033[0m")
                        print("2. \033[1mBorrar\033[0m")
                        n = int(input("Ingrese opción => ")) 
                        assert n==1 or n==2 
                        break
                    except ValueError: 
                        print("\nIngreso invalido, el valor debe ser 1 o 2")
                    except AssertionError:
                        print("\nIngreso invalido, el valor debe ser 1 o 2")
                    
                if n==1:
                    posant = arch.tell()
                    linea = arch.readline()
                if n==2:
                    modif = 0
                    venta[0] = modif
                    Borrado = True
        if Borrado:
            arch.seek(posant)
            writer = csv.writer(arch)
            writer.writerow(venta)
            print("\nBorrado exitoso")
            print()        
        else:
            print("\nNo hay mas registros")
            print()

def modificacion_venta():
    print("\n\033[1mModificaciones\033[0m")
    with open("Ventas.csv", mode="r+", newline="") as arch:
    
        campos_modificables = ["sucursal","producto","importe"]         
        
        arch.seek(0)
        posant = 0
           
        linea = arch.readline()
        
        elegido = False
        
        while linea and not elegido:
            
            venta = list(linea.strip().split(","))
            
            if venta[0] == "0": #si el estado es 0, esta borrado logicamente y no deberia mostrarse
                posant = arch.tell()
                linea = arch.readline()
            else:
                while True: 
                    try:
                        print("\n",linea)
                        print("1. \033[1mSiguiente Linea\033[0m")
                        print("2. \033[1mModificar\033[0m")
                        n = int(input("Ingrese opción => ")) 
                        assert n==1 or n==2 
                        break
                    except ValueError: #se pueder evitar con n siendo str y simplemente validar que no sea "1" o "2"
                        print("\nIngreso invalido, el valor debe ser 1 o 2")
                    except AssertionError:
                        print("\nIngreso invalido, el valor debe ser 1 o 2")
                    
                if n==1:
                    posant = arch.tell()
                    linea = arch.readline()
                    
                if n==2:
                    campo = input("\n¿Qué campo desea modificar? ").lower() # tambien se podria hacer como un menu
                    while campo not in campos_modificables:
                        print("\nCampo invalido, los campos modificables son:",end =' ')
                        print(*(campos_modificables),sep=', ')
                        campo = input("¿Qué campo desea modificar? ")
                        
                    indice_campo = campos_modificables.index(campo) + 2 #existen estado_logico y datetime pero no se modifican
                    
                    print("\nCampo actual:",venta[indice_campo])
                    
                    if campo == "sucursal":
                        modif = ingresar_datos("Ingrese la sucursal: ", validar_palabra)
                    elif campo == "producto":
                        modif = ingresar_datos("Ingrese el producto: ", validar_palabra)
                    elif campo =="importe":
                        modif = float(ingresar_datos("Ingrese el importe: ", validar_numero))
                    
                    venta[indice_campo] = modif
                    
                    elegido = True
        
        if elegido:
            arch.seek(posant)
            writer = csv.writer(arch)
            writer.writerow(venta)
            print("\nModificación exitosa")
            input("Presione una tecla para volver al Menú ")
                    
        else:
            print("\nNo hay mas registros")
            input("Presione una tecla para volver al Menú ")

def listado_ventas():
    with open("Ventas.csv", mode="r+", newline="") as arch:
        arch.seek(0)
        ventas = []  # Lista para almacenar las ventas y luego ordenarlas en orden desc
        for linea in arch:
            venta = list(linea.strip().split(","))
            if venta[0] != "0":
                ventas.append(linea.strip())
        # Ordenar las ventas por la columna de fecha en orden descendente - la ultima primero
        ventas_ordenadas = sorted(ventas, key=lambda x: x.split(",")[1], reverse=True)  #con fecha en pos 1, porque la pos 0 es el estado
        for venta in ventas_ordenadas:
            print(venta)

        print("\nNo hay más registros")
        input("Presione enter para volver al Menú ")

def listado_ventas_por_producto():
    pass

def listado_ventas_por_producto_ordenado_por_suma():
    ventas_por_producto = {}  # Dictionary to store total sales for each product

    with open("Ventas.csv", mode="r", newline="") as arch:
        arch.seek(0)

        # Skip the header line
        next(arch)

        for linea in arch:
            venta = list(linea.strip().split(","))
            if venta[0] != "0":
                producto = venta[3]
                importe = float(venta[4])

                # Update the total sales for the product in the dictionary
                ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + importe

    # Order products by total sales in descending order
    productos_ordenados = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)

    # Print the result
    print("{:<20} {:<15}".format("Producto", "Total de Ventas"))
    for producto, total_ventas in productos_ordenados:
        print("{:<20} ${:<15,.2f}".format(producto, total_ventas))

    print("\nNo hay más registros")
    input("Presione enter para volver al Menú ")


def main():
    generar_archivo()

    while True:
        print("Menú:")
        print("1. \033[1mAlta de venta\033[0m")
        print("2. \033[1mBaja de venta\033[0m")
        print("3. \033[1mModificación de venta\033[0m")
        print("4. \033[1mListado de ventas\033[0m")
        print("5. \033[1mListado de ventas por producto\033[0m (ordenado por cantidad de ventas)")
        print("6. \033[1mListado de ventas por producto\033[0m (ordenado por suma del valor de ventas)")
        print("7. \033[1mSalir del programa\033[0m")

        opcion = input("Elija una opción: ")

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

if __name__ == "__main__":
    main()
