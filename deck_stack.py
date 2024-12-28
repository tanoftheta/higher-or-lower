import os
import pygame

class deckStack(object):
    def __init__(self, width, height, window_width, window_height):
        self.width = width
        self.height = height
        self.x = window_width // 2 - width // 2
        self.y = window_height // 2 - height // 2
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('card_images', 'back.PNG')), (width, height))
        self.target_y = window_height - height - 10
        self.target_x = window_width - width - 20
        self.speed = 4 
        self.animating = True
        self.start_time = pygame.time.get_ticks()

    def animate(self, WIDTH, HEIGHT):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if elapsed_time < 1500:
            self.x = WIDTH // 2 - self.width // 2
            self.y = HEIGHT // 2 - self.height // 2

        if self.y < self.target_y:
            self.y += self.speed 
            if self.y > self.target_y:
                self.y = self.target_y
        if self.x < self.target_x:
            self.x += self.speed 
            if self.x > self.target_x:
                self.x = self.target_x
        else:
            self.animating = False
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
