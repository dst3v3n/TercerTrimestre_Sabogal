import csv

class Pais:
    def __init__(self,Nombre:str,Altura:int,Pib:int , Nominal:int):
        self.__nombre = Nombre
        self.__altura = Altura
        self.__pib = Pib
        self.__nominal = Nominal
        self.__caracter = 0
    
    def getNombre (self):
        return self.__nombre

    def getAltura (self):
        return self.__altura
    
    def getPib (self):
        return self.__pib
    
    def getNominal (self):
        return self.__nominal
        
    def caracter (self , file:str, indice:int):
        caracter = 0

        with open(file , encoding="utf-8" ) as file_csv:
            csv_read = csv.reader(file_csv)

            for row in csv_read:
                indices = row [indice]
                for  i in indices:
                    caracter += 1
        
        self.__caracter = caracter
        with open("manipulacion_archivos/pruebas/caracters.txt" ,"a") as new_file:
            new_file.write (f"La columna del indice {indice} tiene {caracter} caracteres\n")
        print(f"El indice {indice} tiene {caracter} caracteres")

    def Promedio (self,file:str):
        x = int(input("Digita la columna que quieres hayar el promedio: "))

        multiplication = 0
        division = 0
        lista = []
        lista_modify = []

        with open (file , encoding="utf-8") as file_csv:

            read_csv = csv.reader(file_csv)
            if x == 10 :
                for row in read_csv:
                    lista.append(row[x])
                lista.pop(0)
                lista.pop(0)
            else:
                lista.pop(0)
                for row in read_csv:
                    lista.append(row)   

            for i in lista:
                print(i)
                q = i.replace("," , ".")
                y = float(q)
                lista_modify.append(y)
        print(lista_modify)
            

        print(len(lista_modify))
        print(multiplication)
        division = multiplication / len(lista_modify)
        print(division)