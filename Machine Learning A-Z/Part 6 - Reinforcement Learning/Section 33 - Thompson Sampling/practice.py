# Thompson Sampling

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('ADs_CTR_Optimisation.csv')

# Implement Thompson Sampling
import math
N = 10000 # number of rounds
d = 10 # number of models
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        if numbers_of_selection[i] > 0:
            average_reward = sums_of_rewards[i] / numbers_of_selection[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selection[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selection[ad] += 1
    sums_of_rewards[ad] += dataset.values[n, ad]
    total_reward += dataset.values[n, ad]

# Visualizing the result
plt.hist(ads_selected)
plt.title("Histogram of ads selection")
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()