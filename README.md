# TercerTrimestre_Sabogal

[![Python](https://img.shields.io/badge/Python-1.11.3+-00B894?style=for-the-badge&logo=python&logoColor=00B894&labelColor=black)](https://www.mysql.com/)
[![DataBase](https://img.shields.io/badge/MySQL-1.11.3+-00B894?style=for-the-badge&logo=MySQL&logoColor=00B894&labelColor=black)](https://www.python.org/)
[![Visual-Studio-Code](https://img.shields.io/badge/visual_studio_code-1.78+-00B894?style=for-the-badge&logo=visual-studio-code&logoColor=00B894&labelColor=black)](https://code.visualstudio.com/)

## Aprendiendo los fundamentos de Python

### El proyecto lo estoy realizando en el SENA. Estoy estudiando un tecnologo en Analisis y Desarrollo de Software (ADSO) :green_heart:
<br>

--------

>Contenido de los ejercicios con la documentación del proyecto

* [Excepciones](./excepciones/ejercicioexp1.py)
* [Manipulación Archivos](./manipulacion_archivos)
* [DataBases](./DataBase)
  
<br>
<br>
<br>

--------
## **Ultimos codigos realizados** :green_heart:

>Conexión con la base de datos

```python
import mysql.connector

database = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "ecommerce_harold_sabogal"
)

cursor = database.cursor ()

cursor.execute ("SHOW TABLES")

for tables in cursor:
    print(tables)

cursor.execute ("DESCRIBE products")

for describe in cursor:
    print(describe)

cursor.execute ('''INSERT INTO products(id_categories, id_brands , name, description , image , id_sellers) 
                VALUES (1,4,"Redmi 12C" , "Celular XIAOMI Redmi 12C 4GB + 128GB Verde","d:/tecnologia/xiomi/xiomi12c","1") ''')

database.commit()

cursor.execute ("SELECT * FROM products")

for select in cursor:
    print(select)

cursor.execute ("""UPDATE products SET image = 'd:/tecnologias/xiomi/xiomi12c.png' WHERE id_products=5""")
database.commit ()

cursor.execute ("SELECT * FROM products")

for select in cursor:
    print(select)

cursor.execute ("DELETE FROM products WHERE id_products = 5 ")
database.commit ()

cursor.execute ("SELECT * FROM products")

for select in cursor:
    print(select)

name = "Harold Sabogal"
query ="INSERT INTO brands (name) VALUES ('"+ name  +"')" #El signo mas es para concatenar
cursor.execute(query)
database.commit()

print("----------------------------------------------------------------------")
cursor.execute ("SELECT * FROM brands")

for select in cursor:
    print(select)
```
>El codigo se encuentra **[Aqui](./DataBase/DatabasePrueba1.py)**



------
## Seguire aprendiendo mas acerca del mundo de **python!**. Este es solo el principio:green_heart:

--------
#### Puedes apoyar mi trabajo haciendo "☆ Star" en el repo. ¡Gracias!

 ### Hola, mi nombre es Harold Sabogal.
### Estudiante del SENA

![GitHub Followers](https://img.shields.io/github/followers/dst3v3n?style=social)
![GitHub Followers](https://img.shields.io/github/stars/dst3v3n?style=social)

Soy estudiante del SENA desde hace dos año. Este años estoy aprendiendo sobre Analisis y Desarrollo de Software (ADSO) como lo he comentado anteriormente. Quiero seguir aprendiendo mas sobre el mundo del Desarrollo de software **[@dst3v3n](https://github.com/dst3v3n)**.

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/Guthub-dst3v3n-00B894?style=for-the-badge&logo=github&logoColor=00B894&labelColor=black)](https://github.com/dst3v3n)
