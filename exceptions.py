class GameOver(Exception):
    @staticmethod
    def saving(name, score):
        with open('scores.txt', 'a+') as f:
            f.write(f"Name: {name}\tFinal score: {score}\n")

class EnemyDown(Exception):
    pass
