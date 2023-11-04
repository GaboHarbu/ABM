import csv
import datetime

def generar_archivo():
    try:
        with open("Ventas.csv", "r") as file:
            pass
        
    except FileNotFoundError:
        with open("Ventas.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Fecha y Hora", "Sucursal", "Producto", "Importe"])

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
    date_time = datetime.datetime.now()
    date_time_str = date_time.strftime("%Y-%m-%d %H:%M:%S")

    sucursal = ingresar_datos("Ingrese la sucursal: ", validar_palabra)
    producto = ingresar_datos("Ingrese el producto: ", validar_palabra)
    
    importe = ingresar_datos("Ingrese el importe: ", validar_numero)

    nueva_venta = [date_time_str, sucursal, producto, float(importe)]

    with open("Ventas.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(nueva_venta)

    print("Venta agregada con éxito.")
    print()

def baja_venta():
    pass

def modificacion_venta():
    pass

def listado_ventas():
    pass

def listado_ventas_por_producto():
    pass

def listado_ventas_por_producto_ordenado_por_suma():
    pass

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