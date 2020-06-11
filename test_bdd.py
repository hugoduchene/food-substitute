import mysql.connector
mybd = False
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test")
myresult = mycursor.fetchall()

if myresult == []:
    print("hey")
else:
    print("OHHH")

mydb.commit()
