import pygame
maxfps = 60
winsize = 800,600
class Sprite:
    def __init__(self,center,image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image,self.rect)

window = pygame.Window("tower defense",winsize)
surface = window.get_surface()
clock = pygame.Clock()
player_image = pygame.Surface([50,50])
player = Sprite([winsize[0]/2,winsize[1]/2],player_image)
run = True
while run:
    # оббработка события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    surface.fill("green")
    player.render(surface)
    window.flip()

    clock.tick(maxfps)