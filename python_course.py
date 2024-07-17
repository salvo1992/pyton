ANNO_AVVIO_NEGOZIO=2024
veicolo_offerta='bici elettrica'
prezzo_offerta=190.90

biciclette=['montanbike','Graziella','BMX','triciclo']
motociclette=['Vespa','harley','Ciao','apixedda']

veicoli=biciclette
veicoli.append('tandem')


#for bicicletta in biciclette:
 #   print('-' + bicicletta)

#for idx,bicicletta in enumerate(biciclette):
   
print("benvenuti al negozio epic bikers!")
print("non perderti la nostra :"+veicolo_offerta)
print("provala al prezzo di $ "+ str(prezzo_offerta) +"dollari" )      
print(f"provala al prezzo di $ { prezzo_offerta }dollari" )        

print("inserisci il tuo anno di nascita ")
anno_nascita=int(input())
anno_cliente=2024-anno_nascita
print(anno_cliente)

if anno_cliente < 18:
    print('sei minorenne')
    veicoli=biciclette
else:    
    print('sei maggiorenne')
    veicoli=biciclette + motociclette

print(veicoli)
