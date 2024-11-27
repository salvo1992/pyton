from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

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
    return deck[:3], deck[3:6], deck[6], deck[7:]

# Gioco completo
player1_score = 0
player2_score = 0
game_count = 0
player1_hand = []
player2_hand = []
remaining_deck = []
briscola = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global player1_score, player2_score, game_count, player1_hand, player2_hand, remaining_deck, briscola
    player1_score = 0
    player2_score = 0
    game_count = 0
    deck = create_deck()
    player1_hand, player2_hand, briscola, remaining_deck = deal_cards(deck)

    # Risposta con tutte le carte rappresentate come oggetti
    response = {
        'player1_hand': [{'rank': rank, 'suit': suit} for rank, suit in player1_hand],
        'player2_hand': [{'rank': rank, 'suit': suit} for rank, suit in player2_hand],
        'briscola': {'rank': briscola[0], 'suit': briscola[1]},
        'remaining_deck': [{'rank': rank, 'suit': suit} for rank, suit in remaining_deck]
    }
    return jsonify(response)

@app.route('/play_turn', methods=['POST'])
def play_turn_route():
    global player1_score, player2_score, player1_hand, player2_hand, remaining_deck, briscola

    data = request.get_json()
    chosen_card_index = data['chosen_card_index']

    # Scegli la carta del giocatore e dell'avversario
    if player1_hand:
        chosen_card = player1_hand.pop(chosen_card_index)
    else:
        return jsonify({'error': 'No cards left in player hand'}), 400

    if not player2_hand and remaining_deck:
        player2_hand.append(remaining_deck.pop(0))
    opponent_card = player2_hand.pop(0) if player2_hand else None

    # Verifica del formato delle carte e del rank
    if not chosen_card or not opponent_card or chosen_card[0] not in ranks or opponent_card[0] not in ranks:
        return jsonify({'error': f"Invalid card rank: {chosen_card} or {opponent_card}"}), 400

    # Logica di gioco: determinare chi vince il turno
    if chosen_card[1] == briscola[1]:
        if opponent_card[1] == briscola[1]:
            if points[chosen_card[0]] > points[opponent_card[0]]:
                winner = "Player wins the turn"
                player1_score += points[chosen_card[0]] + points[opponent_card[0]]
            else:
                winner = "Opponent wins the turn"
                player2_score += points[chosen_card[0]] + points[opponent_card[0]]
        else:
            winner = "Player wins the turn"
            player1_score += points[chosen_card[0]] + points[opponent_card[0]]
    elif opponent_card[1] == briscola[1]:
        winner = "Opponent wins the turn"
        player2_score += points[chosen_card[0]] + points[opponent_card[0]]
    else:
        if ranks.index(chosen_card[0]) > ranks.index(opponent_card[0]):
            winner = "Player wins the turn"
            player1_score += points[chosen_card[0]] + points[opponent_card[0]]
        else:
            winner = "Opponent wins the turn"
            player2_score += points[chosen_card[0]] + points[opponent_card[0]]

    # Pesca una carta per ogni giocatore se ci sono ancora carte nel mazzo
    if remaining_deck:
        if len(player1_hand) < 3 and remaining_deck:
            player1_hand.append(remaining_deck.pop(0))
        if len(player2_hand) < 3 and remaining_deck:
            player2_hand.append(remaining_deck.pop(0))

    # Controlla se la partita deve finire
    if player1_score >= 120 or player2_score >= 120 or not remaining_deck:
        game_count += 1
        if player1_score >= 120:
            winner = "Player wins the game!"
        elif player2_score >= 120:
            winner = "Opponent wins the game!"
        else:
            winner = "Game over, no more cards left."

        if game_count >= 2 or player1_score >= 120 or player2_score >= 120:
            game_over = True
        else:
            game_over = False
    else:
        game_over = False

    # Risposta con il risultato del turno e il punteggio aggiornato
    response = {
        'result': winner,
        'chosen_card': f'{chosen_card[0]} di {chosen_card[1]}',
        'opponent_card': f'{opponent_card[0]} di {opponent_card[1]}',
        'remaining_deck': [{'rank': card[0], 'suit': card[1]} for card in remaining_deck],
        'player1_hand': [{'rank': card[0], 'suit': card[1]} for card in player1_hand],
        'opponent_hand': [{'rank': card[0], 'suit': card[1]} for card in player2_hand],
        'player1_score': player1_score,
        'player2_score': player2_score,
        'game_over': game_over
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)




