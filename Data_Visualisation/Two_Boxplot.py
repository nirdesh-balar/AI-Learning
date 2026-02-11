import matplotlib.pyplot as plt 
import numpy as np

group1 = np.random.normal(50, 10, 100)
group2 = np.random.normal(60, 15, 100)

plt.boxplot([group1, group2], tick_labels=["Group1", "Group2"],showmeans=True)
plt.show()