
from basic.snakeGym import SnakeEnv
from stable_baselines3 import PPO, A2C
from stable_baselines3.common.evaluation import evaluate_policy
import stable_baselines3 as sb3
import time
import numpy as np
# import gym

# env = gym.make("SnakeEnv-v0")
def evaluate(model, num_episodes=100, display = False):
    """
    Evaluate a RL agent
    :param model: (BaseRLModel object) the RL Agent
    :param num_episodes: (int) number of episodes to evaluate it
    :return: (float) Mean reward for the last num_episodes
    """
    # This function will only work for a single Environment
    env = model.get_env()
    all_episode_rewards = []
    
    for i in range(num_episodes):
        if display:
            env.render()
        episode_rewards = []
        done = False
        obs = env.reset()
        while not done:
            # _states are only useful when using LSTM policies
            action, _states = model.predict(obs)
            # here, action, rewards and dones are arrays
            # because we are using vectorized env
            obs, reward, done, info = env.step(action)
            episode_rewards.append(reward)
            if display:
                env.render()
                print(reward)
                time.sleep(.1)

        all_episode_rewards.append(sum(episode_rewards))

    mean_episode_reward = np.mean(all_episode_rewards)
    print("Mean reward:", mean_episode_reward, "Num episodes:", num_episodes)

    return mean_episode_reward

env = SnakeEnv(rows=10, cols=10)
name = "smart-10"

#EVAL MODEL
# model = PPO("MlpPolicy", env, verbose=1, device="cuda")
# old = evaluate(model)
# print("leanring nows")
# model.learn(total_timesteps=2500000, progress_bar=True)
# model.save(name)
# evaluate(model, num_episodes=20, display=True)
# print(old)


#LOAD MODEL
# model = PPO("MlpPolicy", env, device="cuda").load(path = name, env=env)
# print(model.env)
# evaluate(model, 20, True)




# m = PPO("MlpPolicy", env, verbose=0, device="cuda", n_steps=2048)
# old = evaluate(m)
# print("leanring nows")
# m.learn(total_timesteps=2500000, progress_bar=True)
# m.save(name)
# evaluate(m, num_episodes=20, display=True)
# print(old)

m = PPO("MlpPolicy", env, device="cuda", verbose=1)  .load(path = name, env=env)
print(m.env)



# m.learn(total_timesteps=500000, progress_bar=True)
# m.save(name)


evaluate(m, 20, True)

