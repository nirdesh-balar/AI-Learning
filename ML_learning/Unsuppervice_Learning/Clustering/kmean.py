import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn.metrics import silhouette_score

X, y = make_blobs(
    n_samples=1000,
    n_features=2,
    centers=4,
    random_state=42
)

# Visualize
# sns.scatterplot(x=X[:, 0], y=X[:, 1],c = y)

# plt.show()

k = 4
kmean = KMeans(
    n_clusters=k,
    random_state=42 
)

labels = kmean.fit_predict(X)
# label = cluster number

# sns.scatterplot(x=X[:, 0], y=X[:, 1], c=labels)

# plt.show()

'''         Choose k using elbow            '''

wcss = []
for k in range(1, 21):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit_predict(X)
    wcss.append(kmeans.inertia_)

# sns.lineplot(x=range(1, 21), y=wcss, marker='o')

# plt.show()

knee = KneeLocator(range(1, 21), wcss, curve="convex", direction="decreasing")

print("optimal K = ", knee.elbow)


'''             chooes k using Silhouette Score             '''

ss = []

for k in range(2, 21):
    kmeans = KMeans(n_clusters=k)
    labels = kmeans.fit_predict(X)
    score = silhouette_score(X, labels)

    ss.append(score)


sns.lineplot(x=range(2, 21), y=ss, marker='o')

plt.show()