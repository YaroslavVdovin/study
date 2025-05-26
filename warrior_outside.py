"""Задание 3.2 - усложненный вариант 3.1"""

from warrior_within import Warmonger

"""Создаём себе копию Warmonger, чтобы потом обращаться к ней в нашей программе"""

import random

"""Рандом для трассировки урона"""
def role_choice(*players):
    attackers = []
    defenders = []
    for p in players:
        role = random.choice(['attacker', 'defender'])
        if role == 'attacker':
            attackers.append(p)
        else:
            defenders.append(p)
    return attackers, defenders, players

def fight(*players):
    while True:
        attackers, defenders, players = role_choice(*players)
        main_player = random.choice([i for i in players])
        opponents = [i for i in players if i != main_player]
        for op in opponents:
            if op in attackers:
                damage = op.attack()
                if main_player in attackers:
                    main_player.mutual_attack()
                    op.mutual_attack()
                else:
                    main_player.protect(damage)
            else:
                if main_player in attackers:
                    damage = main_player.attack()
                    op.protect(damage)
        if op.healthbar <= 10:
            mercy(op)
            break
        elif main_player.healthbar <= 10:
            mercy(main_player)
            break
def mercy(player):
    """Функция пощадить или не пощадить - пользователь должен ввести да или нет"""
    while True:
        show_wercy = input('Игрок %s при смерти. Ты хочешь его пощадить? Введите "да" или "нет" ' % player.name)
        if show_wercy == 'да':
            print('%s будет жить' % player.name)
            return False
        elif show_wercy == 'нет':
            print('%s обречён на смерть' % player.name)
            return False
        else:
            print("Ошибочный ввод")

class WarmongerPRO(Warmonger):
    """Наследуем класс Warmonger из предыдущего задания + добавляем функционал брони (armor), выносливости (stamina), силы атаки (attack_power)"""
    def __init__(self, name, healthbar=100, armor=100, stamina=100):
        super().__init__(name, healthbar)
        self.armor = armor
        self.stamina = stamina

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
    players = [warrior1, warrior2]
    fight(warrior1, warrior2)
