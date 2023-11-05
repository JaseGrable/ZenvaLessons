import pygame
from gameObject import GameObject
from player import Player
# Importing the Enemy class
from enemy import Enemy


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
        self.player = Player(280, 530, 40, 40, 'assets/player.png', 1)

        self.enemy = Enemy(0, 450, 40, 40, 'assets/enemy.png', 5)

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

        self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y))

        pygame.display.update()

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        return True

    def run_game_loop(self):
        player_direction = 0

        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:
                # If there's a QUIT event, we break the loop and exit the method
                if event.type == pygame.QUIT:
                    return

                # Listening for when a key is pressed down on the keyboard
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1

                # Stopping the player when arrow keys are released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            # Execute logic
            self.player.move(player_direction, self.height)
            # Moving the enemy
            self.enemy.move(self.width)

            # Update display
            self.draw_objects()

            # Detect Collisions
            if self.detect_collision(self.player, self.enemy):
                return
            elif self.detect_collision(self.player, self.treasure):
                return

            self.clock.tick(60)
