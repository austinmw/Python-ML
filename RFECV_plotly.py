# (after fitting sklearn RFECV)

import plotly.plotly as py
import plotly.graph_objs as go
import cufflinks as cf
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *

cf.set_config_file(offline=True, theme='ggplot')

init_notebook_mode(connected=True)

print("Optimal number of features : %d" % rfecv.n_features_)

trace = go.Scatter(x=list(range(1, len(rfecv.grid_scores_) + 1)), 
			 y=rfecv.grid_scores_)

layout = go.Layout(xaxis=dict(title="Number of features selected",
					showgrid=False),
			 yaxis=dict(title="Cross validation score (nb of correct classifications)",
					showgrid=False)
			)

fig = go.Figure(data=[trace], layout=layout)

iplot(fig)