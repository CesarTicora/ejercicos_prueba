print ("Hola Mundo")

mensaje = "Holas mundo"
print(mensaje)

nombre = input("Ingrese el nombre: \n")
print("Hola " + nombre)

#Operacon matematica
operacion = (((3+2) / (2*5))**2)
resultado = operacion * operacion
print(resultado)

#Cantidad de horas
horas = float(input("Ingrese la cantidad de horas \n"))
valor = float(input("Ingrese la cantidad de el valor de la hora \n"))
resultado = horas * valor
print ("el valor de la cantidad e horas es \n", resultado)

#Ingresar entero positivo

n = int(input("Ingrese el valor a operar: \n"))
suma = (n*(n+1))/2
print (f"La suma de los numeros es {suma}")

#Indice de masa corporal
peso = float(input("Ingrese su peso \n"))
estatura = float(input("Ingrese su estatura: \n"))
imc =  peso / (estatura * estatura)
print (f"El inidce de masa corporal es {imc}")

#Valor a invertir, interes anual y el numero de años y muestre en pantalla el capital obtenido 
#En la inversión
valorInvertir = float(input("Ingrese cuanto deses invertir: \n"))
interesAnual = float(input("Ingrese su interes anual: \n")) / 100
numeroAnos = float(input("Ingrese el numero de años a invertir: \n"))
gananciasTotales = valorInvertir * (1 + interesAnual * numeroAnos)

print("Ganancias Totales {}".format(gananciasTotales))