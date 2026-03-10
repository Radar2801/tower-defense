import pygame 
from random import randint
maxfps = 60
winsize = 800,600
class Sprite:
    def __init__(self,center,image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center
    def render(self, surface):
        surface.blit(self.image,self.rect)

class Movesprite(Sprite):
    def __init__(self, center, image,speed,direction):
        super().__init__(center, image)
        self.speed = speed
        self.direction = direction
    def update(self):
        vector = self.direction * self.speed
        self.rect.move_ip(vector)

pygame.init()

window = pygame.Window("tower defense",winsize)
surface = window.get_surface()
clock = pygame.Clock()
font = pygame.Font(None,32)

player_image = pygame.Surface([50,50])
player = Sprite([winsize[0]/2,winsize[1]/2],player_image)

bullets = []
enemies = []

run = True
score = 0

while run:
    # обработка события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.Vector2(player.rect.center)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            vector = (pos - center).normalize()
            img = pygame.Surface([10,10])
            img.fill("blue")
            bullet = Movesprite(center,img,7,vector)
            bullets.append(bullet)

    if randint (0,100) <= 10:
        r = randint(1,4)
        if r == 1:
            pos = pygame.Vector2(
                randint(0,winsize[0]),
                -100
            )
        if r == 2:
            pos = pygame.Vector2(
                winsize[0] + 100,
                randint(0,winsize[1])
            )
        if r == 3:
            pos = pygame.Vector2(
                randint(0,winsize[0]),
                winsize[1] + 100,
            )
        if r == 4:
            pos = pygame.Vector2(
                -100,
                randint(0,winsize[1])
            )
        center = pygame.Vector2(player.rect.center)
        vector = (pos - center).normalize()    
        img = pygame.Surface([50,50])
        img.fill("black")
        speed = randint(200,600) / 100
        enemy = Movesprite(center,img,speed,vector)
        enemies.append(enemy)

    for bullet in bullets:
        bullet.update()
    for enemy in enemies:
        enemy.update()

    for enemy in enemies:
       for bullet in bullets:
            # colliderect - проверка на столкновение 
            if bullet.rect.colliderect(enemy.rect):
                score += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            score = 0
            enemies.clear()
            bullets.clear()
            break
    
    # отрисовка
    surface.fill("green")


    for bullet in bullets:
        bullet.render(surface)
    for enemy in enemies:
        enemy.render(surface)
    player.render(surface)

    text = 'Баллы: ' + str(score)
    image = font.render(text, True, 'black')
    surface.blit(image, [10,10])

    window.flip()
    clock.tick(maxfps)