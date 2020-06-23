import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)
t = pd.read_csv('train.csv', sep=',',usecols=(62, 80))
X = t['GarageArea']
Y = t['SalePrice']
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(X, Y, alpha=.75, color='b')
plt.title('Scatter plot with out outliner')
plt.show()

# Reduced threshold to remove anamolies
z = np.abs(stats.zscore(t))
modified = t[(z < 2).all(axis=1)]

x = modified['GarageArea']
y = modified['SalePrice']
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(x, y)
plt.title('Scatter plot after outliner')
plt.show()
