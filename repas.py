import sys as sys
import act4 as ins
import dbfunctions as db
import functions as f

def main():
    option = f.user_menu()
    if option == 1:
        ins.main()
    elif option == 2:
        f.read_values()
    elif option == 3:
        f.csv_to_txt()
    elif option == 4:
        f.csv_to_json()


if __name__ == '__main__':
    main()

