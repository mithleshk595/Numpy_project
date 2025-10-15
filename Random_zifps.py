from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=3, size=(3,4))
sns.displot((x[x<12]))
plt.show()