import mysql.connector
from mysql.connector import errorcode
import  functions as f
from credentials import creds

def insert_data():
    try:
        cnx = mysql.connector.connect(user=creds['user'], password=creds['passw'], host=creds['host'], database=creds['database'])
        data_list = f.df_to_list()
        table = creds['table']
        crs = cnx.cursor()
        result = crs.fetchall()
        count = 0
        to_add = list()
        for query in result:
            for reg in data_list:
                reg = tuple(reg)
                if reg[0] != query[0]:
                    to_add.append(list(reg))
                    count += 1
        to_add = tuple(to_add)
        for item in to_add:
            print(item)
        print(f"Base de dades actualitzada, total de registres afegits: {count}")
        crs.close()
    except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)