import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank["rank"]} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards= []
        suits =  ["spades","clubs","hearts","diamonds"]
        ranks = [{"rank": "A" , "value": 1},
                {"rank": "2" , "value": 2},
                {"rank": "3" , "value": 3},
                {"rank": "4" , "value": 4},
                {"rank": "5" , "value": 5},
                {"rank": "6" , "value": 6},
                {"rank": "7" , "value": 7},
                {"rank": "8" , "value": 8},
                {"rank": "9" , "value": 9},
                {"rank": "J" , "value": 10},
                {"rank": "Q" , "value": 10},
                {"rank": "K" , "value": 10}]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self, number):
        cards_dealth = []
        for n in range( number):
            card = self.cards.pop()
            cards_dealth.append(card)
        return cards_dealth

class Hand():
    def __init__ (self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, list_card):
        self.cards.extend(list_card)

    def calculate_value(self):
        self.value = 0
        for card in self.cards:
            card_value = card.rank["value"]
            self.value += card_value
        return self.value
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def display(self, show_all_cards = False):
        print( f'''{"dealer's" if self.dealer else "Yours"}''')
        for card in self.cards:
            if self.dealer and not show_all_cards:
                print ("Hidden")
            else:
                print (card)
        if not self.dealer:    
            print ("Value:", self.get_value())
            


class Game:
    def play(self):
        game_played = 0
        game_required = 0
        player_win = 0
        dealer_win = 0
        while True:
            try:   
                game_required = int(input("number of game to play: "))
                break
            except:
                print( "This requires a number")

        while game_played < game_required:
            game_played+=1
            deck = Deck()
            deck.shuffle()
            hand_player = Hand()
            hand_dealer = Hand(True)
            for n in range (2):
                hand_player.add_card(deck.deal(1))
                hand_dealer.add_card(deck.deal(1))

            print ()
            print ("*" * 30)
            print (f"{game_played} out of {game_required}")
            print( "player_score: ", player_win,"\n", "dealer_score: ", dealer_win, sep="")
            print ("*" * 30)
            hand_player.display()
            print ()
            hand_dealer.display()
            print()
            hits = ""
            while hits not in ["s", "stand"] and len(hand_player.cards)<3:
                hits = input ("please enter Hit / Stand or (S/H) ").lower()
                while hits not in ["h","hit","s", "stand"]:
                    hits = input ("please enter Hit / Stand or (S/H) ").lower()
                if hits in ["h","hit"]:
                    hand_player.add_card(deck.deal(1))
                    hand_player.display()
                    print()
                else:
                    hand_player.display()
                    print()          

            if hand_dealer.get_value()<16:
                hand_dealer.add_card(deck.deal(1))
                hand_dealer.display(True)
                print( "Value:", hand_dealer.get_value())
            else:
                hand_dealer.display(True)
                print( "Value:", hand_dealer.get_value()) 
            self.check_winner(hand_player, hand_dealer, True)
            hand_player_value = hand_player.get_value()%10
            hand_dealer_value = hand_dealer.get_value()%10
            if hand_player_value > hand_dealer_value:
                player_win += 1
            elif hand_player_value < hand_dealer_value:
                dealer_win += 1
            print ("player:", player_win, "dealer:", dealer_win)
        print (f'''{"Player Win" if player_win > dealer_win else "Dealer Win"} ''')


    def check_winner(self, hand_player1, hand_dealer1, game_over = False):
        hand_player = hand_player1.get_value()%10
        hand_dealer = hand_dealer1.get_value()%10
        if not game_over:
            pass
        else:
            if hand_player > hand_dealer:
                print ("You Win")
            elif hand_player < hand_dealer:
                print ("You loss")
            elif hand_player == hand_dealer:
                print ("its a tie")

        



game = Game()
game.play()





