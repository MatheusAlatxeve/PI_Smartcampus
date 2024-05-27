import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# sns.distplot([0, 1, 2, 3, 4, 5])

# plt.show()

sns.set(style="white")
 
# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)
 
# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")