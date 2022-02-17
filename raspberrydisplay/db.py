import mysql.connector
from datetime import datetime
import configparser


class DB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self._query = config['mysqlDB']['query']
        self._query = self._query.replace("'", "")
        self._mydb = mysql.connector.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'],
                           autocommit=True)


    def get_last_update(self):
        self._mycursor = self._mydb.cursor()
        self._mycursor.execute(self._query)
        myresult = self._mycursor.fetchall()
        data = myresult[0][0]
        return data

    def __del__(self):
        self._mydb.close()