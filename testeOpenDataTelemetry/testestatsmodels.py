# pip install statsmodels

# import pandas as pd

# df = pd.read_csv('data.csv')

# import statsmodels.api as sm

# print(data.describe())

# import statsmodels.formula.api as smf

# model = smf.ols('Y ~ X', data=data).fit()
# print(model.summary())
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

#pandas data
data = sm.datasets.get_rdataset("Guerry", "HistData").data

results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=data).fit()

print(results.summary())