# These buttons serve as a template for all of the buttons in the game
import pygame

class TextButton(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, font_size=36, text_color="Black", background_color="White", hover_color="Grey"):
        super().__init__()

        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.is_hovered = False
        self.update_image()
        
    def update(self):
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.update_image()
        if hovered != self.is_hovered:
            self.is_hovered = hovered
            self.update_image()

    def update_image(self):
        current_color = self.hover_color if self.is_hovered else self.background_color
        self.image.fill(current_color)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        else:
            return False
    
