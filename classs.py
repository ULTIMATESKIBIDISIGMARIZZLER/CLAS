import pygame
import time

pygame.init()

screen = pygame.display.set_mode([500, 500])
white=(255,255,255)
screen.fill(white)
pygame.display.update()
blue = (0, 0, 255)
font=pygame.font.SysFont("Georgia",36)
subway_surfer=pygame.image.load("class.py/imageszzzz/Subwaysurfers.png")
screen.blit(subway_surfer, (150,100))
text3=font.render("Subway Surfers",True,(255,255,0))
screen.blit(text3,(350,300))
pygame.display.update()
pygame.time.delay(3000)
class Circle:
    def __init__(self, color, pos, rad, wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

circle = Circle(blue, (250, 250), 50, 5)
circle.draw()

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()