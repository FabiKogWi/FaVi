import pygame
import buttons

pygame.init()
# info = pygame.display.Info()
# WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((1200, 600))

button = buttons.TextButton(screen.get_width() // 2, screen.get_height() // 2, 200, 400, "Hello")

while True:
    button.draw(screen)
 
    for event in pygame.event.get():
        # Menu
        if button.is_clicked(event):
            print("Clicked :)")
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()