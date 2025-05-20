"""Задание 3.2 - усложненный вариант 3.1"""

from warrior_within import Warmonger

"""Создаём себе копию Warmonger, чтобы потом обращаться к ней в нашей программе"""

import random

"""Рандом для трассировки урона"""

def mercy(player):
    """Функция пощадить или не пощадить - пользователь должен ввести да или нет"""
    mercy = input('Игрок %s при смерти. Ты хочешь его пощадить? Введите "да" или "нет" ' % player.name)
    if mercy == 'да':
        print('%s будет жить' % player.name)
    elif mercy == 'нет':
        print('%s обречён на смерть' % player.name)
    else:
        "Решение неясно. Введите 'да' или 'нет'"

def roll_the_dice(player1, player2):
    """Функция для старта шага - рандомно присваивает соперникам роль атакующего или защищающегося"""
    player1.role, player2.role = random.choice(['attacker', 'defender']), random.choice(['attacker', 'defender'])

class WarmongerPRO(Warmonger):
    """Наследуем класс Warmonger из предыдущего задания + добавляем функционал брони (armor), выносливости (stamina), роли (role='attacker' или 'defender')
    и фиксации на цели (enemy)"""
    def __init__(self, name, healthbar=100, armor=100, stamina=100, attack_power=0, role='', enemy=''):
        Warmonger.__init__(self, name, healthbar)
        self.armor = armor
        self.stamina = stamina
        self.role = role
        self.attack_power = attack_power
        self.enemy = enemy

    def action(self):
        """Исходя из своей роли, боец решает - атаковать или защищаться"""
        if self.role == "attacker":
            return self.__attack(self.enemy)
        else:
            return self.__protect(self.enemy)

    def __attack(self, enemy):
        """Функция атаки. В зависимости от стамины присваивается сила атаки.
        Если противник атакует - минусуем себе здоровье и стамину
        в зависимости от его силы атаки.
        После проведения атаки минусуем себе стамину."""
        if self.stamina > 0:
            self.attack_power = random.randint(0,20)
        else:
            self.attack_power = random.randint(0, 10)
        if enemy.role == 'attacker':
            self.healthbar -= enemy.attack_power
            if self.stamina >= enemy.attack_power:
                self.stamina -= enemy.attack_power
            else:
                self.stamina = 0
        else:
            if self.stamina > 0:
                if self.stamina >= enemy.attack_power:
                    self.stamina -= 10
                else:
                    self.stamina = 0
            else:
                pass

    def __protect(self, enemy):
        """Функция защиты. Итоговый импакт на здоровье и броню расчитывается в зависимости от силы атаки противника"""
        if enemy.role == 'attacker':
            if self.armor >= enemy.attack_power:
                health_taken = random.randint(0,enemy.attack_power)
                self.healthbar -= health_taken
                self.armor -= enemy.attack_power - health_taken
            elif self.armor == 0:
                self.healthbar -= enemy.attack_power
            else:
                self.healthbar -= enemy.attack_power - self.armor
                self.armor = 0
        else:
            pass

"""Тест-кейс"""
if __name__ == "__main__":
    player1 = WarmongerPRO('Parsifal')
    player2 = WarmongerPRO('Merlin')
    player1.enemy = player2
    player2.enemy = player1
    while player1.healthbar > 10 and player2.healthbar > 10:
        roll_the_dice(player1, player2)
        player1.action()
        player2.action()
        print(player1.name, player1.healthbar, player1.armor, player1.stamina)
        print(player2.name, player2.healthbar, player2.armor, player2.stamina)
    if player2.healthbar <= 10:
        mercy(player2)
    elif player1.healthbar <= 10:
        mercy(player1)
