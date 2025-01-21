# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
from classes.player import Player  # Импортируем класс Player из файла player.py

# Определяем размеры окна
WIDTH = 1000  # Ширина окна
HEIGHT = 480  # Высота окна
FPS = 144  # Количество кадров в секунду (скорость обновления экрана)

# Задаем цвета (RGB формат)
WHITE = (255, 255, 255)  # Белый цвет
BLACK = (0, 0, 0)  # Черный цвет
RED = (255, 0, 0)  # Красный цвет
GREEN = (0, 255, 0)  # Зеленый цвет
BLUE = (0, 0, 255)  # Синий цвет

# Создаем игру и окно
pygame.init()  # Инициализируем Pygame
pygame.mixer.init()  # Инициализируем звук (не используется в этом примере)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно с заданными размерами
pygame.display.set_caption("УМПА ЛУМПЫ")  # Устанавливаем заголовок окна
clock = pygame.time.Clock()  # Создаем объект часов для контроля FPS

# Начальные координаты и скорость объектов
x = 0  # Начальная позиция прямоугольника по оси X
y = 200  # Начальная позиция прямоугольника по оси Y

xCircle = 500  # Начальная позиция круга по оси X
yCircle = 240  # Начальная позиция круга по оси Y
speed = 1  # Скорость движения объектов

# Добавляем картинку (закомментировано, можно раскомментировать для использования)
# capibara_surface = pygame.image.load("./images/capibara.png")  # Загружаем изображение капибары
# capibara_surface.set_colorkey((255, 255, 255))  # Убираем белый фон
# capibara_surface = pygame.transform.scale(capibara_surface, (100, 100))  # Изменяем размер изображения
# capibara_rect = capibara_surface.get_rect(center=(400, 200))  # Получаем прямоугольник для изображения

# Создаем персонажей
player = Player(image="./images/capibara.png", width=100, height=200)  # Создаем игрока (капибару)
orange = Player(image="./images/orange.png", width=200, height=200, x=700, y=200)  # Создаем объект (апельсин)

# Создаем группу объектов (спрайтов)
group_1 = pygame.sprite.Group(orange)  # Группа спрайтов, содержащая апельсин

# Цикл игры
running = True  # Переменная для управления игровым циклом
while running:
    clock.tick(FPS)  # Контролируем скорость обновления экрана
    screen.fill(WHITE)  # Заполняем экран белым цветом

    # Рисуем круг
    pygame.draw.circle(screen, BLUE, [xCircle, yCircle], 20)  # Рисуем синий круг

    # Рисуем персонажей
    player.draw(screen)  # Рисуем игрока (капибару)
    orange.draw(screen)  # Рисуем апельсин

    # Проверяем столкновения
    if pygame.sprite.spritecollide(player, group_1, False):  # Проверяем столкновение игрока с апельсином
        print("БУМ БАБАХА КАМАЗ")  # Выводим сообщение о столкновении
        orange.x = random.randint(100, WIDTH)  # Перемещаем апельсин в случайное место по оси X
        orange.y = random.randint(100, HEIGHT)  # Перемещаем апельсин в случайное место по оси Y
        player.speed += 10  # Увеличиваем скорость игрока

    # Отслеживаем нажатия клавиш
    keys = pygame.key.get_pressed()  # Получаем список нажатых клавиш
    if keys[pygame.K_d]:  # Если нажата клавиша D
        player.x += player.speed  # Двигаем игрока вправо
    elif keys[pygame.K_a]:  # Если нажата клавиша A
        player.x -= player.speed  # Двигаем игрока влево
    if keys[pygame.K_w]:  # Если нажата клавиша W
        player.y -= player.speed  # Двигаем игрока вверх
    elif keys[pygame.K_s]:  # Если нажата клавиша S
        player.y += player.speed  # Двигаем игрока вниз

    # Проверка на выход за пределы экрана
    if player.x >= WIDTH + player.width:  # Если игрок выходит за правую границу
        player.x = -player.width  # Перемещаем его влево
    elif player.x <= -player.width:  # Если игрок выходит за левую границу
        player.x = WIDTH  # Перемещаем его вправо
    if player.y >= HEIGHT + player.height:  # Если игрок выходит за нижнюю границу
        player.y = -player.height  # Перемещаем его вверх
    elif player.y <= -player.height:  # Если игрок выходит за верхнюю границу
        player.y = HEIGHT  # Перемещаем его вниз

    # Обрабатываем события (например, закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если игрок закрывает окно
            running = False  # Завершаем игровой цикл

    pygame.display.update()  # Обновляем экран

pygame.quit()  # Завершаем работу Pygame


# TODO Добавить в игру полоску жизней, жизни должны быть реализованы в классе player. Добавить Противника при столкновении с которым будет терятся hp