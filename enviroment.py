import pygame

class Enviroment(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.world_pos = pos
        self.rect = self.image.get_rect(center=self.world_pos)
        self.target = self.world_pos

    def move(self, target):
        self.target = target

    def update(self):
        self.world_pos = self.world_pos
