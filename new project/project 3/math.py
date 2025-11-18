import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load dataset (Iris)
iris = datasets.load_iris()
X = iris.data

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Reduce to 2D for plotting (using PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot clustering results
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='rainbow', s=50)
plt.title("K-Means Clustering (Iris Dataset)")
plt.xlabel("PCA Feature 1")
plt.ylabel("PCA Feature 2")
plt.show()