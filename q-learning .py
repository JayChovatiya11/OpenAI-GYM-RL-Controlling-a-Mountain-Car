#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gym


# In[16]:


import numpy as np
import gym


#Creating and reseting environment 
env = gym.make('MountainCar-v0')
number_states = env.observation_space.shape[0]
number_actions = env.action_space.n

# Declaring Q-table with dimensions
Q = np.zeros((number_states, number_actions))

#declaring the parameter 
parameter_alpha = 0.01 # learning rate
parameter_gamma = 0.99 # discount factor
parameter_epsilon = 0.01 # exploration rate
number_episodes = 50

# algorithm of q-learning
for episode in range(number_episodes):
    state = env.reset()
    actions_taken = []
    while True:
        action = np.argmax(Q[-1] + np.random.randn(1, number_actions) * (1. / (episode + 1)))
        result = env.step(action)
        next_state = result[2]
        reward = result[1]
        done = result[2]

        actions_taken.append(action)
        Q[-1][1] = Q[-1][1] + parameter_alpha* (reward + parameter_gamma* np.max(Q[0]) - Q[-1][1])

        if done:
            break
    print("Number of actions taken in episode {}: {}".format(episode, len(actions_taken)))


# In[ ]:


pip install gym


# In[5]:


import gym
env = gym.make('MountainCar-v0')
env.reset()


# In[ ]:




