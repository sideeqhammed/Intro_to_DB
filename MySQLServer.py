import mysql.connector
from getpass import getpass


try:
  with connect(
    host = "localhost",
    port= 3308,
    user = input("Enter your username: "),
    password = getpass("Enter your password: ")
  ) as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")

except Error as e:
  print(e)