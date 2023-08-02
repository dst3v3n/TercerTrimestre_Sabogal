import csv
import os

# columns = ["Nombre","Numero celular" , "Correo Electronico" , "Estudios"]

with open ("manipulacion_archivos/pruebas/aprendiendo_csv.csv" , "w+") as file_csv:
    ### Primera Forma ###
    csv_write = csv.writer(file_csv)
    csv_write.writerow(["Nombre","Numero celular" , "Correo Electronico" , "Estudios"])
    csv_write.writerow(["Harold Steven Sabogal Perez" ,"3143442062" , "haroldsabogal48@gmail.com" , "ADSO"])

    ### Segundo Forma ###
    # writer = csv.DictWriter(file_csv, delimiter=',', fieldnames=columns )
    # writer.writeheader()
    

with open ("manipulacion_archivos/pruebas/aprendiendo_csv.csv") as read_csv:
    csv_read = csv.DictReader(read_csv)
    for reader in csv_read:
        print(reader)
		# print(reader["Nombre"])