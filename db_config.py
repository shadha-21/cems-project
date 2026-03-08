#import mysql.connector

#def get_db_connection():
#    return mysql.connector.connect(
#        host="localhost",
#        user="root",
#        password="Shadha@123",
#  )

import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=os.getenv("MYSQLPORT")
    )