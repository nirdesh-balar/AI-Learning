from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

iris = load_iris()

X = iris.data
y = iris.target

# scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# visualize
# sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 2])

# plt.show()

'''from scipy.cluster.hierarchy import linkage, dendrogram

# linkage matrix
Z = linkage(X_scaled, method="ward")

# Plot
plt.figure(figsize=(12, 6))
dendrogram(Z)
plt.xlabel("samples")
plt.ylabel("distance")
plt.title("Dendrogram for hierarchical clustering")

plt.show(). '''

# Clustering

agg = AgglomerativeClustering(n_clusters=3)
labels = agg.fit_predict(X_scaled)

sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 2], c=labels)

plt.show()