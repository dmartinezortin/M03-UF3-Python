import mysql.connector
from mysql.connector import errorcode
import  functions as f
from credentials import creds

def insert_data():
    try:
        cnx = mysql.connector.connect(user=creds['user'],
                                      password=creds['passw'],
                                      host=creds['host'],
                                      database=creds['database'])
        data_list = f.df_to_list()
        crs = cnx.cursor()
        select = (f"SELECT * FROM %s" % (creds['table']))
        crs.execute(select)
        result = crs.fetchall()
        count = 0
        to_add = list()
        print(result)
        if len(result) == 0:
            to_add = tuple(data_list)
        else:
            for item in data_list:
                if item not in result:
                    to_add.append(item)

        for item in to_add:
            item = tuple(item)
            print(item)
            crs.execute("INSERT INTO tb_video (id, group_name, song_name, publish_date, views)"
                        "VALUES (%s, %s, %s, %s, %s)",
                        (item))
            count += 1
            cnx.commit()
        print(f"Base de dades actualitzada, total de registres afegits: {count}")
        crs.close()
    except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)