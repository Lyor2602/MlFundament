import random
from bke import EvaluationAgent, start

class Mijnspeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        for i in range(len(board)):
            if board[i] == my_symbol:
                getal = getal + 5
            return getal
        
class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1,500)
            
        
my_random_agent = MyRandomAgent()
Mijnspeler = Mijnspeler()
start(player_o = my_random_agent, player_x = Mijnspeler)