#Under- and over-fitting
# Under-fitting: the model is too simple and does not capture the true relation between X and Y.
# Over-fitting: the model is too specific to the training set and does not generalize.


from sklearn.model_selection import validation_curve

# Evaluate parameter range in CV
param_range = range(2, 200)
param_name = "max_leaf_nodes"

train_scores, test_scores = validation_curve(
	DecisionTreeClassifier(), X, y, 
	param_name=param_name, 
	param_range=param_range, cv=5, n_jobs=-1)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

# Plot parameter VS estimated error
plt.xlabel(param_name)
plt.ylabel("mean error")
plt.xlim(min(param_range), max(param_range))
plt.plot(param_range, 1. - train_scores_mean, color="red", label="Training error")
plt.fill_between(param_range, 
				 1. - train_scores_mean + train_scores_std,
				 1. - train_scores_mean - train_scores_std,
				 alpha=0.2, color="red")
plt.plot(param_range, 1. - test_scores_mean, color="blue", label="CV error")
plt.fill_between(param_range, 
				 1. - test_scores_mean + test_scores_std,
				 1. - test_scores_mean - test_scores_std, 
				 alpha=0.2, color="blue")
plt.legend(loc="best")


# Best trade-off
print("%s = %d, CV error = %f" % (param_name,
					 param_range[np.argmax(test_scores_mean)],
		 			 1. - np.max(test_scores_mean)))
		
