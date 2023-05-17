#!/usr/bin/env python
# coding: utf-8

# In[9]:


pip install pyvirtualdisplay


# In[22]:


import gym

# creating and reseting the environment
env = gym.make('MountainCar-v0',render_mode="rgb_array")
env.reset()

# declare some variable in order to store the information of the game
game_finished = False
iterations = 0
observations = []
rewards = []
while(game_finished == False):
    # this step is used to take a random action
    action = env.action_space.sample() 
    result = env.step(action)
    observation = result[0]
    reward = result[1]
    done = result[2]
    info = result[3]
    iterations += 1
    observations.append(observation)
    rewards.append(reward)

    if done:
        game_finished = True
        print("Car will reach to Flag at {} iterations ".format(iterations))

env.close()


# In[ ]:





# ## 

# In[ ]:





# In[ ]:




