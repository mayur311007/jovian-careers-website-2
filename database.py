import mysql.connector

connection = mysql.connector.connect(host="localhost",user="mayur",password="mayur.123",database="joviancreers")

if connection.is_connected():
    print('connected successfully')

else:
    print('failed')    

connection.close()   