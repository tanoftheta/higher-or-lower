import pygame
from deck_stack import deckStack
from create_deck import Deck
pygame.font.init()

text = pygame.font.Font('slkscr.ttf', 20)
WIDTH, HEIGHT = 360, 360
card_width, card_height = 48, 64
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 255, 0))
pygame.display.set_caption("Higher or Lower?")

def draw_higher_lower_buttons(button_width, button_height):
    lower_button_rect = pygame.Rect(
        WIDTH // 4 - button_width // 2, HEIGHT - 100, button_width, button_height
    )
    higher_button_rect = pygame.Rect(
        (WIDTH * 3) // 4 - button_width // 2, HEIGHT - 100, button_width, button_height
    )

    return higher_button_rect, lower_button_rect

def game_over_screen(cards_left):
    WINDOW.fill((0,0,0))
    gameover_text = text.render("GAME OVER", 1, (255, 0, 0))
    cards_left_text = text.render("Cards left: " + str(cards_left), 1, (0, 0, 0))
    WINDOW.blit(gameover_text, (WIDTH//2 - gameover_text.get_width()//2, HEIGHT//2 - gameover_text.get_height()))
    WINDOW.blit(cards_left_text, (WIDTH//2 - cards_left_text.get_width()//2, HEIGHT//2 - gameover_text.get_height() + 10 + cards_left_text.get_height()))
    restart_text = text.render("CLICK SCREEN TO RESTART", 1, (255, 255, 255))
    WINDOW.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 300))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] == 1:
        runGame()

def win_screen():
    win_text = text.render("YOU WIN!", 1, (255, 255, 255))
    restart_text = text.render("CLICK SCREEN TO PLAY AGAIN", 1, (255, 255, 255))
    WINDOW.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()))
    WINDOW.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 300))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] == 1:
        runGame()

def window(active_stacks, deck, deck_stack, waiting_for_bet, higher_button_rect=None, lower_button_rect=None):
    cards_left = deck.remaining_cards
    WINDOW.fill((0, 255, 0)) 

    if cards_left == 0:
        win_screen()
    elif active_stacks > 0:
        cards_left_text = text.render("cards left: " + str(cards_left), 1, (255, 255, 255))
        WINDOW.blit(cards_left_text, (10, HEIGHT - 20))
        deck_stack.draw(WINDOW)
        deck.draw(WINDOW)

        if waiting_for_bet and higher_button_rect and lower_button_rect:
            pygame.draw.rect(WINDOW, (0, 0, 255), lower_button_rect) 
            pygame.draw.rect(WINDOW, (255, 0, 0), higher_button_rect) 

            higher_text = text.render("Higher", True, (255, 255, 255))
            lower_text = text.render("Lower", True, (255, 255, 255))

            WINDOW.blit(higher_text, (higher_button_rect.x + (higher_button_rect.width - higher_text.get_width()) // 2,
                                      higher_button_rect.y + (higher_button_rect.height - higher_text.get_height()) // 2))
            WINDOW.blit(lower_text, (lower_button_rect.x + (lower_button_rect.width - lower_text.get_width()) // 2,
                                     lower_button_rect.y + (lower_button_rect.height - lower_text.get_height()) // 2))

    else:
        game_over_screen(cards_left)

    pygame.display.update() 


def runGame():
    deck_stack = deckStack(card_width, card_height, WIDTH, HEIGHT)
    deck = Deck(card_width, card_height)
    run = True
    table_unset = True
    waiting_for_bet = False
    clicked_card = None 
    higher_button_rect, lower_button_rect = None, None 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if not waiting_for_bet:
                        clicked_card = deck.checkCardClick(mouse_x, mouse_y)
                        if clicked_card:
                            waiting_for_bet = True
                            higher_button_rect, lower_button_rect = draw_higher_lower_buttons(100, 40)
                    else:
                        if higher_button_rect.collidepoint(mouse_x, mouse_y):
                            print("Player chose Higher!")
                            deck.checkBet(clicked_card, "h")
                            waiting_for_bet = False
                        elif lower_button_rect.collidepoint(mouse_x, mouse_y):
                            print("Player chose Lower!")
                            deck.checkBet(clicked_card, "l")
                            waiting_for_bet = False
        if deck_stack.animating:
            deck_stack.animate(WIDTH, HEIGHT)
        else:
            if table_unset:
                deck.setTable()
                table_unset = False

        window(9, deck, deck_stack, waiting_for_bet, higher_button_rect, lower_button_rect)
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    runGame()
