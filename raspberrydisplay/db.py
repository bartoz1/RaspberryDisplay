import mysql.connector
from datetime import datetime
import configparser


class DB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self._mydb = mysql.connector.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])
        self._mycursor = self._mydb.cursor()
        self._seccursor = self._mydb.cursor()


    def get_last_update(self):
        self._mycursor.execute("SELECT created_at FROM sales ORDER BY created_at DESC LIMIT 1")
        myresult = self._mycursor.fetchall()
        data = myresult[0][0]
        return data

    def __del__(self):
        self._mydb.close()