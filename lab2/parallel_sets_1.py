"""
Method:         Parallel sets
Data Variables: random
Author:         Rustam Tukhvatov
"""

from pandas.tools.plotting import parallel_coordinates
data = pd.DataFrame(np.random.randint(1, 10, size = (50, 3) ), columns=list('ABC'))

print(data.head())
plt.figure()
parallel_coordinates(data, 'B')
plt.show()