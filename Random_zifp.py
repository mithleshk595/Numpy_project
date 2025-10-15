from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(2,3))
sns.displot(x[x <10])
plt.show()
