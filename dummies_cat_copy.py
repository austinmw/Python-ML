# Example of using pd.get_dummies() with column names set as the set of categorical values of two different series
# (copy into jupyter notebook)

one = pd.Series(list('aba'),index=range(1,4))
two = pd.Series(list('abc'),index=range(1,4))

poss_vals = sorted(list(set(one.unique().tolist() + two.unique().tolist())))
poss_vals

one = one.astype('category', categories=poss_vals)
two = two.astype('category', categories=poss_vals)

dummies_one = pd.get_dummies(one)
dummies_two = pd.get_dummies(two)


dummies_one
dummies_two

sorted(one.cat.categories.tolist())
sorted(two.cat.categories.tolist())