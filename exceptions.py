#called when player lose all lives
class GameOver(Exception):
    #saving players score
    @staticmethod
    def saving(name, score):
        with open('scores.txt', 'a+') as f:
            f.write(f"Name: {name}\tFinal score: {score}\n")

#called when player beat an enemy
class EnemyDown(Exception):
    pass
