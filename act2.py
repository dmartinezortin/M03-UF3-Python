import functions as f

def main():
    #Demana un string de maxim 100 caracters
    str = f.request_string(100)
    print(str)
    #Defineix on es el fitxer i el passa a la funció
    filename = "files/test.txt"
    f.add_to_file(filename, str, "a")

if __name__ == '__main__':
    main()
