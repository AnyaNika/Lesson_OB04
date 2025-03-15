# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует
# метод attack() своим уникальным способом.

class Sword(Weapon):
    def attack(self):
        print("Удар мечом!")

class Bow(Weapon):
    def attack(self):
        print("Выстрел из лука!")

# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.

class Fighter:
    def __init__(self, weapon: Weapon):
        # Шаг 3: Модифицируйте класс Fighter
        # Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
        self.weapon = weapon

    # Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        self.weapon.attack()

class Monster:
    pass
weapon1 = Sword()
weapon2 = Bow()
fighter1 = Fighter(weapon1)
fighter2 = Fighter(weapon2)

monster = Monster

fighter1.fight()

fighter2.fight()

fighter2.change_weapon(weapon1)
fighter2.fight()
