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
        
        
        
contar_lines("hola.txt")
contar_caracter("hola.txt")