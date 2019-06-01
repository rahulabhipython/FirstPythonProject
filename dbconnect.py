import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="1111",database = "pythondemodb")
mycursor=mydb.cursor()
mycursor.execute("select * from customer")
result = mycursor.fetchone()
print("hello changes from pycharm")
for i in result:
    print(i)