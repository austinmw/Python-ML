# Example of pipline + cross-validated grid-search
# GridSearchCV(estimator, param_grid, scoring=None, fit_params=None, n_jobs=1, iid=True, refit=True, cv=None, verbose=0, pre_dispatch='2*n_jobs', error_score='raise', return_train_score=True)
# param_grid : dict or list of dictionaries

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier


# build classifier pipeline
text_clf = Pipeline([('vect', CountVectorizer()), 
		         ('tfidf', TfidfTransformer()), 
		         ('clf', SGDClassifier(loss='hinge', penalty='l2',
					        alpha=1e-3, n_iter=5, 
					        random_state=42))
])

# grid search parameters (2^3 combinations)
parameters = {'vect__ngram_range': [(1, 1), (1, 2)], # words or bigrams
		  'tfidf__use_idf': (True, False), # with or without inverse-document-frequency reweighting
		  'clf__alpha': (1e-2, 1e-3), # penalty (smoothing) parameter
}

# create crossvalidating gridsearch classifier (3-fold, by default)
# grid search is solely for optimizing hyper parameters
# hyperparameters: common for similar models and cannot be learnt during training but are set beforehand
gs_clf = GridSearchCV(text_clf, parameters, 
	                           n_jobs=-1, # detect number of CPU's and use them all
	                           verbose=1, # higher = more verbose
			      cv=5) 

# fit model														
gs_clf.fit(twenty_train.data, twenty_train.target)

# display best cv score and corresponding parameters 
print("\nBest score: ", gs_clf.best_score_ )
print("\nBest parameters: ")
for param_name in sorted(parameters.keys()):
	print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))
	
# display detailed information on crossvalidated tuning parameters	
print('\n', pd.DataFrame(gs_clf.cv_results_))

# ==========================================================
# ==========================================================

# NESTED CROSS-VALIDATION

# estimates the generalization error of a model, so it is a good way to choose the best model from a list of candidate models and their associated parameter grids. 
# useful to figure out whether, say, a random forest or a SVM is better suited for your problem.

# Selection and evaluation, simultaneously
# grid.best_score_ is not independent from the best model, since its construction was guided by the optimization of this quantity.
# As a result, the optimized grid.best_score_ estimate may in fact be a biased, optimistic, estimate of the true performance of the model.
# Solution: Use nested cross-validation for correctly selecting the model and correctly evaluating its performance.


from sklearn.model_selection import cross_val_score, GridSearchCV

scores = cross_val_score(GridSearchCV(KNeighborsClassifier(), # outer cross-validation on model, inner cross-validation on hyperparameters
		                                             {"n_neighbors": list(range(1, 100))},
				                       scoring="accuracy",
				                       cv=5, n_jobs=-1), 
		                    X, y, cv=5, scoring="accuracy")

# Unbiased estimate of the accuracy
print("%f +-%f" % (np.mean(scores), np.std(scores)))

# ==========================================================
# ==========================================================


# predict on test data
predicted = gs_clf.predict(twenty_test.data)


