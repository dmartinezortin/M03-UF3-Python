import functions as f
def main():

    id_campaign, group, song_name, publish_date, views = f.request_int("Introdueix el id: "), input("Nom del grup/cantant: "), input("Nom de la canço: "), f.request_date("xx/xx/xxxx"), f.request_int("Introdueix les visualitzacions: ")
    aux_dict = {id_campaign: { 'grup/cantant' : group, 'nom de la canço' : song_name, 'data publicacio' : publish_date,'visualitzacions' : views,} }
    main_dict = dict(aux_dict)
    f.insert(main_dict)
if __name__ == '__main__':
    main()
