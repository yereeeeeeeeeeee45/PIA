import math
SEPARADOR = ("*" * 20) + "\n"
'''

Ejemplo para ilustrar la importaqncia de la libreria math en Python 3
Demuestra el uso de: floor(x),trunc(x),ceil(x),round(x),factorial(x).pow(x,y),sqrt(x) y pi
'''


valorflotante = float(input("Introduce un valor con fraccion decimal:\n"))
print(f"El siguiente entero hacia arriba de {valorflotante} es {math.ceil(valorflotante)}")
print(SEPARADOR)
print(f"El siguiente entero hacia abajo de {valorflotante} es {math.floor(valorflotante)}")
print(SEPARADOR)
print(f"La parte entera truncada de {valorflotante} es {math.trunc(valorflotante)}") #Equivalente flour) para positivos, y a cell())
print(SEPARADOR * 2)
pass


valorNumerico = int(input("Dame un valor entero: \n"))
print(f"La raiza cuadrada de {valorNumerico} es igual a {math.sqrt(valorNumerico)}")
print(SEPARADOR)
print(f"El factorial de {valorNumerico} es igual a {math.factorial (valorNumerico)}")
potencia = int(input("Dame un valor entero: \n")) 
print(f"Elresultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico, potencia)}")
print(SEPARADOR * 2)
pass


print("El valor de Pi es {math.pl}")