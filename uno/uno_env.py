import gym
from gym import spaces
import numpy as np

from unogame import Uno


class UnoEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(UnoEnv, self).__init__()
        
        self.action_space = spaces.Discrete(54)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)
        
        self.game = Uno()
        self.hand = np.zeros(7, dtype=np.uint8)
        self.history = np.zeros(108, dtype=np.uint8)
    
    
    def step(self, action):
        ...
        return observation, reward, done, info

    def reset(self):
        self.game = Uno(4)
        return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        for n, player in enumerate(self.game.get_players()):
            print(f"Player {n}'s Hand: {player.get_hand()}")
        

    def close(self):
        ...
