import random

class Warmonger:
    def __init__(self, name, healthbar=100):
        self.healthbar = healthbar
        self.name = name

    def protect(self):
        self.healthbar -= 20

if __name__ == "__main__":
    first_player = Warmonger("Leroy Jenkins")
    second_player = Warmonger("Nerzul")
    battle_list = [first_player, second_player]

    while first_player.healthbar > 0 and second_player.healthbar > 0:
        defender = random.choice(battle_list)
        attacker = [i for i in battle_list if i != defender][0]
        defender.protect()
        if defender.healthbar > 0:
            print("%s успешно атаковал %s. У %s осталось %s здоровья" % (attacker.name, defender.name, defender.name, defender.healthbar))
        else:
            print("%s откис %s празднует победу." % (defender.name, attacker.name))
