import pygame

pygame.init()

#game window dimensions 
Screen_Width = 800
Screen_Height = 600

#game window
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))

#drawing a rectangle (player) it takes 4 arguments 
#(first 2, x and y coordenates on game window, and other 2 width and height)
player = pygame.Rect(300,250,50,50)
obstacle = pygame.Rect(100,50,25,25)
pygame.time.Clock()

#main loop
run = True
while run:

    Screen.fill((0,0,0,0))
    color = (255,0,0,0)

    if player.colliderect(obstacle):
        color = (128,128,0)
       
        
    pygame.draw.rect(Screen,color, player)
    pygame.draw.rect(Screen,(124,252,0), obstacle)
    key = pygame.key.get_pressed() #funcion get pressed regresa false en tocas las teclas que no estan presionadas
    if key[pygame.K_a] == True: #revisa la funcion getpressed para ver si la tecla a esta siendo presiona
        player.move_ip(-1,0) #funcion de los objetos rect se usa para mover el rectangulo
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    #event handler, always looking for events like pressing a key or move a mouse etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento de presionar la X de salida
            run = False #se pone run en false para que el juego se cierre
    pygame.display.update()
    pygame.time.Clock().tick(60) #limita la velocidad de juego a 60 frames
pygame.quit()