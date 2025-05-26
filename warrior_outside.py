"""Задание 3.2 - усложненный вариант 3.1"""

from warrior_within import Warmonger

"""Создаём себе копию Warmonger, чтобы потом обращаться к ней в нашей программе"""

import random

"""Рандом для трассировки урона"""


def fight(player1, player2):
    """Функция для старта шага - создаем таблицы действий и начинаем цикл"""

    while player1.healthbar > 10 and player2.healthbar > 10:
        role1 = random.choice(['attacker', 'defender'])
        role2 = random.choice(['attacker', 'defender'])
        if role1 == 'attacker' and role2 == 'attacker':
                player1.mutual_attack()
                player2.mutual_attack()
        else:
            if role1 == 'attacker':
                damage1 = player1.attack()
                player2.protect(damage1)
            else:
                damage2 = player2.attack()
                player1.protect(damage2)
        print(warrior1.name, warrior1.healthbar, warrior1.armor, warrior1.stamina,
              warrior2.name, warrior2.healthbar, warrior2.armor, warrior2.stamina)
    if player1.healthbar < 10:
        mercy(player1)
    elif player2.healthbar < 10:
        mercy(player2)


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

    def attack(self):
        """Функция атаки."""
        if self.stamina > 0:
            self.stamina -= 10
            return random.randint(0,20)
        else:
            return random.randint(0, 10)

    def mutual_attack(self):
        self.healthbar -= random.randint(10, 30)
        if self.healthbar < 0:
            self.healthbar = 0

    def protect(self, damage):
        """Функция защиты. Итоговый импакт на здоровье и броню расчитывается в зависимости от силы атаки противника"""
        if self.armor >= damage:
            health_taken = random.randint(0, damage)
            self.healthbar -= health_taken
            self.armor -= damage - health_taken
        elif self.armor == 0:
            self.healthbar -= damage
        else:
            self.healthbar -= damage - self.armor
            self.armor = 0
        if self.healthbar < 0:
            self.healthbar = 0


"""Тест-кейс"""
if __name__ == "__main__":
    warrior1 = WarmongerPRO('Parsifal')
    warrior2 = WarmongerPRO('Merlin')
    fight(warrior1, warrior2)
