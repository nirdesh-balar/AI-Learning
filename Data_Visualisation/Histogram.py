import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
# generates 100 nums with mean 70 & std dev 10
scores = np.random.normal(loc=70, scale=10, size=100) 

bins = [0,30.60,90,100]
plt.hist(scores,edgecolor = "black",bins=bins)   # bins = rang 
plt.xlabel("score")
plt.ylabel("# of student")

plt.show()