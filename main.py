import pygame
import buttons

pygame.init()
# info = pygame.display.Info()
# WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

# Game States
play = True
menu = False
dead = False

# Menu Buttons
options = buttons.TextButton(screen.get_width() // 2 - 100, screen.get_height() // 2 - 25, 200, 50, "Options")
resume = buttons.TextButton(screen.get_width() // 2 - 100, screen.get_height() // 2 - 75, 200, 50, "Resume")
help = buttons.TextButton(screen.get_width() // 2 - 100, screen.get_height() // 2 + 25, 200, 50, "Help")
leave = buttons.TextButton(screen.get_width() // 2 - 100, screen.get_height() // 2 + 75, 200, 50, "Leave")
buttons = pygame.sprite.Group(options, resume, help, leave)

# Player


while True:

    if menu:
        screen.fill("Dark Green")
        buttons.update()
        buttons.draw(screen)
        pygame.display.flip()
    if play:
        screen.fill("Green")

    for event in pygame.event.get():
        key_pressed = False # A bit of a weird solution
        # Controlls
        if play and not key_pressed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("clicked")
                    menu = True
                    play = False
                    key_pressed = True
        elif menu and not key_pressed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("noob")
                    menu = False
                    play = True
                    key_pressed = True

        # Menu
        if menu:
            if options.is_clicked(event):
                print("Options Clicked :)")
            if help.is_clicked(event):
                print("HEEEEEELPT")
            if resume.is_clicked(event):
                menu = False
                play = True
            if leave.is_clicked(event):
                pygame.quit()
                exit()
        
        # Quitting gracefully
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)