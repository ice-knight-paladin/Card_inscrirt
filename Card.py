import pygame
import resources


class Card:
    def __init__(self, text="images/error.jpg"):
        self.img = pygame.image.load(text)
        self.dm = resources.CARDS.get(text.split("/")[1])[1]
        self.hp = resources.CARDS.get(text.split("/")[1])[0]
        self.csle = pygame.transform.scale(self.img, (self.img.get_width() // 1.3, self.img.get_height() // 1.3))

    def atack(self):
        return self.dm

    def hpe(self):
        return self.hp

    def properties(self):
        pass
