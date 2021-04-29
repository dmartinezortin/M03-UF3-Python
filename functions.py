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
    num = int(input(str))
    while num < 0:
        num = int(input(str))
    return  num
def request_date(format = "xx/xx/xxxx"):
    check_pattern = list([x for x in range(len(format)) if format[x] == "/"])
    date = input("Introdueix una data: ")
    while len(date) != len(format) or date[check_pattern[0]] != "/" or date[check_pattern[1]] != "/" :
        date = input("Introdueix una data: ")
    return date

def insert_dict(main_dict):
    with open(ACT4, "a+") as f:
        try:
            if f.read(1):
                new_df = pd.DataFrame(main_dict)
                new_df.to_csv(ACT4)
            else:
                actual_df = pd.read_csv(ACT4)
                print(actual_df)
            f.close()
        except:
            # Obté el error del procés i el printa
            err = sys.exc_info()[1]
            print(err)

def get_index(main_dict, id_campaign):
    offset = 0
    with open(ACT4, "r+") as f:
        f.seek(0)
        try:
            for line in f:
                offset += len(line)


        except:
            # Obté el error del procés i el printa
            err = sys.exc_info()[1]
            print(err)

