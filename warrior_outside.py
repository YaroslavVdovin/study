"""Задание 3.2 - усложненный вариант 3.1"""

from warrior_within import Warmonger

"""Создаём себе копию Warmonger, чтобы потом обращаться к ней в нашей программе"""

import random

"""Рандом для трассировки урона"""


def fight(player1, player2):
    """Функция для старта шага - создаем таблицы действий и начинаем цикл"""

    p1_action = ({"attackp1": lambda: player1._attack(), "protectp1": lambda: player1._protect(player2.attack_power)})
    p2_action = ({"attackp2": lambda: player2._attack(), "protectp2": lambda: player2._protect(player1.attack_power)})

    while player1.healthbar > 10 and player2.healthbar > 10:
        random.choice(list(p1_action.values()))()
        random.choice(list(p2_action.values()))()
        print(player1.name, player1.healthbar, player1.armor, player1.stamina)
        print(player2.name, player2.healthbar, player2.armor, player2.stamina)
        if player2.healthbar <= 10:
            mercy(player2)
        elif player1.healthbar <= 10:
            mercy(player1)

def mercy(player):
    """Функция пощадить или не пощадить - пользователь должен ввести да или нет"""
    while True:
        show_wercy = input('Игрок %s при смерти. Ты хочешь его пощадить? Введите "да" или "нет" ' % player.name)
        if show_wercy == 'да':
            print('%s будет жить' % player.name)
            break
        elif show_wercy == 'нет':
            print('%s обречён на смерть' % player.name)
            break
        else:
            print("Ошибочный ввод")

class WarmongerPRO(Warmonger):
    """Наследуем класс Warmonger из предыдущего задания + добавляем функционал брони (armor), выносливости (stamina), силы атаки (attack_power)"""
    def __init__(self, name, healthbar=100, armor=100, stamina=100, attack_power=0):
        super().__init__(name, healthbar)
        self.armor = armor
        self.stamina = stamina
        self.attack_power = attack_power

    @property
    def attack_power(self):
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value):
        self._attack_power = value

    def _attack(self):
        """Функция атаки."""
        if self.stamina > 0:
            self.attack_power = random.randint(0,20)
            self.stamina -= 10
        else:
            self.attack_power = random.randint(0, 10)
        return self.attack_power


    def _protect(self, damage):
        """Функция защиты. Итоговый импакт на здоровье и броню расчитывается в зависимости от силы атаки противника"""
        self.attack_power = 0
        self.damage = damage
        if self.armor >= self.damage:
            health_taken = random.randint(0,self.damage)
            self.healthbar -= health_taken
            self.armor -= self.damage - health_taken
        elif self.armor == 0:
            self.healthbar -= self.damage
        else:
            self.healthbar -= self.damage - self.armor
            self.armor = 0

"""Тест-кейс"""
if __name__ == "__main__":
    warrior1 = WarmongerPRO('Parsifal')
    warrior2 = WarmongerPRO('Merlin')
    fight(warrior1, warrior2)

