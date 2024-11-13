import random

# Definizione delle carte
suits = ['Coppe', 'Denari', 'Spade', 'Bastoni']
ranks = ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Fante', 'Cavallo', 'Re']
points = {'Asso': 11, 'Due': 0, 'Tre': 10, 'Quattro': 0, 'Cinque': 0, 'Sei': 0, 'Sette': 0, 'Fante': 2, 'Cavallo': 3, 'Re': 4}

# Creazione del mazzo
def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Distribuzione delle carte
def deal_cards(deck):
    return deck[:3], deck[3:6], deck[6], deck[7:]  # mano giocatore 1, mano giocatore 2, briscola, mazzo rimanente

# Mostra la mano del giocatore
def show_hand(player_hand, player_number):
    print(f"Mano Giocatore {player_number}: {', '.join([f'{rank} di {suit}' for rank, suit in player_hand])}")

# Giocare un turno
def play_turn(player_hand, opponent_hand, briscola):
    print(f"\nBriscola: {briscola[0]} di {briscola[1]}")
    show_hand(player_hand, 1)

    # Scegli una carta da giocare
    card = int(input("Scegli una carta da giocare (1-3): ")) - 1
    chosen_card = player_hand[card]

    print(f"Hai giocato: {chosen_card[0]} di {chosen_card[1]}")

    # Giocatore avversario gioca una carta casuale
    opponent_card = random.choice(opponent_hand)
    print(f"Giocatore 2 ha giocato: {opponent_card[0]} di {opponent_card[1]}")

    # Logica per determinare chi vince il turno
    if chosen_card[1] == briscola[1]:
        if opponent_card[1] == briscola[1]:
            if points[chosen_card[0]] > points[opponent_card[0]]:
                print("Hai vinto il turno!")
                return chosen_card, opponent_card
            else:
                print("Giocatore 2 ha vinto il turno!")
                return opponent_card, chosen_card
        else:
            print("Hai vinto il turno!")
            return chosen_card, opponent_card
    elif opponent_card[1] == briscola[1]:
        print("Giocatore 2 ha vinto il turno!")
        return opponent_card, chosen_card
    else:
        if ranks.index(chosen_card[0]) > ranks.index(opponent_card[0]):
            print("Hai vinto il turno!")
            return chosen_card, opponent_card
        else:
            print("Giocatore 2 ha vinto il turno!")
            return opponent_card, chosen_card

# Calcolo punteggio
def calculate_score(played_cards):
    return sum(points[card[0]] for card in played_cards)

# Gioco
def play_game():
    player1_score = 0
    player2_score = 0
    total_games = 2  # Numero di partite da giocare
    game_count = 1  # Contatore delle partite

    while game_count <= total_games:
        print(f"\nInizio partita {game_count}:")
        deck = create_deck()
        player1_hand, player2_hand, briscola, remaining_deck = deal_cards(deck)

        played_cards_p1 = []
        played_cards_p2 = []

        while remaining_deck or player1_hand or player2_hand:
            print("\nNuovo turno:")
            played_cards = play_turn(player1_hand, player2_hand, briscola)

            # Rimuovi le carte giocate dalle mani
            played_cards_p1.append(played_cards[0])
            played_cards_p2.append(played_cards[1])
            player1_hand.remove(played_cards[0])
            player2_hand.remove(played_cards[1])

            # Calcola il punteggio del turno
            if played_cards[0] == played_cards_p1[-1]:
                player1_score += calculate_score([played_cards[0]])
            else:
                player2_score += calculate_score([played_cards[1]])

            # Pesca nuove carte
            if remaining_deck:
                if len(player1_hand) < 3:
                    player1_hand.append(remaining_deck.pop(0))
                if len(player2_hand) < 3:
                    player2_hand.append(remaining_deck.pop(0))

        print("\nGioco finito!")
        print(f"Punteggio Partita {game_count}: Giocatore 1 = {player1_score}, Giocatore 2 = {player2_score}")

        if player1_score > player2_score:
            print("Giocatore 1 ha vinto la partita!")
        elif player2_score > player1_score:
            print("Giocatore 2 ha vinto la partita!")
        else:
            print("La partita è finita in pareggio!")

        # Resettare i punteggi per la prossima partita
        player1_score = 0
        player2_score = 0
        game_count += 1

    # Determina il vincitore finale
    if player1_score > player2_score:
        print("Giocatore 1 ha vinto il gioco finale!")
    elif player2_score > player1_score:
        print("Giocatore 2 ha vinto il gioco finale!")
    else:
        print("Il gioco finale è finito in pareggio!")

# Avvia il gioco
play_game()
