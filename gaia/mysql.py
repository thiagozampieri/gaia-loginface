import sys
#import mysql.connector
from mysql.connector import MySQLConnection, Error
import thanos.settings as settings

db = settings.DATABASES['default']

config = {
 'user': db['USER'],
 'password': db['PASSWORD'],
 'host': db['HOST'],
 'port': db['PORT'],
 'database': db['NAME'],
}

def find(query_string):
    try:
        conn = MySQLConnection(**config)
        cursor = conn.cursor()
        cursor.execute(query_string)
        rows = cursor.fetchall() 
        return rows
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()

def findOne(query_string):
    try:
        conn = MySQLConnection(**config)
        cursor = conn.cursor()
        cursor.execute(query_string)
        row = cursor.fetchone() 
        return row
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
