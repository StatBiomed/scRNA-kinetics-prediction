HELP_STRING="""

Date : April 22,2021

Author : Ruiyan Hou (ruiyan_hou@163.com)

This script will produce the figure 2A in the supplementary.
We take the pancreas dataset as an example to show the relationship between the log(1/gamma) in stochastic model and 
the log(beta) in dynamical model.

"""


# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import pylab as pl
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from hilearn import CrossValidation, corr_plot
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt


#arrange data
basicdf=pd.read_csv('/home/houruiyan/scRNAkineticprediction/scRNA-kinetics-prediction/data/estimated/pancreas_dynamical_beta_gamma.csv',index_col=0)
print(basicdf)
y=pd.read_csv('/home/houruiyan/scRNAkineticprediction/scRNA-kinetics-prediction/data/estimated/pancreas_stochastical_gamma.csv',index_col=0)
print(y)
mergedf=y.merge(basicdf,on='gene_id')
print(mergedf)


#plot scatter plot
fig=plt.gcf()
corr_plot(mergedf['log(fit_beta)'].values,-mergedf['log(velocity_gamma)'].values,size=20,dot_color='tomato',alpha=0.8)
pl.xlabel(u"log(β) in dynamical model",fontsize=15)
pl.ylabel(u"log(1/γ) in stochastic model",fontsize=15)
pl.title('Pancreas',fontweight='medium',fontsize=18)
fig.savefig(u'/home/houruiyan/scRNAkineticprediction/figure/supp/FigS2/pancreas.pdf', dpi=300, bbox_inches='tight')