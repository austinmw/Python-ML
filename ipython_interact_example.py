from IPython.html.widgets import interact

def plot_svm(N=10):
	X, y = make_blobs(n_samples=200, centers=2,
					  random_state=0, cluster_std=0.60)
	X = X[:N]
	y = y[:N]
	clf = SVC(kernel='linear')
	clf.fit(X, y)
	plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='spring')
	plt.xlim(-1, 4)
	plt.ylim(-1, 6)
	plot_svc_decision_function(clf, plt.gca())
	plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
				s=200, facecolors='none')
	
interact(plot_svm, N=[10, 200], kernel='linear');