import functions as f
def main():
    add = input("Vols introfuir valors? S/N: ")
    if add.upper() == "S":
        for x in range(f.request_int("Quants registres vols introduir? ")):
            id_campaign, group, song_name, publish_date, views = f.request_int("Introdueix el id: "), input("Nom del grup/cantant: "), input("Nom de la canço: "), f.request_date("xx/xx/xxxx"), f.request_int("Introdueix les visualitzacions: ")
            aux_dict = {id_campaign: [group, song_name, publish_date, views]}
            main_dict = dict(aux_dict)
            f.insert(main_dict)
    else:
        f.read_values()

if __name__ == '__main__':
    main()

