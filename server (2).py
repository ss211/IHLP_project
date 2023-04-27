import socket
import random


cards = [(value, suit) for value in range(1,14) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]


random.shuffle(cards)


clients = []
client_scores = {}

server_scores = {'Client 1': 0, 'Client 2': 0, 'Client 3': 0}


server_socket = socket.socket()
host = '127.0.0.2'
port = 3002
print('Waiting for clients connection response')

server_socket.bind((host, port))

server_socket.listen(3)


for i in range(3):
    conn, addr = server_socket.accept()
    clients.append(conn)
    client_scores[conn] = 0
    print("Connected to client " + str(i+1))


for round_num in range(1,14):
    print("Round " + str(round_num))

   
    server_card = cards.pop()

    
    for conn in clients:
        conn.send(str(server_card).encode())
    
    
    client_cards = {}

    for conn in clients:
            card = conn.recv(1024).decode()
            try:
                card_value = eval(card)
                client_cards[conn] = card_value
            except SyntaxError:
                print("Invalid card format received from client:", card)

        
    winning_card_value = max(client_cards.values())

    print(winning_card_value)
    winners = [k for k, v in client_cards.items() if v == winning_card_value]
    if len(winners) == 1:
        winner = winners[0]
        winning_card = client_cards[winner]
        client_scores[winner] + winning_card_value
        print("Winner: Client " + str(clients.index(winner)+1))
    elif len(winners) == 2:
        for winner in winners:
            winning_card = client_cards[winner]
            client_scores[winner] += winning_card_value
        print("Winners: Clients " + str(clients.index(winners[0])) + " and " + str(clients.index(winners[1])))
    else:
        for conn in clients:
            client_scores[conn] += winning_card_value
        print("All players tied")

   
    for i, client in enumerate(clients):
        server_scores['Client ' + str(i+1)] = client_scores[client]

    print("Server Score Card:")
    for key, value in server_scores.items():
        print(key + ": " + str(value))

winning_score = max(server_scores.values())
winners = [k for k, v in server_scores.items() if v == winning_score]
if len(winners) == 1:
    winner = winners[0]
    print("The winner is " + winner)
    for conn in clients:
        conn.send(("The winner is " + winner).encode())
elif len(winners) == 2:
    print("There is a tie between " + winners[0] + " and " + winners[1])
    for conn in clients:
        conn.send(("There is a tie between " + winners[0] + " and " + winners[1]).encode())
else:
    print("All players tied")
