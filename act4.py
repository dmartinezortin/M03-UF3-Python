import functions as f
def main():
    id_campaign, group, song_name, publish_date, views = f.request_int("Introdueix el id: "), input("Nom del grup/cantant: "), input("Nom de la canço: "), f.request_date("xx/xx/xxxx"), f.request_int("Introdueix les visualitzacions: ")

if __name__ == '__main__':
    main()
