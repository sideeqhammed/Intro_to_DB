import mysql.connector
from getpass import getpass


try:
  mydb = mysql.connector.connect(
    host = "localhost",
    port= 3308,
    user = input("Enter your username: "),
    password = getpass("Enter your password: ")
  )
  cursor = mydb.cursor()
  cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
  print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
  print(e)