import os
import pygame

class deckStack(object):
    def __init__(self, width, height, window_width, window_height):
        self.x = window_width // 2 - width // 2
        self.y = window_height // 2 - height // 2
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('card_images', 'back.PNG')), (width, height))