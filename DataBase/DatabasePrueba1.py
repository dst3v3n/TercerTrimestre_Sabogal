import mysql.connector

database = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "comercializadora"
)

cursor = database.cursor ()

# cursor.execute ("SHOW TABLES")

# for tables in cursor:
#     print(tables)

# cursor.execute ("DESCRIBE products")

# for describe in cursor:
#     print(describe)

# cursor.execute ('''INSERT INTO products(id_categories, id_brands , name, description , image , id_sellers) 
#                 VALUES (1,4,"Redmi 12C" , "Celular XIAOMI Redmi 12C 4GB + 128GB Verde","d:/tecnologia/xiomi/xiomi12c","1") ''')

# database.commit()

# cursor.execute ("SELECT * FROM products")

# for select in cursor:
#     print(select)

# cursor.execute ("""UPDATE products SET image = 'd:/tecnologias/xiomi/xiomi12c.png' WHERE id_products=5""")
# database.commit ()

# cursor.execute ("SELECT * FROM products")

# for select in cursor:
#     print(select)

# cursor.execute ("DELETE FROM products WHERE id_products = 5 ")
# database.commit ()

cursor.execute ("SELECT * FROM products")

for select in cursor:
    print(select)


name="Alirio Suarez"
doc='909997'
formacion='adso'
genero='m'


# query ="INSERT INTO brands (name) VALUES ('"+ name  +"','"+  doc+"','"+formacion+"','"+genero+"')"#El signo mas es para 
# cursor.execute(query)
# database.commit()

print("'"+ name  +"','"+  doc+"','"+formacion+"','"+genero+"'")

cursor.execute ("SELECT * FROM brands")

for select in cursor:
    print(select)