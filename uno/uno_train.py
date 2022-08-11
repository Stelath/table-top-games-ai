from uno_env import UnoEnv

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback

import os
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
model_name = "PPO_" + timestamp

# Directory Setup
model_dir = "models/" + model_name
logdir = "logs"

if not os.path.exists(model_dir):
    os.makedirs(model_dir)
if not os.path.exists(logdir):
    os.makedirs(logdir)

# Environment Setup
env = UnoEnv()
env.reset()

eval_env = UnoEnv()
eval_env.reset()

# Model Setup

eval_callback = EvalCallback(eval_env, best_model_save_path=model_dir,
                             log_path=logdir, eval_freq=1000,
                             deterministic=True, render=False)

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)
model.learn(total_timesteps=10000000, tb_log_name=model_name)

env.close()
