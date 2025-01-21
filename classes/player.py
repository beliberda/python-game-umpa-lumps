import pygame
class Player(pygame.sprite.Sprite):
    speed = 1
    hp = 100
    x = 200
    y = 200
    width = 100
    height = 100
    surface = ""
    rect=""
    def __init__(self,image, width=100, height=100,x=200,y=200):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # передаем путь до картинки и создаем surface
        self.surface = pygame.image.load(image)
        # убираем цвет
        self.surface.set_colorkey((255, 255, 255))
        # трансформируем surface
        self.surface = pygame.transform.scale(self.surface, (width, height))
        # Создаем холст, на котором будет наша картинка и задаем ему центр =================================
        self.rect = self.surface.get_rect(center=(self.x,self.y))
    def draw(self,screen:pygame.Surface):
        self.rect.center = (self.x, self.y)
        # рисуем картинку на холсте
        screen.blit(self.surface, self.rect)

git config --global user.name "ваш username с github"
git config --global user.email "ваша почта с github"