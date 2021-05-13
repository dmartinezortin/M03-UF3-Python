import mysql.connector
from mysql.connector import errorcode
import  functions as f

USER = "dmartinez_camp"
PASSW = "4dm1n_c4mp41gn"
HOST = "mysql-dmartinez.alwaysdata.net"
TABLE = "tb_video"

def insert_data():
    try:
        cnx = mysql.connector.connect(user=USER, password=PASSW, host=HOST)
        data_list = f.df_to_list()
        for list in data_list:
            list = tuple(list)
            print(list)
    except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)