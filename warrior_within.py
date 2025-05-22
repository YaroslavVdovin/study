class Warmonger:
    def __init__(self, name, enemy='', healthbar=100):
        self.healthbar = healthbar
        self.name = name
        self.enemy = enemy
    def protect(self):
        self.healthbar -= 20
        if self.healthbar > 0:
            print("%s успешно атаковал %s. У %s осталось %s здоровья" % (self.enemy, self.name, self.name, self.healthbar))
        else:
            print("%s откис %s празднует победу." % (self.name, self.enemy))

if __name__ == "__main__":
    first_player = Warmonger("Leroy Jenkins")
    second_player = Warmonger("Nerzul")
    first_player.enemy = second_player.name
    second_player.enemy = first_player.name
    battle_list = [first_player, second_player]

    while first_player.healthbar > 0 and second_player.healthbar > 0:
        defender = random.choice(battle_list)
        defender.protect()
