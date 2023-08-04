from Pais import *
import csv

listaPais = []


with open("C:\\Users\\PERSONAL\\Downloads\\pais.csv" , encoding="utf-8") as file_csv:
# with open("C:\\Users\\SENA\\Downloads\\pais.csv" , encoding="utf-8") as file_csv:
    csv_reader = csv.reader(file_csv)
    for row in csv_reader:
        ob = Pais(row[1], row[7],row[10] , row [11])
        listaPais.append(ob)

for apr in listaPais:
    print(f"Nombre del pais: {apr.getNombre()}")
    print(f"Altura del pais: {apr.getAltura()}")
    print(f"Pib del pais:  {apr.getPib()}")
    print(f"Nominal del pais: {apr.getNominal()}\n")

x = int(input("Digita el indice: "))
ob.caracter ("C:\\Users\\PERSONAL\\Downloads\\pais.csv" , x)
# ob.caracter ("C:\\Users\\SENA\\Downloads\\pais.csv" , x)
ob.Promedio("C:\\Users\\PERSONAL\\Downloads\\pais.csv")
# ob.Promedio("C:\\Users\\SENA\\Downloads\\pais.csv")

