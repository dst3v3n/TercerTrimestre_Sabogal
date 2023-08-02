from os import strerror #Se importa un modulo

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)} #Se crea un diccionario mediando comprension
file_name = input("Ingresa el nombre del archivo a analizar: ") #Se pido al usuario que digite el nombre del archivo para analizar
counters.update({"!":0,
                 ".":0,
                 ",": 0})
try:
    file = open(file_name, "rt") #Se abre el archivo que quiere analizar
    for line in file: #Empieza a pasar por cada linea
        for char in line: # Empieza a pasar por cada indice
            # Si es una letra...
            if char.isalpha():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1 #El diccionario el keys se va a volver en minuscula y aumentara el contador
    file.close() # Se cierra el archivo
    # Demos salida a los contadores.
    for char in counters.keys(): # Para cada letra en el diccionario va a usar un metodo que se encarga de solo usar los keys de ese diccionario
        c = counters[char] #Se va a guardar en la variable los numeros del valor del diccionario
        if c > 0: #Si c es mayor a 0
            print(char, '->', c) # Va a imprimir el mensaje
except IOError as e: #Exception
    print("Se produjo un error de E/S: ", strerror(e.errno)) #Va a imprimir el mensaje si ocurre esa exception