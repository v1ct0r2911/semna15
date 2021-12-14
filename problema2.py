nombre=input("Ingrese su nombre: ")
nota_1=int(input("Ingrese la nota 1: "))
nota_2=int(input("Ingrese la nota 2: "))

promedio=(nota_1 + nota_2)/2

aprobado=False

if promedio >= 13:
    aprobado=True

file=open("notas.txt", "w")
file.write("nombre: " + nombre + "\n")
file.write("nota 1 : " + str(nota_1) + "\n")
file.write("nota 2 : " + str(nota_2) + "\n")
file.write("promedio :" + str(promedio) + "\n")
file.write("aprobado :" + str(aprobado) + "\n")


file.close()