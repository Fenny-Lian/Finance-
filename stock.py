import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

from pandas_datareader import data as pdr
#import fix_yahoo_finance as yf

df1 = pdr.get_data_yahoo("SLB", start = "2019-01-01", end = "2019-06-30")
df2 = pdr.get_data_yahoo("SPY", start = "2019-01-01", end = "2019-06-30")

return_goog = df1.Close.pct_change()[1:]
return_spy = df2.Close.pct_change()[1:]

plt.figure(figsize=(20,10))
return_goog.plot()
return_spy.plot()
plt.ylabel("Daily Return of SLB and SPY")
#plt.show()

import statsmodels.api as sm
from statsmodels import regression

X = return_spy.values
Y = return_goog.values

def linreg(x,y):
    x = sm.add_constant(x)
    model = regression.linear_model.OLS(y,x).fit()

    x = x[:,1]
    return model.params[0], model.params[1]

alpha, beta = linreg(X,Y)
print("alpha:", str(alpha))
print("beta:", str(beta))
