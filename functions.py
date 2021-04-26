import sys as sys

ACT4 = "files/act4.txt"

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
        date = input("Introdueix una data")
    return date

def insert_dict(main_dict, pointer = 0):
    f = open(ACT4, "a")
    f.seek(pointer)
    try:
        # Llegeix el text del document
        for key, value in main_dict.items():
            print("{ id:", key , "\n\t{", file = f)
            for x, y in value.items():
                print("\t\t" + x + ":", y, ",", file = f)
            print("\t}\n}\n", file = f)
        f.close()
    except:
        # Obté el error del procés i el printa
        err = sys.exc_info()[1]
        print(err)

def get_index(main_dict):
    pointer = 0
    is_updated = False
    with open(ACT4, "r+") as f:
        target_index = list(main_dict)
        target_index = target_index[0]
        try:
            # Llegeix el text del document
            f.seek(0)
            chunk = f.readline()
            while chunk != '':
                chunk = f.readline()
                line = f.readline()
                num = line.split()
                if line.startswith("{ id:"):
                    if target_index < int(num[-1]):
                        pointer = f.tell()
                        f.close()
                        insert_dict(main_dict, pointer)
                        print(pointer)
                        is_updated = True
                        break

            if is_updated == False:
                insert_dict(main_dict)
        except:
            # Obté el error del procés i el printa
            err = sys.exc_info()[1]
            print(err)

    return pointer