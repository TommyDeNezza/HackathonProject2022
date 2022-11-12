import pygame, sys, random, time
pygame.init() 

#Constants/Vars
HEIGHT = 748
WIDTH = 1422

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#Set-Up
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dopamine D")
clock = pygame.time.Clock()

#Classes
class Background():
    def __init__(self):
        self.image = pygame.image.load("Icon_Assets/bckgd.jpeg").convert_alpha()
        self.image2 = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
    def draw(self, surface):
        surface.fill(WHITE)
        surface.blit(self.image2, (0,0))
class Face():
    def __init__(self, surface):
        self.phase1 = pygame.image.load("Icon_Assets/happyface.png").convert_alpha()
        self.phase2 = pygame.image.load("Icon_Assets/sadface.png").convert_alpha()
        self.posX = 100
        self.posY = 15
        self.surface = surface
        self.rect = self.phase1.get_rect(topleft = (self.posX, self.posY))
    def draw1(self):
        self.surface.blit(self.phase1, (self.posX,self.posY))
        self.rect = self.phase1.get_rect(topleft = (self.posX, self.posY))
    def draw2(self):
        self.surface.blit(self.phase2, (self.posX,self.posY))
        self.rect = self.phase2.get_rect(topleft = (self.posX, self.posY))
class Quotes():
    def __init__(self):
        self.font = pygame.font.SysFont('monospace', 30, bold = False)
        self.list = ["Don’t let yesterday take up too much of today", "If you’re going through hell, keep going.", "Every man dies. Not every man lives."]
    def draw(self, surface):
        num = random.randint(0, len(self.list)-1)
        quote = self.list[num]
        lbl = self.font.render(quote,1, BLACK)

        surface.blit(lbl,(150,15))

#Main Loop


def main():
    #Objects
    background = Background()
    face = Face(screen)
    quote = Quotes()

    #Functions
    def draw_screen():
        background.draw(screen)
        face.draw2()
    #def quoter(surface):
      # time.sleep(30)
       # quote.draw(surface)

    while True:

        draw_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if face.rect.collidepoint(pygame.mouse.get_pos()):
                    face.draw1()
                    if event.type == pygame.MOUSEBUTTONUP:
                        face.draw2()
                
            
        #Game
        pygame.display.flip()
main()