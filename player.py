import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, velocity=5, environment=None):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.pos = pos
        self.image.fill("Red")
        self.rect = self.image.get_rect(center = pos)
        self.target = self.pos
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = velocity
        self.environment = environment

    def set_target(self, target):
        self.target = target

    def move(self):
        # checks if the player is not at the target
        if self.target != self.pos:

            # calculates the direction vector
            target_vector = pygame.math.Vector2(self.target[0], self.target[1])
            position_vector = pygame.math.Vector2(self.pos[0], self.pos[1])
            self.direction = target_vector - position_vector
                        
            
            # moves the player towards the target if he is close enough
            if self.direction.length() < 6:
                self.pos = self.target
                # collision detection
                if self.environment:
                    for environment in self.environment:
                        if environment.rect.collidepoint(self.target):
                            self.target = self.pos
            else: # moves the player towards the target according to his velocity
                if self.direction.length() != 0:
                    self.direction = self.direction.normalize()

                new_position_vector = position_vector + self.direction * self.velocity
                new_position = pygame.math.Vector2(new_position_vector.x, new_position_vector.y)
                if self.environment:
                    collision = False
                    for environment in self.environment:
                        if environment.rect.collidepoint(new_position.x + self.rect.width / 2, new_position.y + self.rect.height / 2) or environment.rect.collidepoint(new_position.x - self.rect.width / 2, new_position.y - self.rect.height / 2) or environment.rect.collidepoint(new_position.x + self.rect.width / 2, new_position.y - self.rect.height / 2) or environment.rect.collidepoint(new_position.x - self.rect.width / 2, new_position.y + self.rect.height / 2):
                            collision = True
                    if not collision:
                        self.pos = (new_position.x, new_position.y)
                    else:
                        self.target = self.pos
                else:
                    self.pos = (new_position.x, new_position.y)
            
        self.rect.center = self.pos
    
    def set_pos(self, pos):
        self.pos = pos

    def update(self):
        self.move()