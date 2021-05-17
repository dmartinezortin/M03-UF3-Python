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
        # Escriu el string al document
        f.writelines(str)
        f.close()
    except:
        # Obté el error del procés i el printa
        err = sys.exc_info()[1]
        print(err)
    else:
        # Cas que tot ha estat correcte
        print("Processant...")
    finally:
        # Finalment, hagi fallat o no, tanca el programa
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
    option = int(input(
        "Que vols fer? \n1.Crear un fitxer\n2.Mostrar el contingut d'un fitxer\n3.Modificar el contingut d'un fitxer\n4.Sortir\n"))
    while option > 4 or option < 1:
        option = int(input(
            "Que vols fer? \n1.Crear un fitxer\n2.Mostrar el contingut d'un fitxer\n3.Modificar el contingut d'un fitxer\n4.Sortir\n"))
    return option


def request_int(str):
    num = -1
    while num < 0:
        try:
            num = int(input(str))
        except:
            pass
    return num


def request_date(format="xx/xx/xxxx"):
    check_pattern = list([x for x in range(len(format)) if format[x] == "/"])
    date = "/"
    date_arr = []
    while len(date) != len(format) or date[check_pattern[0]] != "/" or date[check_pattern[1]] != "/":
        date = input("Introdueix una data: ")
        date_arr = date.split("/")
        print(date_arr)
    return date


def insert(data):
    actual_df = pd.read_csv(ACT4)
    #new_df = pd.DataFrame.from_dict(data, orient= 'index')
    actual_df.loc[len(actual_df)] = data
    print(actual_df)
    actual_df.to_csv(ACT4, mode='w', index=False)


def read_values():
    selected_col = input("Quina columna vols llegir?").lower()
    selected_value = input("Quin valor vols llegir?").lower()
    df = pd.read_csv(ACT4)
    print(df)
    try:
        query = df.query(f"{selected_col} == '{selected_value}'", inplace=False)
        print(query)
    except:
        print("ups... Prueba a decir una columna o valor adecuado")
        pass

def df_to_list():
    df = pd.read_csv(ACT4)
    return df.values.tolist()