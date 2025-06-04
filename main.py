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
player_surf = pygame.Surface((50, 50))
player_surf.fill("Red")
player_rect = player_surf.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2))

# Map Surface
map_surf = pygame.Surface((600, 600))
map_surf.fill("Green")
corners = pygame.Surface((100, 100))
corners.fill("Brown")
map_surf.blit(corners, (0, 0))
map_surf.blit(corners, (1100, 0))
map_surf.blit(corners, (1100, 500))
map_surf.blit(corners, (0, 500))
map_rect = map_surf.get_rect(topleft = (0, 0))
tiles = int(screen.get_width() // map_surf.get_width()) + 1
scroll_x = 0
scroll_y = 0
print(f'{tiles}')



while True:

    if menu:
        screen.fill("Dark Green")
        buttons.update()
        buttons.draw(screen)
        pygame.display.flip()
    if play:
        # screen.fill("Green")
        # Draw scrolling background
        # screen.blit(map_surf, map_rect)
        screen.blit(player_surf, player_rect)

    for event in pygame.event.get():

        # Controls
        key_pressed = False # A bit of a weird solution
        if play and not key_pressed:
            if event.type == pygame.KEYDOWN:
                # Menu
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
                print("HEEEEEELP")
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
    
    # Controls
    # Navigation
    if play:
        screen.fill("Green") # Clears screen
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            scroll_x += 10
        if keys[pygame.K_a]:
            scroll_x -= 10
        if keys[pygame.K_w]:
            scroll_y -= 10
        if keys[pygame.K_s]:
            scroll_y += 10

        for i in range(-1, tiles):
            for j in range(-1, tiles):
                screen.blit(map_surf, (i * map_surf.get_width() - scroll_x, j * map_surf.get_width() - scroll_y))

        if abs(scroll_x) > map_surf.get_width():
            scroll_x = 0
        if abs(scroll_y) > map_surf.get_height():
            scroll_y = 0

        screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)