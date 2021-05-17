import functions as f
def main():

    for x in range(f.request_int("Quants registres vols introduir? ")):
        id_campaign, group, song_name, publish_date, views = f.request_int("Introdueix el id: "), input("Nom del grup/cantant: "), input("Nom de la canço: "), f.request_date("xx/xx/xxxx"), f.request_int("Introdueix les visualitzacions: ")
        data = [id_campaign, group, song_name, publish_date, views]
        f.insert(data)
        f.read_values()

if __name__ == '__main__':
    main()

