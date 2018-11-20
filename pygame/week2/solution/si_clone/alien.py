import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.game = game
        self.screen = game.getScreen()
        self.settings = game.getSettings()

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self, elapsedMs):
        """Move the alien right or left."""
        self.x += (elapsedMs * self.settings.alien_speed_factor *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def draw(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)