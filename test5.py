import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""xpoints = np.array([10, 6, 3]).reshape([3,1])
ypoints = np.array([[14, 40, 30],[ 1, 2, 3]]).reshape([3,2])

#plt.plot(xpoints, ypoints, 'D')
#plt.plot(ypoints, marker = 'd')
plt.plot(xpoints, ypoints, 'o:r')


plt.show()"""

df = pd.read_csv('data.csv')

df.plot(kind='scatter',x='Pulse',y='Calories')

plt.show()






