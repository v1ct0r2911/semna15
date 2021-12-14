from datetime import datetime 
ahora = datetime.now()
fecha = ahora.strftime("%d/%m/%Y")
archivo= open ("registro.txt" , "a")
TOTAL = 0 


def obtenerIGV(a):
    igv = a * 0.18
    return igv
def obtenerIGVTotal(a):
    subTotal = a * 1.18
    return subTotal
def obtenerTotal(a,b):
    total = a+b
    return total
print("-----------------VENTAS------------------: ")
print("*"*50)

a = int(input("Ingresa la cantidad de productos a adquirir: "))
for x in range (0,a):
    producto = str(input("Ingresa el producto: "))
    precio = str(input("Ingresa el precio: "))
    cantidad = str(input("Ingresa la cantidad: "))
    archivo.write(cantidad+ "\t" + producto + "\t" + precio + "\n")
    TOTAL = TOTAL + obtenerTotal(int(precio), int(cantidad))


archivo.write("Fecha: " + str(fecha) + "\n")
archivo.write("SubTotal: " + str(TOTAL) + "\n")
archivo.write("IGV: " + str(obtenerIGV(TOTAL)) + "\n")
archivo.write("Total costo: " + str(obtenerIGVTotal(TOTAL)) + "\n")
archivo.close()