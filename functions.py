import sys as sys
import pandas as pd
ACT4 = "files/act4.csv"
BLOCK_LENGTH = 5

def request_string(str_size):
    str = input("introdueix el string: ")
    while len(str) > str_size:
        input("introdueix el string: ")
    return str

def add_to_file(filename, str, operation):
    f = open(filename, operation)
    try:
        #Escriu el string al document
        f.writelines(str)
        f.close()
    except:
        #Obté el error del procés i el printa
        err = sys.exc_info()[1]
        print(err)
    else:
        #Cas que tot ha estat correcte
        print("Processant...")
    finally:
        #Finalment, hagi fallat o no, tanca el programa
        print("Sortint del programa.")

def read_file(filename, operation):
    f = open(filename, operation)
    try:
        # Llegeix el text del document
        print(f.read())
        f.close()
    except:
        # Obté el error del procés i el printa
        err = sys.exc_info()[1]
        print(err)
    else:
        # Cas que tot ha estat correcte
        print("Processat...")
    finally:
        # Finalment, hagi fallat o no, tanca el programa
        print("Sortint del programa.")
        
def request_option():
    option = int(input("Que vols fer? \n1.Crear un fitxer\n2.Mostrar el contingut d'un fitxer\n3.Modificar el contingut d'un fitxer\n4.Sortir\n"))
    while option > 4 or option < 1:
        option = int(input("Que vols fer? \n1.Crear un fitxer\n2.Mostrar el contingut d'un fitxer\n3.Modificar el contingut d'un fitxer\n4.Sortir\n"))
    return option

def request_int(str):
    num = -1
    while num < 0 :
        try:
            num = int(input(str))
        except:
            pass
    return num



def request_date(format = "xx/xx/xxxx"):

    check_pattern = list([x for x in range(len(format)) if format[x] == "/"])
    date = "/"
    date_arr = []
    while len(date) != len(format) or date[check_pattern[0]] != "/" or date[check_pattern[1]] != "/" or int(date_arr[0]) > 31 or int(date_arr[1] > 12):
        date = input("Introdueix una data: ")
        date_arr = date.split("/")
        print(date_arr)
        while int(date_arr[0]) is ValueError or int(date_arr[1]) is ValueError:
            date = input("Introdueix una data (Format numeric!!) : ")
            date_arr = date.split("/")
            print(date_arr)

    return date


def insert(main_dict):
    df = pd.DataFrame.from_dict(main_dict, orient='index', columns=['group', 'song_Name', 'publish_date', 'views'])
    df.index.name = 'id'
    df.to_csv(ACT4, mode='a')

def read_values():
    selected_col = input("Quina columna vols llegir?").lower()
    selected_value = input("Quin valor vols llegir?").lower()
    df = pd.read_csv(ACT4)
    query = df.query(f"{selected_col} == '{selected_value}'", inplace=False)
    print(query)