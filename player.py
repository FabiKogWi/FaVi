import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface(50, 50)
        self.image.fill("Red")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        print("Update xD")