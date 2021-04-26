import sys as sys

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
    num = int(input("Introdueix un numero: "))
    while num < 0:
        num = int(input("Introdueix un numero: "))
    return  num
def request_date(format = "xx/xx/xxxx"):
    check_pattern = list([x for x in range(len(format)) if format[x] == "/"])
    date = input("Introdueix una data: ")
    while date[check_pattern[0]] != "/" or date[check_pattern[1]] != "/":
        date = input("Introdueix una data")
    return date

def get_index():
    f = open("files/act4.txt", "r")
    try:
        # Llegeix el text del document
        index_id = f.readlines()
        f.close()
    except:
        # Obté el error del procés i el printa
        err = sys.exc_info()[1]
        print(err)