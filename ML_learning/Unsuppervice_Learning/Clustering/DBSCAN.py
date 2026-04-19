from sklearn.datasets import load_iris
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y  =iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# DBSCAN

dbscan = DBSCAN(
    eps = 0.8,
    min_samples = 5
)

labels = dbscan.fit_predict(X_scaled)

# sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:,2], c=labels)

# plt.show()


'''                 Non-linear data                 '''

from sklearn.datasets import make_moons

X, y = make_moons(
    n_samples=300,
    noise=0.05,
    random_state=42
)

X_scaled = scaler.fit_transform(X)

sns.scatterplot(x=X_scaled[:,0], y=X_scaled[:, 1])

# K-Means
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=2,
    random_state=42
)

labels = kmeans.fit_predict(X_scaled)

# sns.scatterplot(x=X_scaled[:,0], y=X_scaled[:, 1], c=labels)

# plt.show()


# DBSCAN

dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)

labels = dbscan.fit_predict(X_scaled)

sns.scatterplot(x=X_scaled[:,0], y=X_scaled[:, 1], c=labels)

plt.show()