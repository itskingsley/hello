import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES ")

for x in mycursor:
  print(x)

#If this page is executed with no error, you have successfully created a database.
