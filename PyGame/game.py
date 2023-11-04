import pygame
from gameObject import GameObject
# Importing the Player class
from player import Player


class Game:

    def __init__(self):
        self.width = 600
        self.height = 600
        self.white_colour = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        # Loading the game assets
        # NOTE: We're using different values and image paths here specifically for the Trinket application
        self.background = GameObject(
            0, 0, self.width, self.height, 'assets/background.png')
        self.treasure = GameObject(280, 35, 40, 40, 'assets/treasure.png')

        # Creating the Player asset
        self.player = Player(280, 530, 40, 40, 'assets/player.png', 10)

        self.clock = pygame.time.Clock()

    def draw_objects(self):
        self.game_window.fill(self.white_colour)

        # Blitting assets to the screen
        self.game_window.blit(self.background.image,
                              (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image,
                              (self.treasure.x, self.treasure.y))

        self.game_window.blit(
            self.player.image, (self.player.x, self.player.y))

        pygame.display.update()

    def run_game_loop(self):

        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:
                # If there's a QUIT event, we break the loop and exit the method
                if event.type == pygame.QUIT:
                    return

            # Execute logic
            # Update display
            self.draw_objects()

            self.clock.tick(60)
