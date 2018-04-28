# Script to test normal approximation of Central Limit Theorem with different sample sizes
# Austin Welch 6/9/17

import numpy as np
import random
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# generate population (uniform / exponential / log-normal)
population = list(np.random.uniform(-10,10,10000))
#population = list(np.random.exponential(1,100000))
#population = list(np.random.lognormal(0,1,10000))
population.sort()


# sample sizes to test
sample_sizes = [2, 5, 30, 50, 100]


# distributions of sample mean
data = {}
for s in sample_sizes:
	data[s], dist_xhat  = [], []
	for _ in range(1000):
		sample = random.sample(population,s)
		sample_mean = np.mean(sample)
		data[s].append(sample_mean)
		data[s].sort()


# display
fig = plt.figure(figsize=(5,4*len(sample_sizes)))
axes = {}
for i, s in enumerate(sample_sizes):
	axes[i] = fig.add_subplot(len(sample_sizes),1,i+1)
	_, pval = stats.normaltest(data[s])
	pval = round(pval, 4) # null hypothesis = normally distributed	
	axes[i].set_title("sample size = "+str(s)+", p-value = "+str(pval))
	sns.distplot(data[s], hist=False, ax=axes[i])
plt.show()



