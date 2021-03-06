import mysql.connector
from mysql.connector import errorcode
import functions as f
from credentials import creds

def insert_data():
    try:
        cnx = mysql.connector.connect(user=creds['user'],
                                      password=creds['passw'],
                                      host=creds['host'],
                                      database=creds['database'])
        crs = cnx.cursor()
        to_add = tuple(f.df_to_list())
        for item in to_add:
            try:
                crs.execute("INSERT INTO tb_video (id, group_name, song_name, publish_date, views)"
                            "VALUES (%s, %s, %s, %s, %s)",
                            (item))

                cnx.commit()
            except mysql.connector.IntegrityError:
                print(f"Valor amb ID ja existent, passant al seguent id... (ID duplicat: {item[0]})")
        print(f"Base de dades actualitzada, total de registres afegits: {crs.rowcount}")
        crs.close()
    except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)