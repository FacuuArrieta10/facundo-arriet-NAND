

def nand_gate(numeros_binarios):
    resultado = 1 
    """
    Es necesario que la variable donde se hara la primera comparación inice en 1, ya que si inicia en 0 dara siempre False.
    Al desconocer la cantidad de variables que se van a ingresar..
    Se utiliza un for para que vaya una a una anilzandose a través de la compuerta AND

    """
    for valor in numeros_binarios:
        resultado = resultado and valor
         #*Una vez que se tiene el resultado se niega a través de la compuerta "not"
        #*El int es importante para que el resultado final sea un binario y no un boleano.
    return int(not resultado)

#Creamos una lista a través de numeros_binarios = []
#La lista guardara los valores binarios que ingrese el usuario.

numeros_binarios = []

#Usamos un while para pedir al usuario que ingrese números:

entrada= ""

#Inicializamos entrada en ""  para que pueda ingresar cualquier string.

while entrada.upper() != "X":
#Mientras que la entrada no sea x o X, el programa pedira números binarios(Aprovechamos upper, para que conviernta el string en mayusculas).
    entrada = input("Ingrese un número binario: (0 o 1), si desea salir ingrese (X): ")
    #el operador IN, sirve para "buscar variables dentro de una lista, le estamos dando como lista. ["0","1"]
    #Si in encuentra que el usuario ingreso 1 o 0 guarda la variable.
    if entrada in ["0", "1"]:
    #Con numeros.binarios.append guardamos en la lista el string ingresado por el usuario.
         numeros_binarios.append(int(entrada))
    elif entrada.upper() != "X":
        print("Por favor ingrese un número binario válido (0 o 1).")
        

print(numeros_binarios)
resultado = nand_gate(numeros_binarios)
print(f"El resultado de la compuerta NAND es: {resultado}")

    

#*Apuntes propios para comprender mejor el funcionamiento:

#Analiza los númerios binarios y resulevo si es true o false
#La compuerta lógica NAND, niega el resultado de AND
#Not sirve para negar
#AND evalua si las entradas son 1, si alguna no es 1 dara resultado false, y NAND, negara este resultado dando True
#Solo sera false si todos son 1 ya que AND dara true y NAND, negara esto.