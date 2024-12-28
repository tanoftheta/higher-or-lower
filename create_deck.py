import random
import pygame
import os 

class Card(object):
    def __init__(self, suit, rank, card_width, card_height): 
        self.suit = suit
        self.rank = rank
        self.x = 0
        self.y = 0
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('card_images', f"{suit}_{rank}.PNG")), (card_width, card_height))
        self.is_selected = False

    def get_card_value(self):
        if self.rank == "a":
            return 1
        elif self.rank == "j":
            return 11
        elif self.rank == "q":
            return 12
        elif self.rank == "k":
            return 13
        else:
            return int(self.rank)

class Deck(object):
    def __init__(self, card_width, card_height):
        self.deck = self.createDeck(card_width, card_height)
        self.remaining_cards = len(self.deck)
        self.active_cards = []
        self.card_width = card_width
        self.card_height = card_height

    def createDeck(self, card_width, card_height):
        suits = ["clubs", "diamonds", "spades", "hearts"]
        ranks = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
        deck = [Card(suit, rank, card_width, card_height) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def setTable(self):
        self.active_cards = self.deck[:9]
        del self.deck[:9]
        self.remaining_cards = len(self.deck)
    
    def draw(self, window):
        window_width = window.get_size()[0]
        window_height = window.get_size()[1]
        horizontal_white_space = (window_width - self.card_width * 3) / 4
        vertical_white_space = (window_height - self.card_height * 3) / 4
        for index, card in enumerate(self.active_cards):
            x_pos = (index % 3) * (horizontal_white_space + self.card_width) + horizontal_white_space
            y_pos = (index // 3) * (vertical_white_space + self.card_height) + 5
            if card.is_selected:
                selected_rect = pygame.Rect(x_pos - 5, y_pos - 5, self.card_width + 10, self.card_height + 10)
                pygame.draw.rect(window, (255, 0, 0), selected_rect)
            window.blit(card.image, (x_pos, y_pos))
            card.x = x_pos
            card.y = y_pos

    def checkCardClick(self, mouse_x, mouse_y):
        for card in self.active_cards:
            card.is_selected = False
            if (card.x <= mouse_x <= card.x + self.card_width) and (card.y <= mouse_y <= card.y + self.card_height):
                print(f"Card clicked: {card.rank} of {card.suit}")
                card.is_selected = True
                return card
        return None

    def checkBet(self, card, bet):
        challenge_value = card.get_card_value()
        real_value = self.deck[0].get_card_value()
        is_right = True
        if bet == "h":
            if challenge_value <= real_value:
                print("You're right! The next card is ", self.deck[0].rank)
            else:
                print("You're wrong! The next card is ", self.deck[0].rank)
                is_right = False
        if bet == 'l':
            if challenge_value < real_value:
                print("You're wrong. The next card is ", self.deck[0].rank)
                is_right = False
            else:
                print("You're right! The next card is ", self.deck[0].rank)
        card.is_selected = False

def main():
    game_table = Deck(48, 64)
    game_table.setTable()
    print("Active cards:")
    for index, card in enumerate(game_table.active_cards):
        print(f"{index} {card.rank}")
    incorrect = 0
    while incorrect < 9:
        challenge_num = int(input("What card will you challenge?"))
        bet = input("Will you go higher or lower?")
        game_table.checkBet(game_table.active_cards[challenge_num], bet)


if __name__ == "__main__":
    main()
