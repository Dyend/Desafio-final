import gym
import slimevolleygym
import numpy as np

env = gym.make("SlimeVolley-v0")

obs = env.reset()
done = False
total_reward = 0

while not done:
  action = np.random.randint(2, size=3)
  print(action)
  obs, reward, done, info = env.step(action)
  total_reward += reward
  env.render()

print("score:", total_reward)