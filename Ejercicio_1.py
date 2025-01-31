#Ejercicio 1. Función contar_caracteres.
#Descripción del ejercicio:Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
  contar=0
  for caracter in cadena:
    if caracter != " ":
     contar += 1
  return contar
cadena = "Hola Mundo"  
print(f"El número de caracteres de la cadena de texto dada: {(cadena)} es igual a {contar_caracteres(cadena)}")  

#Ejercicio 2. Función calcular_promedio :
#Descripción del ejercicio:Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(Lista_numeros):
  sumar=0
  for numero in Lista_numeros:
    sumar += numero
  return sumar/len(Lista_numeros)
Lista_numeros = (5,2,2)  
print(f"El promedio de la lista de número: {(Lista_numeros)} es  igual a {calcular_promedio(Lista_numeros)}")  

#Ejercicio 3. Función encontrar_duplicado :
#Descripción del ejercicio:Crea una función que busque y devuelva el primer elemento duplicado en una lista dada:
def encontrar_duplicado(lista):
  comprobados = set()
  for elemento in lista:
    if elemento in comprobados:
        return elemento
    else:
      comprobados.add(elemento)
  return None    
lista = (5,2,1,2,3,4)  
print(f"El primmer elemento duplicado en la lista dada: {(lista)} es  igual a {encontrar_duplicado(lista)}")  

#Ejercicio 4. Función enmascarado_datos :
#Descripción del ejercicio: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
def enmascarado_datos(variable):
  #Converti la cadena en cadena de texto
  cadena=str(variable)
  #si la variable de la cadena es meno o igual a 4, no enmascarar nada
  if len(cadena) <=4:
    return cadena
  #Enmascara todos los carateres expeto los ultimos 4 ( me debo de situar en el indice "-4" desde la derecha y hasta el final ":")
  enmascarada= "#" * (len(cadena)-4) + cadena[-4:]
  return enmascarada
variable= 1247592
print(f"Enmascar la variable {(variable)} excpeto los utlimmos cuaro caracteres {enmascarado_datos(variable)}")  

#Ejercicio 5. Función es_anagrama
#Descripción del ejercicio: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def es_anagrama(palabra1, palabra2):
#convertir las palabras a minúscula para hacer la comparación
  palabra1 = palabra1.lower()
  palabra2 = palabra2.lower()
#Ordenar las letras de ambas palabras
  palabra1_ordenada =sorted(palabra1)
  palabra2_ordenada = sorted(palabra2)
  if palabra1_ordenada == palabra2_ordenada:
       print("son anagramas")
  else:
      print("No son anagramas")  
palabra1= "casa"
palabra2 = "saca"
es_anagrama(palabra1, palabra2)

#Ejercicio 6. Función buscar_nombre.
#Descripción del ejercicio:Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
  #Solicitar al usuario ingresar una lista de nombres
  lista_nombres = input("Ingrese una lista de nombres separados por comas: ")
  #Solicita al usuario ingresa un nombre para buscar en la lista.
  nombre_a_buscar= input("Ingrese el nombre que desea buscar de las lista: ")
  if nombre_a_buscar in lista_nombres:
      print(f"El nombre {nombre_a_buscar} fue encontrado en la lista")
  else:
      raise ValueError(f"El nombre {nombre_a_buscar} no fue encontrado en la lista")
#llamar a la función.
buscar_nombre()
#Ejercicio 7.Función fibonacci :
#Descripción del ejercicio:Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión.
def fibonacci(n):
   if n<= 0:
      raise ValueError("El término n debe ser un número positivo")
   if n==1:
      return 0
   if n==2:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
#Ejemplo
termino_n =int(input("Ingrese el término n de la serie de Fibonacci que desea calcular: "))   
resultado= fibonacci(termino_n)
print(F"El ténino {termino_n} de la serie de Fibonacci es: {resultado}")

#Ejercicio 8. Función encontrar_puesto_empleado :
#Descripción del ejercicio: Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def encontrar_puesto_empleado(nombre_completo, lista_empleados):
   for empleado in lista_empleados:
       nombre_completo_empleado = f"{empleado["nombre"]} {empleado["apellido"]}" 
       if nombre_completo_empleado == nombre_completo:
          return f"{nombre_completo_empleado} trabaja aqui con el puesto de {empleado["puesto"]}"
       else:
          return f"{nombre_completo_empleado} no trabaja aqui"
#Lista de empleados facilitada       
empleados = [
   {"nombre":"Juan","apellido": "García", "puesto":"Secretario"},
   {"nombre":"Mabel","apellido": "García", "puesto":"Product Manager"},
   {"nombre":"Isabel","apellido": "Martin", "puesto":"CEO"}
]
#Solicitar al usuario ingresar un nombre completo
nombre_a_buscar = input("Ingrese un nombre completo del empleado que desea buscar: ")
#LLamar a la funcion y mostar el resultado
resultado = encontrar_puesto_empleado(nombre_a_buscar, empleados)
print(resultado)

#Ejercicio 9 Función cubo_numero usando lambdas:
#Descripción del ejercicio: Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo=lambda x: x** 3
#Solicitar al usuario ingresar un numero
numero = int(input("Ingrese un número sobre el que quieres obtener el cubo: "))
resultado= cubo(numero)
print(f" El cubo de {numero} es {resultado}")

#Ejercicio 10: Función resto_division usando lambdas:
#Descripción del ejercicio:Crea una función lambda que calcule el resto de la división entre dos números dados.
# Definir la función lambda para calcular el resto de la división
resto_division = lambda x, y: x % y
# Solicitar al usuario ingresar dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
# Calcular el resto de la división usando la función lambda
resultado = resto_division(numero1, numero2)
# Mostrar el resultado
print(f"El resto de dividir {numero1} entre {numero2} es {resultado}.")

#Ejercicio 11: Función numeros_pares usando lambdas y filter :
#Descripción del ejercicio: Crea una función lambda que filtre los números pares de una lista dada.
def numeros_pares(lista_numeros):
   return list(filter(lambda x:x % 2==0,lista_numeros))
lista_numeros = [24,56, 2.3,19,-1,0]
print(f"los numeros pares de la lista dada son: {numeros_pares(lista_numeros)}")

#Ejercicio 12: Función numeros_suma usando lambdas y map :
#Descripción del ejercicio: Crea una función lambda que sume 3 a cada número de una lista dada.
def numeros_suma(lista_numeros):
   return list(map(lambda x:x +3,lista_numeros))
lista_numeros = [24,56, 2.3,19,-1,0]
print(f"de la lista {lista_numeros} el resultado sería {numeros_suma(lista_numeros)}")

#Ejercicio 13: Función sumar_listas usando lambdas:
#Descripción del ejercicio:  Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def sumar_listas(lista_numeros_1,lista_numeros_2):
    max_length = max(len(lista_numeros_1), len(lista_numeros_2))
    lista_numeros_1.extend([0] * (max_length - len(lista_numeros_1)))
    lista_numeros_2.extend([0] * (max_length - len(lista_numeros_2))) 
    return list(map(lambda x, y: x + y, lista_numeros_1,lista_numeros_2))
lista_numeros_1= [1, 4, 5, 6 , 7 , 7] 
lista_numeros_2 = [3, 11, 34, 56]
print(sumar_listas(lista_numeros_1,lista_numeros_2))
#Ejercicio 14:No te vayas por las ramas :
#Descripción del ejercicio: Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida")

    def info_arbol(self):
        info = f"Longitud del tronco: {self.tronco}\n"
        info += f"Número de ramas: {len(self.ramas)}\n"
        info += f"Longitudes de las ramas: {self.ramas}"
        return info

# Caso de uso
mi_arbol = Arbol()       # 1. Crear un árbol
mi_arbol.crecer_tronco() # 2. Hacer crecer el tronco del árbol una unidad
mi_arbol.nueva_rama()    # 3. Añadir una nueva rama al árbol
mi_arbol.crecer_ramas()  # 4. Hacer crecer todas las ramas del árbol una unidad
mi_arbol.nueva_rama()    # 5. Añadir dos nuevas ramas al árbol
mi_arbol.nueva_rama()    # Añadir la segunda nueva rama
mi_arbol.quitar_rama(2)  # 6. Retirar la rama situada en la posición 2
print(mi_arbol.info_arbol()) # 7. Obtener información sobre el árbol

#Ejercicio 15: Clase UsuarioBanco :
#Descripción del ejercicio: Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        otro_usuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
# Caso de uso
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
# Agregar 20 unidades de saldo a "Alicia"
alicia.agregar_dinero(20)
print(f"Saldo de Alicia después de agregar 20 unidades: {alicia.saldo}")
# Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"
try:
    bob.transferir_dinero(alicia, 80)
    print(f"Saldo de Bob después de la transferencia: {bob.saldo}")
    print(f"Saldo de Alicia después de recibir la transferencia: {alicia.saldo}")
except ValueError as e:
    print(e)
# Retirar 50 unidades de saldo de "Alicia"
try:
    alicia.retirar_dinero(50)
    print(f"Saldo de Alicia después de retirar 50 unidades: {alicia.saldo}")
except ValueError as e:
    print(e)

#Ejercicio 16:
#Descripción del ejercicio:Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función rocesar_texto .
def contar_palabras(texto):
    contador = {}
    for palabra in texto.split():
        if palabra in contador:
           contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    if palabra_original in texto.split():
     return texto.replace(palabra_original, palabra_nueva) 

def eliminar_palabra(texto, palabra_a_eliminar):
    if palabra_a_eliminar in texto.split():
        texto = texto.replace(palabra_a_eliminar, "")
    return texto   

def procesar_texto(texto, opcion, *args):
    texto = texto.lower()
    caracteres_especiales = ['.']
    for caracter in caracteres_especiales:
        texto = texto.replace(caracter, '')
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == "eliminar":
          palabra_a_eliminar = args[0]
          return eliminar_palabra(texto, palabra_a_eliminar)
    else:
        return "Opción no válida"

# Caso de uso
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
resultado_contar = procesar_texto(texto, "contar")
resultado_reemplazar = procesar_texto(texto, "reemplazar", "texto", "relato")
resultado_eliminar = procesar_texto(texto, "eliminar", "ejemplo")

print("Contar palabras:", resultado_contar)
print("Reemplazar palabras:", resultado_reemplazar)
print("Eliminar palabra:", resultado_eliminar)
