import random

class Warmonger:
    def __init__(self, name, healthbar=100):
        self.healthbar = healthbar
        self.name = name
    def attack(self, enemy):
        enemy.healthbar -= 20
        if enemy.healthbar > 0:
            print("%s успешно атаковал %s. У %s осталось %s здоровья" % (self.name, enemy.name, enemy.name, enemy.healthbar))
        else:
            print("%s откис %s празднует победу." % (enemy.name, self.name))

if __name__ == "__main__":
    first_player = Warmonger("Leroy Jenkins")
    second_player = Warmonger("Nerzul")

    battle_list = [first_player, second_player]

    while first_player.healthbar > 0 and second_player.healthbar > 0:
        attacker = random.choice(battle_list)
        defender = random.choice([i for i in battle_list if i is not attacker])
        attacker.__attack(defender)