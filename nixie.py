import pygame
import time

pygame.init()


display_width = 800
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
#gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Nixie Clock')
pygame.mouse.set_visible(0)

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

Img0 = pygame.image.load('Nixie0.png')
Img1 = pygame.image.load('Nixie1.png')
Img2 = pygame.image.load('Nixie2.png')
Img3 = pygame.image.load('Nixie3.png')
Img4 = pygame.image.load('Nixie4.png')
Img5 = pygame.image.load('Nixie5.png')
Img6 = pygame.image.load('Nixie6.png')
Img7 = pygame.image.load('Nixie7.png')
Img8 = pygame.image.load('Nixie8.png')
Img9 = pygame.image.load('Nixie9.png')
Imgdot = pygame.image.load('Neon.png')



def digit(x,y,z):
    if z == 0:
      gameDisplay.blit(Img0, (x,y))
    if z == 1:
      gameDisplay.blit(Img1, (x,y))
    if z == 2:
      gameDisplay.blit(Img2, (x,y))
    if z == 3:
      gameDisplay.blit(Img3, (x,y))
    if z == 4:
      gameDisplay.blit(Img4, (x,y))
    if z == 5:
      gameDisplay.blit(Img5, (x,y))
    if z == 6:
      gameDisplay.blit(Img6, (x,y))
    if z == 7:
      gameDisplay.blit(Img7, (x,y))
    if z == 8:
      gameDisplay.blit(Img8, (x,y))
    if z == 9:
      gameDisplay.blit(Img9, (x,y))
    if z == 10:
      gameDisplay.blit(Imgdot, (x,y))


y = 150
c = 0
ml = 0
bl = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    
    clock.tick(60)
    c = c +1
    if c >= 60:
        c = 0
        bl = ~ bl
        gameDisplay.fill(black)
        
        result = time.localtime()        

        digit(0,y, result.tm_hour // 10)
        digit(200,y ,result.tm_hour % 10)
              
        digit(400,y, result.tm_min // 10)
        digit(600,y, result.tm_min % 10)
        if bl == 0:
            digit(395,y+140, 10)      
      
        pygame.display.update()

        

pygame.quit()
quit()