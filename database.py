
# # Database setup
# # ============================================================
# # 1)https://www.sqlite.org/download.html
# # 2) crte   afolder and extrar all the file in the folder (SQLite)


# # C:/SQLiteimport 
# # 	-
# # 	-
# # 	=


# import sqlite3




# connection = sqlite3.connect('PythonClass')

# connection.close()

# ===================================================================================
# Creatig a table in my Database

# import sqlite3

# connection = sqlite3.connect('PythonClass')

# connection.execute('''CREATE TABLE class1130  
# 					(ID INT PRIMARY KEY  NOT NULL,
# 					 NAME TEXT  NOT NULL,
# 					 AGE INT NOT NULL,
# 					 ADDRESS CHAR(100) NOT NULL,
# 					 PROOF TEXT NOT NULL);''')

# print('THE TABLE HASE BEEN CREATED SUSSFULLY.........!!!')

# connection.close()

# sqlite3 commnads
# =========================================================================
# .tables
# .show
# .users
# .quit
# .schema


#  sqlite3 PythonClass
# SQLite version 3.11.0 2016-02-15 17:29:24
# Enter ".help" for usage hints.
# sqlite> .users
# Error: unknown command or invalid arguments:  "users". Enter ".help" for help
# sqlite> .user
# Error: unknown command or invalid arguments:  "user". Enter ".help" for help
# sqlite> .tables
# class1130
# sqlite> .schema
# CREATE TABLE class1130  
# 					(ID INT PRIMARY KEY  NOT NULL,
# 					 NAME TEXT  NOT NULL,
# 					 AGE INT NOT NULL,
# 					 ADDRESS CHAR(100) NOT NULL,
# 					 PROOF TEXT NOT NULL);
# sqlite> 

# INsert data in TABLE
# ===================================================================================
# import sqlite3

# connection = sqlite3.connect('PythonClass')

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(1,'himan55',23,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(2,'batman',22,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(3,'superman',21,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(4,'Iornman',18,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(5,'wonderwomen',23,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(6,'tonystark',23,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(7,'himan',23,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(8,'himan1',23,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(9,'himan2',23,'gachibowli','aadhar')")

# connection.execute("INSERT INTO class1130  (ID,NAME,AGE,ADDRESS,PROOF) \
# 						values(10,'himan3',23,'gachibowli','aadhar')")

# connection.commit()

# connection.close()



# vineet@vineetiot:~/Documents/vineet/python/python1130$ sqlite3 PythonClass
# SQLite version 3.11.0 2016-02-15 17:29:24
# Enter ".help" for usage hints.
# sqlite> .tables
# class1130
# sqlite> select * from class1130;
# 1|himan55|23|gachibowli|aadhar
# 2|batman|22|gachibowli|aadhar
# 3|superman|21|gachibowli|aadhar
# 4|Iornman|18|gachibowli|aadhar
# 5|wonderwomen|23|gachibowli|aadhar
# 6|tonystark|23|gachibowli|aadhar
# 7|himan|23|gachibowli|aadhar
# 8|himan1|23|gachibowli|aadhar
# 9|himan2|23|gachibowli|aadhar
# 10|himan3|23|gachibowli|aadhar
# sqlite> .show
#         echo: off
#          eqp: off
#      explain: auto
#      headers: off
#         mode: list
#    nullvalue: ""
#       output: stdout
# colseparator: "|"
# rowseparator: "\n"
#        stats: off
#        width: 
# sqlite> echo ON;
# Error: near "echo": syntax error
# sqlite> echo ON
#    ...> 
#    ...> ^Z
# [2]+  Stopped                 sqlite3 PythonClass
# vineet@vineetiot:~/Documents/vineet/python/python1130$ sqlite3 PythonClass
# SQLite version 3.11.0 2016-02-15 17:29:24
# Enter ".help" for usage hints.
#
# sqlite> .headers ON
# sqlite> .mode coloum
# Error: mode should be one of: ascii column csv html insert line list tabs tcl
# sqlite> .mode column
# sqlite> select * from auth_user;
# Error: no such table: auth_user
# sqlite> select * from class1130;
# ID          NAME        AGE         ADDRESS     PROOF     
# ----------  ----------  ----------  ----------  ----------
# 1           himan55     23          gachibowli  aadhar    
# 2           batman      22          gachibowli  aadhar    
# 3           superman    21          gachibowli  aadhar    
# 4           Iornman     18          gachibowli  aadhar    
# 5           wonderwome  23          gachibowli  aadhar    
# 6           tonystark   23          gachibowli  aadhar    
# 7           himan       23          gachibowli  aadhar    
# 8           himan1      23          gachibowli  aadhar    
# 9           himan2      23          gachibowli  aadhar    
# 10          himan3      23          gachibowli  aadhar    
# sqlite> 


# Data base show dain tables
# ===============================================


import sqlite3

connection = sqlite3.connect('PythonClass')

deatails = connection.execute("SELECT  ID,NAME,AGE,ADDRESS,PROOF FROM  class1130")

for a in deatails:
	print('ID is :',a[0])
	print('NAME is :',a[1])
	print('AGE is :',a[2])
	print('ADDRESS is :',a[3])
	print('PROOF is :',a[4])
	print(60*'-')

connection.close()




# import sqlite3 

# connection = sqlite3.connect('python.db')

# connection.execute("UPDATE python_500 set NAME = 'superhero' where ID =1 ")
# connection.commit()
# print('The chager are',connection.total_changes)

# var = connection.execute("SELECT ID,NAME,AGE,ADDRESS,PROOF FROM python_500")

# for a in var:
# 	print('ID is:',a[0])
# 	print('NAME is:',a[1])
# 	print('AGE is:',a[2])
# 	print('ADDRESS is:',a[3])
# 	print('PROOF is:',a[4])
# 	print('-------------------------------\n')
# connection.close()


# import sqlite3 

# connection = sqlite3.connect('python.db')

# connection.execute("DELETE FROM python_500 WHERE ID = 3")
# print('The TOTAL CHANGES AER',connection.total_changes)
# var = connection.execute("SELECT ID,NAME,AGE,ADDRESS,PROOF FROM python_500")

# for a in var:
# 	print('ID is:',a[0])
# 	print('NAME is:',a[1])
# 	print('AGE is:',a[2])
# 	print('ADDRESS is:',a[3])
# 	print('PROOF is:',a[4])
# 	print('-------------------------------\n')
# connection.close()

 # UPDATE()
 # INSERT()
 # DELETE()