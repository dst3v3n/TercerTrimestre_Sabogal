import csv

class Pais:
    def __init__(self,Nombre:str,Altura:int,Pib:int , Nominal:int):
        self.__nombre = Nombre
        self.__altura = Altura
        self.__pib = Pib
        self.__nominal = Nominal
        self.__caracter = 0
        self.__promedio = 0
    
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
        lista = []

        with open(file , encoding="utf-8" ) as file_csv:
            csv_read = csv.reader(file_csv)

            for row in csv_read:
                indices = row [indice]
                lista.append (indices)
                for i in indices:
                    caracter += 1
                    
        
        self.__caracter = caracter
        with open("manipulacion_archivos/pruebas/caracters.txt" ,"a") as new_file:
            new_file.write (f"La columna del indice {lista[0]} tiene {caracter} caracteres\n")
        print(f"El indice {lista[0]} tiene {caracter} caracteres")

    def Promedio (self,file:str):
        try:
            x = int(input("Digita la columna que quieres hayar el promedio: "))

            suma1 = 0
            lista = []
            listax = []
            listmodify = []
            numero = ""

            with open (file , encoding="utf-8") as file_csv:

                read_csv = csv.reader(file_csv)
                for row in read_csv:
                    if not(row[x] == ""):
                        lista.append(row[x])
                y = lista.pop(0)
                
                for i in lista:
                    for h in i:
                        if h != ",":
                            listax.append (h)
                        elif h == ",":
                            listax.append (".")
                    for i in listax:
                        numero = str(numero) + str(i)
                    listmodify.append(numero)
                    numero = ""
                    listax = []
                # for i in lista:
                #     n = i.replace("," , ".") 
                #     suma += float(n)

             
                for i in listmodify:
                    suma1 += float(i)

            division1 = suma1 / len(lista)   
            # division = suma / len(lista)
            self.__promedio = division1

            with open("manipulacion_archivos/pruebas/promedio.txt" ,"a") as new_file:
                new_file.write (f"El promedio del indice {y} es de: {division1}\n")
                                
            # print (f"El promedio del indice {y} es de: {division} lista modificada")
            print (f"El promedio del indice {y} es de: {division1}")

        except ValueError:
            print("No se puede sacar el promedio con valores de tipo string (cadena)")