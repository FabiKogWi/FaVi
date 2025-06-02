import pygame
import buttons

pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

button = buttons.TextButton(100, 100, 400, 100, "Hello World")

while True:
    button.draw(screen)
 
    for event in pygame.event.get():
        if button.is_clicked(event):
            print("Clicked :)")
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()