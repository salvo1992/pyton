#print("hello words")
#print ("Aldo","Giovanni","Giacomo",sep="\n")  #"portare a capo"#
#print("Aldo,","Giacomo,","Giovanni.")

#print("aldo", end=",")    #"portare tutto in una riga #
#print("giovanni", end=",")   #"portare tutto in una riga #
#print("giacomo", end=".")     #"portare tutto in una riga #

#print("jacqueline","marge","lisa",sep=" -> ") 

#print("ciao come ti chiami ")
#nome_utente =str( input())

#("ciao", nome_utente)


# modello_telefono = "iPhone 14"  # stringa (str) che rappresenta il modello del telefono
# anno_acquisto = 2022  # intero (int) che indica l'anno di acquisto
# prezzo = 999.99  # numero decimale (float) che rappresenta il prezzo del telefono
# in_garanzia = True  # booleano (bool) che indica se il telefono è ancora in garanzia

# modello_bicicletta = "BMX"  # stringa (str) che rappresenta il modello del telefono
# anno_acquisto = 2021  # intero (int) che indica l'anno di acquisto
# prezzo = 600.05  # numero decimale (float) che rappresenta il prezzo del telefono
# in_garanzia = False  # booleano (bool) che indica se il telefono è ancora in garanzia

# modello_Pc = "lenovo Notebook"  # stringa (str) che rappresenta il modello del telefono
# anno_acquisto = 2023  # intero (int) che indica l'anno di acquisto
# prezzo = 800.99  # numero decimale (float) che rappresenta il prezzo del telefono
# in_garanzia = True  # booleano (bool) che indica se il telefono è ancora in garanzia

# Richiesta di input all'utente
#input_utente = input("Inserisci qualcosa: ")

# Stampa del tipo di dato dell'input
#print("Il tipo di dato dell'input è:", type(input_utente))


harry_potter=''' Harry si sentì leggero mentre saliva sulla scopa volante.
Per la prima volta, Harry provò il brivido del decollo.
Quella del volo, diventò immediatamente la più grande passione di Harry.'''

# Richiesta della parola da trovare
parola_da_trovare = input("Inserisci la parola da trovare nel testo: ")

# Conteggio delle occorrenze della parola
occorrenze = harry_potter.lower().count(parola_da_trovare.lower())
print(f"La parola '{parola_da_trovare}' appare {occorrenze} volte nel testo.")

# Richiesta della nuova parola con cui sostituire
nuova_parola = input("Inserisci la nuova parola con cui sostituire: ")

# Sostituzione della parola
testo_modificato = harry_potter.replace(parola_da_trovare, nuova_parola)

# Stampa del testo modificato
print("\nTesto modificato:")
print(testo_modificato)
