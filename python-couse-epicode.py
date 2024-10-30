##print("hello words")
##print ("Aldo","Giovanni","Giacomo",sep="\n")  #"portare a capo"#
##print("Aldo,","Giacomo,","Giovanni.")

##print("aldo", end=",")    #"portare tutto in una riga #
##print("giovanni", end=",")   #"portare tutto in una riga #
##print("giacomo", end=".")     #"portare tutto in una riga #

##print("jacqueline","marge","lisa",sep=" -> ") 

##print("ciao come ti chiami ")
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
##print("Il tipo di dato dell'input è:", type(input_utente))


#harry_potter=''' Harry si sentì leggero mentre saliva sulla scopa volante.
#Per la prima volta, Harry provò il brivido del decollo.
#Quella del volo, diventò immediatamente la più grande passione di Harry.'''

# Richiesta della parola da trovare
#parola_da_trovare = input("Inserisci la parola da trovare nel testo: ")

# Conteggio delle occorrenze della parola
#occorrenze = harry_potter.lower().count(parola_da_trovare.lower())
##print(f"La parola '{parola_da_trovare}' appare {occorrenze} volte nel testo.")

# Richiesta della nuova parola con cui sostituire
#nuova_parola = input("Inserisci la nuova parola con cui sostituire: ")

# Sostituzione della parola
#testo_modificato = harry_potter.replace(parola_da_trovare, nuova_parola)

# Stampa del testo modificato
##print("\nTesto modificato:")
##print(testo_modificato)


#print("inserisci il tuo anno di nascita ")
#anno_nascita=int(input())
#anno_cliente=2024-anno_nascita
#print(anno_cliente)


#if anno_cliente < 18:
    #print('sei minorenne non hai la patente e non puoi guidare ')
  

#else:    
    #print('sei maggiorenne hai l eta per guidare ma hai ottenuto la patente ?')
    #patente_guida=str(input())
   
    #if patente_guida== "si":
        #print('sei autorizato a guidare')

    #else:
        #print('sei maggiorenne ma non hai la patente e non puoi guidare ')    
   

  
#temperature = 8


#if temperature > 70:
 #print("INCEDIO! Attiva estintori!")
#elif temperature > 30:
 #print("Accendi il raffreddamento")
#elif temperature < 10:
 #print("Accendi il riscaldamento")
#else:
 #print("Temperatura ideale")


#is_user_logged_in=False
#user_status="Active"if is_user_logged_in else "Inactive"
#print(user_status)

#name=input("Inserisci il tuo nome ")
#if name:
# print(f"Ciao {name}")
#else:
# print("nome non inserito")

#correct_psw="bartsimpson"
#psw=None

 #while psw!=correct_psw:
  #  psw=input("Inserisci la tua password ")
 #print("Accesso riuscito")

 

 #tasks=["fare la spesa ","cucinare","lavare i piatti "]
 #for task in tasks:
  #  print(task)

 #for i in range(2):
 #   print(i)



 #for i in range(10):
 #   print(i)

#for seconds in range(10,0,-1):
 #  print(f"Mancano {seconds} secondi")
  #if seconds==5:
   #  break
#else:
 # print("E' Capodanno!")     




#correct_number=8
#number=None

#while number!=correct_number:
    #number=int(input("Inserisci il mio numero preferito da 0 a 9 "))
    #if number==correct_number:
     #   print("corretto hai trovato il mio numero preferito")
    #elif number<0 or number>9:
   #     print("il numero inserito non è valido, ritenta ")    
  #  else:   
 #       print("non hai trovato il mio numero preferito ritenta ")
#print("Grazie per aver giocato")        



#implementare il numero di tentativi.
#Stavolta è vietato utilizzare il ciclo while!
#Ad ogni iterazione,
#stampa il numero del tentativo corrente,
#as esempio “Tentativo n. 1”
#poi, come sempre, richiedi l'inserimento del numero,
#e valuta se è corretto.
#Se l'utente non indovina entro 5 tentativi,
#il gioco termina, stampando un messaggio opportuno.

#import random

#numero_da_indovinare = random.randint(1, 100)

#tentativi_max = 5

#for tentativo in range(1, tentativi_max + 1):
 #   print(f"Tentativo n. {tentativo}")
  #  numero = int(input("Inserisci un numero tra 1 e 100: "))
   # if numero == numero_da_indovinare:
    #    print("Complimenti! Hai indovinato il numero.")
     #   break
    #elif numero < numero_da_indovinare:
     #   print("Il numero è più grande.")
    #else:
     #   print("Il numero è più piccolo.")

    
    #if tentativo == tentativi_max:
     #   print(f"Mi dispiace, hai terminato i {tentativi_max} tentativi. Il numero era {numero_da_indovinare}.")


clients=["Maria","Luisa","Marco"]

for client in clients:
    print(client)


# Crea una lista della spesa che contenga
# alcuni articoli a piacere.
# Ordina gli articoli alfabeticamente
# e poi stampali tutti a schermo,
# ognuno di essi preceduto da un trattino.
# Ora chiedi all'utente un nuovo articolo
# da aggiungere.
# Se l'utente non inserisce nulla,
# stampa un messaggio di errore,
# Se l'utente inserisce un articolo già presente,
# stampa un messaggio di errore.
# Se l'utente inserisce correttamente
# un nuovo articolo,
# aggiungilo alla lista.
# In ogni caso, al termine del programma,
# stampa nuovamente tutti gli articoli
# (sempre ordinati alfabeticamente).
# BONUS: attenzione al case!