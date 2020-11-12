import pygame
W = 4288
H = 2848
pygame.init()
pygame.display.set_caption("история")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))
bg = pygame.image.load("uhu.png")
bg_rect = bg.get_rect(topleft=(0, 0))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        
 
pygame.display.update()
