# http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt


# BLOBS

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=1000, centers=20, random_state=123) #(or centers=2)
labels = ["b", "r"]
y = np.take(labels, y < 10) # y<10: T/F => 0,1 for 'b' or 'r'      (or y<1)

# plot
xx,yy = zip(*X)
plt.scatter(xx,yy, c=y)
#plt.show()

# ==========================================

# LINEAR

from sklearn.datasets import make_classification

# generate a random n-class classification problem.
X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
									random_state=1, n_clusters_per_class=1)
# add some uniform noise to the two clusters to bring them closer together
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
linearly_separable = (X, y) # single tuple of (list of lists {X, 100x2},  list (y, 100x1))

# show this data (added, with colors)
x1,x2 = zip(*X)
plt.scatter(np.array(x1)[y==0],np.array(x2)[y==0], c='r')
plt.scatter(np.array(x1)[y==1],np.array(x2)[y==1], c='b')

# ==========================================

# MOONS

from sklearn.datasets import make_moons

# generate two interleaving half circles
Xmoon, ymoon = make_moons(noise=0.3, random_state=0)

# show this data
x1,x2 = zip(*Xmoon)
plt.scatter(np.array(x1)[ymoon==0],np.array(x2)[ymoon==0], c='r')
plt.scatter(np.array(x1)[ymoon==1],np.array(x2)[ymoon==1], c='b')

# ==========================================

# CIRCLES

from sklearn.datasets import make_circles

# generate a large circle containing a smaller circle in 2d
Xcirc, ycirc = make_circles(noise=0.2, factor=0.5, random_state=1)

# show this data
x1,x2 = zip(*Xcirc)
plt.scatter(np.array(x1)[ycirc==0],np.array(x2)[ycirc==0], c='r')
plt.scatter(np.array(x1)[ycirc==1],np.array(x2)[ycirc==1], c='b')

# ==========================================

# built-in sets

from sklearn.datasets import load_boston, load_breast_cancer, load_diabetes, load_digits, load_files, load_iris

data = load_iris()

# ==========================================

# downloadable set

#from sklearn.datasets import fetch_20newsgroups

# ==========================================

# fetch_mldata  (mldata.org repository)

#from sklearn.datasets import fetch_mldata
#import tempfile
#test_data_home = tempfile.mkdtemp()
#iris = fetch_mldata('iris', data_home=test_data_home)




