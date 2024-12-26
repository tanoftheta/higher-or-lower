import random

class GameTable(object):
    def __init__(self):
        self.deck = self.createDeck()
        self.remaining_cards = len(self.deck)
        self.active_cards = []

    def createDeck(self):
        suits = ["clubs", "diamonds", "spades", "hearts"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def setTable(self):
        self.active_cards = self.deck[:9]
        del self.deck[:9]
        self.remaining_cards = len(self.deck)
    
    def get_card_value(self, card):
        if card["rank"] == "A":
            return 1
        elif card["rank"] == "J":
            return 11
        elif card["rank"] == "Q":
            return 12
        elif card["rank"] == "K":
            return 13
        else: 
            return int(card["rank"])
        
    def checkBet(self, card, bet):
        challenge_value = self.get_card_value(card)
        real_value = self.get_card_value(self.deck[0])
        is_right = True
        if bet == "h":
            if challenge_value < real_value:
                print("You're right! The next card is ", self.deck[0])
            else:
                print("You're wrong! The next card is ", self.deck[0])
                is_right = False
        if bet == 'l':
            if challenge_value < real_value:
                print("You're wrong. The next card is ", self.deck[0])
                is_right = False
            else:
                print("You're right! The next card is ", self.deck[0])

def main():
    game_table = GameTable()
    game_table.setTable()
    print("Active cards:")
    for index, card in enumerate(game_table.active_cards):
        print(f"{index} {card}")
    incorrect = 0
    while incorrect < 9:
        challenge_num = int(input("What card will you challenge?"))
        bet = input("Will you go higher or lower?")
        game_table.checkBet(game_table.active_cards[challenge_num], bet)


if __name__ == "__main__":
    main()
