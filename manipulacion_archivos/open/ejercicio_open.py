import os

file_txt = open("manipulacion_archivos/pruebas/aprendiendo_open.txt", "w+")

file_txt.write("Hola, mi nombre es Harold Steven Sabogal Perez\n"
               "Mi numero de celular es: 3143442062\n"
               "Mi correo electronico es: haroldsabogal48@gmail.com\n"
                "Estudio en el Sena el programada de Analisis y Desarrollo de Software")

file_txt.close()

def contar_lines(file):
    count = 0
    read_txt = open(file,"r")
    for i in read_txt.readlines():
        count += 1
    if count == 1:
        print(f"El archivo tiene {count} linea")
    elif count>1:
        print(f"El archivo tiene {count} lineas")
    else:
        print("No tiene lineas")
    read_txt.close()

def contar_caracteres(file):
    count = 0
    read_txt = open(file,"r")
    for i in read_txt.read():
        count += 1
    if count == 1:
        print(f"El archivo tiene {count} caracter")
    elif count>1:
        print(f"El archivo tiene {count} caracteres")
    else:
        print("No tiene caracteres  ")
    read_txt.close()

contar_lines("manipulacion_archivos/pruebas/aprendiendo_open.txt")
contar_caracteres("manipulacion_archivos/pruebas/aprendiendo_open.txt")

# os.remove("manipulacion_archivos/pruebas/aprendiendo_open.txt")