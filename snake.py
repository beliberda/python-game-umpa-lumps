from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from panda3d.core import CollisionNode, CollisionSphere
from panda3d.core import KeyboardButton
import sys

class DoomLikeGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Настройка окна
        self.window_props = WindowProperties()
        self.window_props.setSize(800, 600)
        self.window_props.setTitle("Doom-like 3D Game")
        self.win.requestProperties(self.window_props)

        # Настройка камеры
        self.disableMouse()  # Отключаем управление камерой мышью
        self.camera.setPos(0, -10, 2)  # Позиция камеры
        self.camera.setHpr(0, 0, 0)    # Ориентация камеры

        # Загрузка карты
        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.5, 0.5, 0.5)
        self.scene.setPos(-8, 42, 0)

        # Игрок
        self.player = Actor("models/player", {"walk": "models/player-walk"})
        self.player.reparentTo(self.render)
        self.player.setScale(0.5)
        self.player.setPos(0, 0, 0)

        # Управление игроком
        self.keys = {
            "w": False,
            "a": False,
            "s": False,
            "d": False,
            "space": False
        }
        self.accept("w", self.set_key, ["w", True])
        self.accept("w-up", self.set_key, ["w", False])
        self.accept("a", self.set_key, ["a", True])
        self.accept("a-up", self.set_key, ["a", False])
        self.accept("s", self.set_key, ["s", True])
        self.accept("s-up", self.set_key, ["s", False])
        self.accept("d", self.set_key, ["d", True])
        self.accept("d-up", self.set_key, ["d", False])
        self.accept("space", self.shoot)

        # Противники
        self.enemies = []
        self.spawn_enemies()

        # Здоровье игрока
        self.player_hp = 100

        # Коллизии
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        self.setup_collisions()

        # Основной игровой цикл
        self.taskMgr.add(self.update, "update")

    def set_key(self, key, value):
        self.keys[key] = value

    def update(self, task):
        dt = globalClock.getDt()

        # Движение игрока
        if self.keys["w"]:
            self.player.setY(self.player, 5 * dt)
        if self.keys["s"]:
            self.player.setY(self.player, -5 * dt)
        if self.keys["a"]:
            self.player.setX(self.player, -5 * dt)
        if self.keys["d"]:
            self.player.setX(self.player, 5 * dt)

        # Обновление противников
        for enemy in self.enemies:
            enemy.lookAt(self.player)
            enemy.setY(enemy, 2 * dt)

        return task.cont

    def spawn_enemies(self):
        for i in range(3):
            enemy = Actor("models/enemy", {"walk": "models/enemy-walk"})
            enemy.reparentTo(self.render)
            enemy.setScale(0.5)
            enemy.setPos(i * 5, 10, 0)
            self.enemies.append(enemy)

    def shoot(self):
        # Логика стрельбы
        for enemy in self.enemies:
            if self.player.getDistance(enemy) < 5:
                self.enemies.remove(enemy)
                enemy.removeNode()
                break

    def setup_collisions(self):
        # Коллизии игрока
        player_collider = self.player.attachNewNode(CollisionNode("player_collider"))
        player_collider.node().addSolid(CollisionSphere(0, 0, 0, 1))
        self.cTrav.addCollider(player_collider, self.pusher)
        self.pusher.addCollider(player_collider, self.player, self.drive)

    def drive(self, entry):
        # Обработка коллизий
        print("Collision detected!")

# Запуск игры
game = DoomLikeGame()
game.run()