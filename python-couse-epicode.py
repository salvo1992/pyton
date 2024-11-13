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


# clients=["Maria","Luisa","Marco"]

# for client in clients:
#     print(client)


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


# modifica il programma precedente :
# sel'utente inserisce un articolo presente,
# chiedi al utente se vuole rimuoverlo.
# in caso affermativo, rimuovi l'articolo
# dalla lista.


# items = ["fagioli", "noci", "mele"]
# items.sort()


# for item in items:
#  print("-", item)


# user_item = input("Aggiungi un articolo: ").lower().strip()


# if not user_item:
#  print("Errore: Non hai inserito alcun articolo")
# elif user_item in items:
#  print("Errore: Articolo già presente")
# else:
#  items.append(user_item)
# print("Articolo aggiunto ✅")
# items.sort()


# for item in items:
#  print("-", item)



# EPICODE Institute of Technology 30/10/2024 21:01 • 
# Modifica il programma precedente:
# l'utente deve poter inserire più articoli alla volta,
# separandoli col carattere |
# In tal caso, il programma converte
# tale stringa inserita dall'utente in una lista di articoli,
# i quali vengono poi aggiunti alla lista iniziale.
# Per semplicità, non controllare se l'utente
# inserisce articoli già presenti o stringhe vuote.


# items = ["FAGIOLI", "NOCI", "MELE"]
# split_char = "|"
# items.sort()


# for item in items:
#  print("-", item)


# user_item = input("Aggiungi un articolo: ").upper().strip()


# if split_char in user_item:
#  to_add_items = user_item.split(split_char)
#  items.extend(to_add_items)
#  print("Articoli aggiunti")
#  items.sort()
# elif not user_item:
#  print("Errore: Non hai inserito alcun articolo")
# elif user_item in items:
#  print("Errore: Articolo già presente")
#  user_answer = input("Vuoi rimuoverlo? In caso affermativo scrivi si: ")
# if user_answer == "si":
#  items.remove(user_item)
#  print("Articolo rimosso")
# else:
#  print("Articolo non rimosso")
# else:
# items.append(user_item)
#  print("Articolo aggiunto ✅")
#  items.sort() 


#  for item in items:
#   print("-", item)



# panda = {
# "color": "red",
# "price": 35_000.0,
# "year": 2024,
# "hybrid": True
# }


# punto = {
# "color": "green",
# "price": 25_000.0,
# "year": 2014,
# "hybrid": False
# }



# def get_discounted_price(price):
#  discounted_price = price * 0.7
#  if discounted_price > 20_000:
#   discounted_price -= 100
#  print(discounted_price)



# get_discounted_price(panda["price"])



# panda = {
# "color": "red",
# "price": 35_000.0,
# "year": 2024,
# "hybrid": True
# }


# punto = {
# "color": "green",
# "price": 25_000.0,
# "year": 2014,
# "hybrid": False
# }



# def get_discounted_price(price, *bonus_discounts):
# discounted_price = price * 0.7
# if discounted_price > 20_000:
# for discount in bonus_discounts:
# discounted_price -= discount
# return discounted_price



# print(get_discounted_price(panda["price"], 100, 150, 200))

 
# Modifica l'esercizio della lezione precedente,
# (vedi codice di partenza in chat)
# ma basandolo su un dizionario, invece che su una lista.
# Il dizionario iniziale deve contenere
# come chiave il prodotto da acquistare
# e come valore la sua quantità.
# All'utente sarà richiesto di inserire
# sia il prodotto che la quantità.
# Non è necessario ordinare il dizionario.


# BONUS:
# Se l'articolo è già presente,
# chiedi di inserire la quantità
# e aggiornala sul dizionario.


# converti items da lista in dizionario {key:val, ...}
# items = {
# "fagioli": 10,
# "noci": 5,
# "mele": 15
# }


# # stampa le coppie chiave e valore del dizionario items.items()
# for item, quantity in items.items():
#  print(f"- {item} ({quantity} pezzi)")


# user_item = input("Aggiungi un articolo: ").lower().strip()


# if not user_item:
#  print("Errore: Non hai inserito alcun articolo")
# elif user_item in items:
#    print("Articolo già presente")
# # richiedi all'utente la quantità
#    user_quantity = int(input("Inserisci la quantità: ").strip())
# # sul dizionario modifica il valore della chiave già presente items[new_key] = new_val
#    items[user_item] = user_quantity
#    print("Articolo aggiornato ✅")
# else:
# # richiedi all'utente la quantità
#   user_quantity = int(input("Inserisci la quantità: ").strip())
# # sul dizionario crea la nuova coppia chiave valore items[new_key] = new_val
#   items[user_item] = user_quantity
# print("Articolo aggiunto ✅")


# # vedi ciclo precedente
# for item, quantity in items.items():
#   print(f"- {item} ({quantity} pezzi)")
    


person1={
  "name": "John",
  "surname": "Doe",
  "age": None,
  "city": "New York",
  "hobbies": ["reading", "painting"]
}

person2={    
  "name": "Jane",
  "surname": "Doe",
  "age": None,
  "city": "New York",
  "hobbies": ["painting", "hiking"]
}
def calculate_age(name, current_year ):
   birth_year = int(input(f" {name}, inserisci il tuo anno di nascita: "))
   age = current_year - birth_year
   return age


person1["age"] = calculate_age(person1["name"],2024) 
person2["age"] = calculate_age(person2["name"],2024) 


print(person1)
print(person2)

# # Crea una classe Pokemon coi seguenti attributi:
# Nome, Salute e Forza.
# Implementa un metodo di attacco che permetta
# a un Pokemon di attaccarne un altro,
# riducendo la Salute dell'avversario.
# (al metodo passeremo come argomento un oggetto Pokemon)
# La Salute dell'avversario viene ridotta
# di un valore pari alla Forza dell'attaccante.
# Il metodo infine stampa un messaggio,
# con alcuni dettagli sull'attacco, ad esempio:
# Pikachu attacca Charizard causando 15 danni!


# Completata la classe, istanzia due Pokemon
# e falli attaccare l'un l'altro, quante volte desideri.
# Dopo il combattimento, stampa la Salute
# di entrambi, per vedere se è coerente con gli attacchi.




 
class Pokemon:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attacks(self, enemy):
        enemy.health -= self.strength
        print(f"{self.name} attacca {enemy.name} causando {self.strength} danni!")

pikachu = Pokemon("Pikachu", 100, 15)
charizard = Pokemon("Charizard", 150, 20)

pikachu.attacks(charizard)
charizard.attacks(pikachu)
pikachu.attacks(charizard)

print(pikachu.health, charizard.health)



