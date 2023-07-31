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

contar_lines("Aprendiendo.txt")
contar_caracteres("Aprendiendo.txt")