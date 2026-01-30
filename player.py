import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.pos = pos
        self.image.fill("Red")
        self.rect = self.image.get_rect(center = pos)
        self.target = self.pos

    def set_target(self, target):
        self.target = target

    def move(self):
        if self.target != self.pos:
            target_vector = pygame.math.Vector2(self.target[0], self.target[1])
            position_vector = pygame.math.Vector2(self.pos[0], self.pos[1])
            direction = target_vector - position_vector

            if direction.length() < 6:
                self.pos = self.target
            else:
                if direction.length() != 0:
                    direction = direction.normalize()
                
                new_pos = position_vector + direction * 5
                self.pos = (math.ceil(new_pos.x), math.ceil(new_pos.y))
            
        self.rect.center = self.pos
    
    def set_pos(self, pos):
        self.pos = pos

    def update(self):
        self.move()