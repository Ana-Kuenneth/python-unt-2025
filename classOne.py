
"comentario de linea"
#comentario en linea

"""
DOC STRING
block de comentarios
wuju
guau
"""

"Imprimir un mensaje en consola. No es necesario poner punto y coma"
print("hola mundo")


"CTRL + L   en la terminar es el clear para limpiar la terminal"

"Hacer variables"
"hacer variables de tipo String"
mensaje = "hola" 
"hacer variables de tipo int"
entero = 2
"hacer variables de tipo float"
real = 12.3
    
"Imprimir variables"
print(mensaje)
print(entero)
print(real)

"concatenacion error"
# print(mensaje + entero)

#correcta transformación de un numero a un string
print(mensaje + str(entero))


#OPCION PARA ESCRIBIR MUCHO TEXTO
texto={
       "mucho texto"
"mucho texto"
"mucho texto"
"mucho texto"
"mucho texto"
"mucho texto"
"mucho texto"
"mucho texto mucho texto mucho texto mucho texto mucho texto mucho texto"
       }
print(texto)

#imprimir muchas variables
print(mensaje, entero, real)

#BOOLEANOS
esta_lloviendo = True
estas_feliz=False

print(esta_lloviendo)
print(estas_feliz)

#Numeros complejos
num = 5 + 1j
print(num)

#separar y buscar strings
saludo="Hola Juan, como estas?"
print(saludo[5:9])
print(saludo[5:])
print(saludo[:5])
#terminador nulo?
print(saludo[-1])
print(saludo[-22])
print(saludo[0])

#
print(f"El resultado es {entero}")
elemento= "jarron"
print(f"El resultado es {elemento[:2]}"f"{elemento[2:]}")
print(f"El resultado es {elemento[:2]}{elemento[2:]}")

print("El resultado es\nUNO")