import models
import exceptions
from settings import LEVEL

#main game procces
def play():
    
    name = input('Enter player name: ')
    print("Awailable heroes:\n1 - wizard\n2 - warrior\n3 - rouge")
    #creating instalse of player
    player = models.Player(name)
    
    #creating instalne of enemy
    enemy = models.Enemy(LEVEL)

    #game loop
    while True:
        try:
            print (f"Your turn!\nPlayer lives: {player.lives}\t Enemy lives: {enemy.lives}")
            print (player.attack(enemy))
            print (f"Enemy turn!\nPlayer lives: {player.lives}\t Enemy lives: {enemy.lives}")
            print (player.defense(enemy))
            
        except exceptions.EnemyDown:
            level += 1
            enemy = models.Enemy(level)
            player.score += 5
            print(f"You attacked successfully! Enemy down. Score: {player.score}")
            
        except exceptions.GameOver as e:
            e.saving(player.name, str(player.score))
            raise exceptions.GameOver

if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver:
        print("Game over! Score saved!")
    except KeyboardInterrupt:
        pass
    finally:
        print("\nGood bye!")
        