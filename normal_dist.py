import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

# Using mathplotlib.mlab
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-3, 3, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))
#plt.show()



# Or using scipy.stats

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
plt.plot(x_axis, norm.pdf(x_axis,0,2))


plt.show()

