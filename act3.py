import functions as f
import sys as sys

def main():

    #demana un numero del 1 al 4
    option = f.request_option()
    if option == 1:
        fname = input("Afegeix el nom del document: ")
        f.add_to_file("files/" + fname, "", "w")
    elif option == 2:
        fname = input("Afegeix el nom del document: ")
        f.read_file("files/" + fname, "r")
    elif option == 3:
        fname = input("Afegeix el nom del document: ")
        f.add_to_file("files/" + fname, input("Introdueix el text a afegir: "), "a")
    else:
        sys.exit()
if __name__ == '__main__':
    main()
