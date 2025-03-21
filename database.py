import mysql.connector

connection=mysql.connector.connect(host="localhost", user="mayur", password="", database="joviancreers")

cmd=connection.cursor()
cmd.execute("select * from jobs")
data=cmd.fetchall()
for row in data:
    print(row)
con.close()    