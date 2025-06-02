# These buttons serve as a template for all of the buttons in the game
import pygame
pygame.init()


class TextButton:
    def __init__(self, x, y, width, height, text, font_size=36, text_color="Black", background_color="White", hover_color="Grey"):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.rect = pygame.Rect(x, y, width, height)

        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        
    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        return self.is_hovered
        

    def draw(self, screen):
        # Test for Hovering
        curr_color = "White"
        if self.hovered():
            curr_color = self.hover_color
        else:
            curr_color = self.background_color
        
        # Drawing the button
        pygame.draw.rect(screen, curr_color, self.rect)

        # Drawing the text
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        else:
            return False
    
