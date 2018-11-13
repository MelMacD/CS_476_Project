
from code import app
from flask import request
    
@app.route("/bloglist", methods=['GET', 'POST'])

def bloglist():
    if request.method == 'POST':
        return ""
    else:
        return """

import mysql.connector
from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='tcp:expressyourself.database.windows.net',
                             database='expressyourself',
                             username='cs476',
                             password='$up3rSecret')
   sql_select_Query = "select * from blog"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in blog is - ", cursor.rowcount)
   print ("Printing each row's column values i.e.  blog records")
   for row in records:
       print("username = ", row[0], )
       print("blogName = ", row[1])
       print("descr  = ", row[2], "\n")
   cursor.close()
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")

