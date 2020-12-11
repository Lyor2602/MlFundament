import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot


class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    
random.seed(1)
 
# alpha verandert de snelheid waarmee het model verandert naar elke error.
# epsilon verandert de waarde waarmee het algorimte iets willekeurigs nieuws probeert
# als je ze omdraait dan leert het algorimte dus minder snel en het probeert meer willeukeurige dingen
 
my_agent = MyAgent(alpha = 0.8, epsilon = 0.2)
random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)
