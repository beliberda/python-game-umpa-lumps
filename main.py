k=1 
while True:
    for n in range(2,0,-1):
        print(n, end=" ")
    k+=1
    if k ==3:
        break

# https://meet.google.com/ias-tsjm-ygd
# импортировали библиотеку для управления временем (сделать задержку программы и все такое)
import time
# библиотека для рандомного числа
import random

# import player_class
from player_class import Player
from enemy_class import Enemy

# ВЫЗОВ 15.10.2024

# СОЗДАТЬ, ЕСЛИ НЕ СОЗДАЛИ, КЛАСС ENEMY, добавить ему дамаг, хп, броня, выносливость. Создать объект класса с параметрами


    

listEnemy = [Enemy("Тролль"),Enemy("Пупа")]
print(listEnemy)
# МЕТОДЫ - ФУНКЦИИ ПЕРСОНАЖА
# ничего
# атаковать
# защищаться
# уворачиваться
# убегать



# "ВОИН" != "воин"
# > < == != >= <=
# с помощью or добавили второе условие. если пользователь вводит 1 или воин, то условие срабатывает, если нет, то нет



# здесь прибавляем к хп, мане и выносливости силу, интеллект и ловкость умноженные на 5



player = Player(input("Введите имя персонажа: "))
player.show_info()
troll = Enemy("Умпа-Лумпа", 60, 15)
troll.attack(player)
player.attack(troll)




print("Приветствую тебя,", player.name)

# for i in range(100,0,-1):
#     print("Проход по циклу (итерация):", i)

# Создали переменную, которая отслеживает идет игра или нет. Если True игра идет, False - закончена
isGame = True

while isGame == True:
    print("\nТекущее хп:", player.hp) 
    # вычисляем случайное число через библиотеку random и фукнцию randint(), внутри указываем от скольки и до скольки
    # результат записываем в переменную roll
    roll = random.randint(1,6)
    print("Выпало число", roll)
    # Если выпадает 6, то делаем столкновение с противником.
    if roll == 6:
        print("\nПеред вами встал медведь, что будем делать?")
        enemyHp = 50
        enemyDamage = 20
        while enemyHp>0:
            choice = input("1. Атаковать, 2. Увернуться, 3. Защититься, Ничего: пропустить ход")

            if choice == 1 or choice.lower() == "атаковать":
                print("\nВы атаковали медведя, нанесли урон", player.damage)
                enemyHp -= player.damage
            elif choice == "2" or choice.lower() == "увернуться":
                roll = random.randint(1,2)
                if roll == 1:
                    print("\nВы увернулись от удара медведя")
                else:
                    print("\nОП! Пропустил двоечку! -10 хп")
                    player.hp -= 10
            elif choice == "3" or choice.lower() == "защититься":
                if enemyDamage > player.armor:
                    print(f"\nВы частично защищаетесь от удара, получите по лицу {enemyDamage-player.armor} урона")
                    player.hp -= enemyDamage - player.armor
                else: 
                    print("ПОЛНАЯ БЛОКИРОВКА УРОНА")

            if enemyHp <= 0:
                print("\УРА! ПОБИДА!")
                break
            if player.hp<=0:
                print("\nВы погибли!")
                isGame = False
                break
                

        # еще одна проверка на 5, все также, как и выше
    elif roll == 5:
        print("\nНа вас налетела стая АГРЕССИВНЫХ пингвинов, потеряйте 15 хп")
        hp -= 15

    # делаем проверку на окончание игры, если хп ниже 0
    if hp <= 0:
        print("\nПОТРАЧЕНО")
        # игра закончена
        isGame = False

    #делаем задержку, чтобы игра не так быстро шла (время в секундах, здесь пол секунды)     
    time.sleep(0.5)

print("Игра закончена")

# Что нам надо будет добавить
# 4) атака, блок, уворот
# 1) добавить броню
# 2) восстановление здоровья
# 3) оружие
