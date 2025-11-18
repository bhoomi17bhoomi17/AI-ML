import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift, estimate_bandwidth
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset (Iris for simplicity)
iris = datasets.load_iris()
X = iris.data
y = iris.target  # True labels (only for reference, clustering is unsupervised)

# Standardize data for better performance
X = StandardScaler().fit_transform(X)

# Reduce dimensions for visualization (2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Dictionary to hold clustering results
clustering_algorithms = {
    "K-Means": KMeans(n_clusters=3, random_state=42),
    "Hierarchical (Agglomerative)": AgglomerativeClustering(n_clusters=3),
    "DBSCAN": DBSCAN(eps=0.8, min_samples=5),
    "Gaussian Mixture Model": GaussianMixture(n_components=3, random_state=42),
    "Mean Shift": MeanShift(bandwidth=estimate_bandwidth(X, quantile=0.2))
}

# Plot results
plt.figure(figsize=(15, 8))
for i, (name, algorithm) in enumerate(clustering_algorithms.items()):
    # Fit model
    if name == "Gaussian Mixture Model":
        y_pred = algorithm.fit(X).predict(X)
    else:
        y_pred = algorithm.fit_predict(X)
    
    # Plotting
    plt.subplot(2, 3, i+1)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_pred, cmap='rainbow', s=30)
    plt.title(name)

plt.suptitle("Comparison of Clustering Techniques on Iris Dataset", fontsize=16)
plt.tight_layout()
plt.show()
sae-jjuc-trm