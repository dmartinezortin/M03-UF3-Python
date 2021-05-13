
import act4 as ins
import dbfunctions as db



def main():
    if input("Vols afegir nous registres? S/N").upper() == "S":
        ins.main()
    else:
        print("Actualitzant la base de dades... ")
    try:
        db.insert_data()
    except:
        # Obte el error del proces i el printa
        err = sys.exc_info()[1]
        print(err)

if __name__ == '__main__':
    main()

