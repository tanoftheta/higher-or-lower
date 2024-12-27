import pygame
from deck_stack import deckStack
pygame.font.init()

text = pygame.font.Font('slkscr.ttf', 20)
WIDTH, HEIGHT = 360, 360
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 255, 0))
pygame.display.set_caption("Higher or Lower?") 

def game_over_screen(cards_left):
    WINDOW.fill((0,0,0))
    gameover_text = text.render("GAME OVER", 1, (255, 0,0))
    cards_left_text = text.render("Cards left: " + str(cards_left), 1, (0, 0, 0))
    WINDOW.blit(gameover_text, (WIDTH//2 - gameover_text.get_width()//2, HEIGHT//2 - gameover_text.get_height()))
    WINDOW.blit(cards_left_text, (WIDTH//2 - cards_left_text.get_width()//2, HEIGHT//2 - gameover_text.get_height() + 10 + cards_left_text.get_height()))
    restart_text = text.render("CLICK SCREEN TO RESTART", 1, (255, 255, 255))
    WINDOW.blit(restart_text, (WIDTH//2- restart_text.get_width()//2, 300))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] == 1:
        runGame()

def win_screen(): 
    win_text = text.render("YOU WIN!", 1, (255, 255, 255))
    restart_text = text.render("CLICK SCREEN TO PLAY AGAIN", 1, (255, 255, 255))
    WINDOW.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()))
    WINDOW.blit(restart_text, (WIDTH//2- restart_text.get_width()//2, 300))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] == 1:
        runGame()

def window(active_stacks, cards_left, deck_stack):
    if cards_left == 0: 
        win_screen()
    elif active_stacks > 0:
        cards_left_text = text.render("cards left: " + str(cards_left), 1, (255, 255, 255))
        WINDOW.blit(cards_left_text, (10, HEIGHT-20))
        WINDOW.blit(deck_stack.image, (deck_stack.x, deck_stack.y))
        pygame.display.update()
    else:
        game_over_screen(cards_left)


def runGame():
    deck_stack = deckStack(48, 64, WIDTH, HEIGHT)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window(4, 9, deck_stack)
    pygame.quit()

if __name__ == "__main__":
    runGame()