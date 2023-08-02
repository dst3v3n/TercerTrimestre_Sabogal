import os
with open ("manipulacion_archivos/pruebas/aprendiendo_with_open.txt" , "w+") as file_text:
    escritura = file_text.write("Hola, mi nombre es Harold Steven Sabogal Perez\n"
               "Mi numero de celular es: 3143442062\n"
               "Mi correo electronico es: haroldsabogal48@gmail.com\n"
                "Estudio en el Sena el programada de Analisis y Desarrollo de Software")

def contar_lines(file):
    with open(file,"r") as read_text:
        countL = 0

        lines = read_text.readlines()
        for i in lines:
            countL += 1
        if countL == 1:
            print(f"El archivo tiene {countL} linea")
        elif countL>1:
            print(f"El archivo tiene {countL} lineas")
        else:
            print("No tiene lineas")

def contar_caracter(file):
    with open(file,"r") as read_text:
        countL = 0

        caracter = read_text.read()

        for f in caracter:
                countL += 1

        if countL == 1:
            print(f"El archivo tiene {countL} caracter")
        elif countL>1:
            print(f"El archivo tiene {countL} caracteres")
        else:
            print("No tiene caracter")
        
        
        
contar_lines("manipulacion_archivos/pruebas/aprendiendo_with_open.txt")
contar_caracter("manipulacion_archivos/pruebas/aprendiendo_with_open.txt")

# os.remove("manipulacion_archivos/pruebas/aprendiendo_with_open.txt")