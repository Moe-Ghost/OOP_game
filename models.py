from random import randint

from exceptions import EnemyDown, GameOver
from settings import START_LIVES, ALLOWED_ATTACK

class Enemy():
    def __init__(self, level):
        self.level = level
        self.lives = self.level
        
    @staticmethod
    def select_attack():
        return randint(1,3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown

class Player():
    allowed_attack = ALLOWED_ATTACK
    lives = START_LIVES
    score = 0
    def __init__(self, name):
        self.name = name

    @staticmethod
    def fight(attack, defense):
        if attack > defense or attack - defense == -2:
            return -1
        if attack < defense or attack - defense == 2:
            return 1
        return 0
        
    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver
    
    def attack(self, enemy_obj):
        while True:
            player_attack = input("Player choise: ")
            if player_attack in self.allowed_attack:
                player_attack = int(player_attack)
                break
            print('incorrect')
        enemy_attack = enemy_obj.select_attack()
        print(f"Enemy choise: {enemy_attack}")

        result = Player.fight(player_attack, enemy_attack)

        if result == 0:
            return "Its a draw!\n"
        elif result == -1:
            return "Attack missed!\n"

        enemy_obj.decrease_lives()
        return "You attacked successfully!\n"

    def defense(self, enemy_obj):
        while True:
            player_attack = input("Player attack: ")
            if player_attack in self.allowed_attack:
                player_attack = int(player_attack)
                break
            print('incorrect')
        enemy_attack = enemy_obj.select_attack()
        print(f"Enemy attack: {enemy_attack}")

        result = Player.fight(enemy_attack, player_attack)
        if result == 0:
            return "Its a draw\n"
        elif result == -1:
            return "You blocked successfully!\n"
        self.decrease_lives()
        return "Block missed! Minus 1 live\n"
        
    