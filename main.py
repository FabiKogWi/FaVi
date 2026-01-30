import pygame
import buttons
import player
import enviroment

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

# Map Surface
map_surf = pygame.Surface((8000, 8000)) # Everything just gets drawn on this
# And then this gets drawn on the map
map_surf.fill("Light Green")

# Player
player = player.Player((25, 25))

player_group = pygame.sprite.GroupSingle(player)

# Enviroment
envir_group = pygame.sprite.Group()

for i in range(1, 5):
    wall_surf = pygame.Surface((50, 100))
    wall_surf.fill("Brown")
    wall = enviroment.Enviroment((i * 2 * 50, 350), wall_surf)
    envir_group.add(wall)


while True:

    # Coding the menu
    if menu:
        screen.fill("Dark Green")
        buttons.update()
        buttons.draw(screen)
        pygame.display.flip()

    if play:
        screen.blit(map_surf, (0, 0))
        map_surf.fill("Light Green")

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
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    player_group.sprite.set_target(event.pos)
            
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
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    if play:
        player_group.update()
        envir_group.update()
        envir_group.draw(map_surf)
        player_group.draw(map_surf)

        # Collision Detection
        for envir in envir_group.sprites():
            if player.rect.colliderect(envir.rect):
                player.set_target((player.pos[0], player.pos[1]))
                print("Collision Detected")

    pygame.display.update()
    clock.tick(60)