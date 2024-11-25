#class Car: 
#    wheels = 4
#    total_built_car = 0
#    total_drove_km = 0

#    def __init__(self, band,max_speed,year,is_electric):
#        self.band = band
#        self.max_speed = max_speed
#        self.year = year
#        self.is_electric = is_electric
#        Car.total_built_car +=1

#    def drive(self,kilometers):
#        print(f"La{self.band} guida per {kilometers} chilometri")
#        Car.total_drove_km +=kilometers
#    def __str__(self):
#        return f"Sono un bellissima {self.brand} del {self.year}"
    
    
#car1 = Car("fiat",200.0, 2020, True)
#car2 = Car("ferrari", 300.0, 2010, False)

#car1.drive(50)
#car1.drive(100)
#car1.drive(150)

#car1.total_drove_km = 0y

#print(car1.total_drove_km)

#setattr(car1, "is_electric", False)
#print(car1.is_electric)


#Definisci una classe che rappresenti
#uno strumento musicale,
#ad esempio una chitarra, un piano, etc...
#Assegna alla classe almeno due attributi d'istanza
#e almeno due attributi di classe, a piacere.

#Istanzia un oggetto della classe e applica
#il principio della Instrospection:
#con le funzioni hasattr e dir,
#verifica quali attributi sono accessibili
#sull'oggetto e quali sulla classe. 


#class payment:
    #def __init__(self,amount,currency):
    # self.amount = amount
   #  self.currency = currency

  #  def process(self):
 #       print(f"Paying {self.amount} {self.currency}")

#class CreditCardpayment(payment):
   # def __init__(self,amount,currency,card_number):
  #      super().__init__(amount,currency)
 #       self.card_number = card_number

#class PayPalPayment(payment):
  #  def __init__(self,amount,currency,email):
  #      super().__init__(amount,currency)
 #       self.email = email

#cc_payment = CreditCardpayment(100,"EUR","1234-1234-1234-1234")
#cc_payment.process

#pay_pal_payment = PayPalPayment(100,"EUR","j2oG1@example.com")
#pay_pal_payment.process

#payment1 = payment(100,"EUR")
#payment1.process        




#class payment:
    #def __init__(self,amount,currency):
     #self.amount = amount
     #self.currency = currency

    #def process(self):
    #    print(f"Paying {self.amount} {self.currency}")

   # def enage_processing(self):
  #      print("ability payment")
 #       self.process()    

#class PayPalPayment(payment):
    #def __init__(self,amount,currency,email):
    #    super().__init__(amount,currency)
   #     self.email = email

  #  def process(self):
 #       print(f"{self.email} is paying {self.amount} {self.currency}")

#payment1 = payment(100,"EUR")         
#paypal_payment=PayPalPayment(100,"EUR","j2oG1@example.com")
#payment.enage_processing()




#class payment:
 #   def __init__(self,payment_service)
  #      self.payment_service = payment_service

 #   def process(self):
 #       self.payment_service.make_payment()

#class CreditCardpayment:
 #   def make_payment(self):
 #       print("Credit card payment")

#class PayPalPayment:
#    def make_payment(self):
#        print("PayPal payment")   

#cc_payment_service = CreditCardpayment()
#pp_payment_service = PayPalPayment()

#pp_payment=payment(pp_payment_service)
#pp_payment.process()



# Crea una classe che rappresenta una persona,
#che possiede gli attributi di istanza nome e età.
#Ora crea una classe che rappresenta un regista,
#che eredita dalla classe persona,
#e possiede un attributo di istanza in più
#che indica un film famoso che ha girato.

#Istanzia un oggetto della superclasse,
#poi un oggetto della sottoclasse,
#e verifica quali attributi
#sono accessibili su di essi.

#Alle classi dell'esercizio precedente,
#aggiungi un metodo.
#La classe Persona dovrà avere un metodo
#che le permetta di presentarsi,
#stampando a schermo i valori dei propri attributi.
#La sottoclasse dovrà fare
#un override di tale metodo,
#per stampare a schermo un messaggio diverso,
#che contenga il valore del suo
#attributo specifico (film famoso).

# class Giorge:
#     def __init__(self,name,age,):
#         self.name = name
#         self.age = age
#     def process(self):
#         print(f"il mio nome e {self.name} e ho {self.age}")

# class Regista(Giorge):
#     def __init__(self,name,age,film):
#         super().__init__(name,age)
#         self.film = film

#     def process(self):  
#         print(f"il mio nome e {self.name} e ho {self.age} e ho fatto {self.film}")

# giorge=Giorge("giorge",22)
# giorge.process()

# regista=Regista("giorge",22,"la vita e bella")
# regista.process()

# print(giorge.name)


#  Definisci una lista che contenga 3 mete turistiche.
# Stampale tutte a schermo e chiedi all'utente
# dove desidera andare.
# Per scegliere, dovrà immettere
# l'indice dell'elemento della lista,
# in questo caso un numero da 0 a 2.
# Stampa a schermo un augurio di buon viaggio,
# contenente la destinazione scelta.

# Lancia il programma e tenta di farlo andare in errore,
# così da trovare le eccezioni che potrebbero
# verificarsi nel processo.
# INDIZIO: Dovresti trovare due principali eccezioni.
# Con un blocco try costituito da due rami except,
# gestisci le due eccezioni.

# car_price:20_000
# try:
#  moths =int(input("in quanti mesi vuoi pagare?"))
#  monthly_payment = car_price / moths
#  print(monthly_payment)
# except ValueError:
#     print("devi inserire un numero intero")
# except ZeroDivisionError:
#     print("devi inserire un numero diverso da 0") 

# Aggiungi all'esercizio precedente,
# un ulteriore funzionalità di gestione errori.
# Se l'utente inserisce un numero negativo,
# il programma DEVE andare in errore!
# Perciò, in questo caso, solleva (col comando raise),
# un eccezione ValueError o una IndexError,
# quella che ti sembra più appropriata.
# Senza fare nessun altra modifica,
# prova a lanciare il programma
# e inserire un numero negativo;
# il blocco try-except dovrebbe gestirlo come atteso.


# Turistic_met=["roma","milano","napoli","costarica","venezia","Palermo","Bora-Bora","Parigi","new-york","Tokio"]
# for i, met in enumerate(Turistic_met):
#     print(i,met,sep="_")

# try:    
#     selected_index=int(input("in che mete turistiche vuoi andare?🌍🎉 "))
#     selected_met=Turistic_met[selected_index]
#     print(f"buon viaggio   a ✈️  {selected_met}  ✈️  felice di essere stato d'aiuto ")
# except ValueError:
#     print("devi inserire un numero intero")    
# except IndexError:
#     print("Errore:destinazione inesistente ",
#           f"Inserisci un numero da 0 a {len(Turistic_met)-1}")
# if (selected_index<0):
#     raise Exception("non si accettano numeri negativi grazie   🛑 Nessun viaggio verso il passato!") 


 
# destinazioni = ["Stintino", "Viareggio", "Favignana"]
# print("🌍 Dove ti porterà il tuo prossimo pellegrinaggio? Ecco le destinazioni che abbiamo pensato per te:")
# indice = 0
# for destinazione in destinazioni:
#     print(f"{indice}: {destinazione}")
#     indice += 1
# try:
#     choice = int(input("✈️ Inserisci il numero della tua meta preferita (0-2): "))
#     if choice < 0:
#         raise ValueError("Oh no! Sembra che tu abbia scelto un numero negativo. 🛑 Nessun viaggio verso il passato!")

#     print(f"🎉 Hai scelto {destinazioni[choice]}! Prepara le valigie, il mare e l’avventura ti aspettano! 🏖️ Buon viaggio! 🪁")
    
# except ValueError as ve:
#     print(f"⚠️ Ops, qualcosa è andato storto: {ve}")
#     print("🐪 Dai, riproviamo insieme: scegli un numero valido tra 0 e 2. 🐪")
# except IndexError:
#     print("🚫 Ooops! Sembra che quella destinazione sia un po' troppo lontana dalla realtà. 😅 Prova con un numero tra 0 e 2!")
# except Exception as e:
#     print(f"🔍 Hmm, qualcosa di inaspettato è successo: {e}. Ma non preoccuparti, riproviamo insieme! 🌊😉")


# Nell'esercizio precedente,
# se il numero inserito è negativo,
# solleva un'eccezione più appropriata.
# Crea un eccezione utente, con un nome appropriato,
# tramite una classe che eredita da Exception
# e assegnale un messaggio d'errore personalizzato.
# Ora sollevala col comando raise,
# al posto di quella precedente.
# Infine, gestisci questa nuova eccezione,
# con un nuovo ramo except.




# class NegativeDestinationError(Exception):
#     def __init__(self):
#         super().__init__("Il numero della destinazione non può essere negativo!")

# travel_spots = ["Sudafrica", "Brasile", "Indonesia"]
# for i, spot in enumerate(travel_spots):
#     print(i, spot, sep="-")

# try:
#     selected_index = int(input("Dove desideri andare? "))
#     if selected_index < 0:
#         raise NegativeDestinationError
#     selected_spot = travel_spots[selected_index]
# except ValueError:
#     print("Errore: inserisci un numero intero!")
# except NegativeDestinationError as e:
#     print(e)
# except IndexError:
#     print(
#         "Errore: destinazione inesistente!",
#         f"Inserisci un numero da 0 a {len(travel_spots) - 1}",
#     )
# else:
#     print(f"Buon viaggio in {selected_spot}")


#  Scrivi un programma che chiede all'utente
# il nome di un social network che utilizza abitualmente
# e la relativa password di accesso.
# Il programma, a questo punto, apre un file
# e scrive al suo interno una riga
# contenente social e password,
# magari separati da un = o un altro carattere a piacere.
# Attenzione: ogni volta che il programma viene riavviato,
# ed i nuovi social e password vengono inseriti,
# la nuova riga che li conterrà dev'essere AGGIUNTA al file.

# with open("lista della spesa.txt","w",encoding="utf-8") as file:
#     file.write(item_to_buy)

social_network = input()
password = input()

with open("social_networks.txt", "a") as file:
  file.write(f"{social_network}={password}\n")


#   Modifica il programma precedente,
# aggiungendo la funzionalità di lettura.
# All'avvio, il programma chiede all'utente
# se desidera aggiungere un nuovo social e password,
# o se desidera leggere quelli già presenti.
# Se desidera aggiungere, procedi come in precedenza.
# Se desidera leggere, apri il file in lettura,
# e stampa a schermo ognuna delle righe
# contenenti social e password,
# precedute da un trattino o un altro carattere a piacere.


FILENAME = "social_passwords.txt"


def add_social_psw():
    social = input("Inserisci il nome del social: ")
    password = input(f"Inserisci la password per {social}: ")

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{social}={password}\n")

    print("Elemento aggiunto!")


def read_social_psw(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            print("🔐", line.strip())


user_choice = input("Ciao, desisderi aggiungere o leggere? (a/l)")
if user_choice == "a":
    add_social_psw()
elif user_choice == "l":
    read_social_psw(FILENAME)
else:
    print("Scelta non valida!")

#  Converti in un file json,
# il file di testo generato,
# negli esercizi precedenti
# (non alterare l'originale).
# Inizialmente crea un dizionario vuoto,
# quindi apri il file di testo in lettura
# accedi ciclicamente ad ognuna delle righe,
# e dividila (metodo split)
# per ottenere chiave (social) e valore (password).
# Aggiungi al dizionario ciascuna coppia chiave-valore.
# Infine, apri un nuovo file in scrittura,
# e scrivi il dizionario su di esso,
# serializzandolo col metodo json.dump.