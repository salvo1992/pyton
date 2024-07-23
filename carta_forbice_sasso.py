#print('benvenuti  al nuovo gioco python carta forbici sasso ')
#print('e il vostro turno scrivi la tua scelta ')

#scelta_gioco = input('scrivi "carta", "forbici" o "sasso": ')

#import random
#scelte_computer = ['carta', 'forbici', 'sasso']
#scelta_computer = random.choice(scelte_computer)
#print('il computer ha scelto ', scelta_computer)

#if scelta_gioco == scelta_computer:
   
#    print('pareggio!')
   


#    if scelta_gioco == 'carta': scelta_computer == 'sasso'
#    print('hai vinto')


#    if scelta_gioco == 'sasso': scelta_computer == 'forbici'
#    print('hai vinto')

    
#    if scelta_gioco == 'forbici': scelta_computer == 'carta'
#    print('hai vinto')
#else:print('hai perso')



   
import random

SCELTE = ['carta', 'forbici', 'sasso']

print('Benvenuto al gioco!')

nome_giocatore = input('Per favore, inserisci il tuo nome: ')

# Chiedere il numero di partite che il giocatore vuole giocare
try:
    numero_partite = int(input(f'{nome_giocatore}, scegli quante partite vuoi giocare: '))
except ValueError:
    print('Numero non valido, per favore inserisci un numero intero.')
    numero_partite = 1

# Chiedere se il giocatore vuole utilizzare la modalità invincibile
modalita_invincibile = input('Vuoi attivare la modalità invincibile? (sì/no): ').lower() == 'sì'

punti_giocatore = 0
punti_computer = 0

for i in range(numero_partite):
    scelta_giocatore = input(f'{nome_giocatore}, scegli tra carta, forbici, sasso: ').lower()

    if scelta_giocatore not in SCELTE:
        print('Scelta non valida, riprova.')
    else:
        if modalita_invincibile:
            # In modalità invincibile, il giocatore vince sempre
            scelta_computer = random.choice([scelta for scelta in SCELTE if scelta != scelta_giocatore])
        else:
            scelta_computer = random.choice(SCELTE)
        
        print(f'{nome_giocatore} ha scelto {scelta_giocatore}')
        print(f'Il computer ha scelto {scelta_computer}')

        if scelta_giocatore == scelta_computer:
            print('Pareggio!')
        elif modalita_invincibile or (scelta_giocatore == 'carta' and scelta_computer == 'sasso') or \
             (scelta_giocatore == 'forbici' and scelta_computer == 'carta') or \
             (scelta_giocatore == 'sasso' and scelta_computer == 'forbici'):
            print(f'{nome_giocatore} ha vinto!')
            punti_giocatore += 1
        else:
            print('Il computer ha vinto!')
            punti_computer += 1

print(f'\nPunti finali:')
print(f'{nome_giocatore}: {punti_giocatore}')
print(f'Computer: {punti_computer}')

if punti_giocatore > punti_computer:
    print(f'Complimenti, {nome_giocatore}! Hai vinto la serie di partite.')
elif punti_giocatore < punti_computer:
    print(f'Il computer ha vinto la serie di partite. Meglio fortuna la prossima volta, {nome_giocatore}.')
else:
    print('La serie di partite è terminata in pareggio.')

print(f'Grazie e alla prossima, {nome_giocatore}!')
