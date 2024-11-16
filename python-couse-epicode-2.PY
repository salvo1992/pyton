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
class Giorge:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    def process(self):
        print(f"il mio nome e {self.name} e ho {self.age}")

class Regista(Giorge):
    def __init__(self,name,age,film):
        super().__init__(name,age)
        self.film = film

    def process(self):  
        print(f"il mio nome e {self.name} e ho {self.age} e ho fatto {self.film}")

giorge=Giorge("giorge",22)
giorge.process()

regista=Regista("giorge",22,"la vita e bella")
regista.process()

print(giorge.name)


