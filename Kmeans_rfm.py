import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from scipy.spatial import ConvexHull
import numpy as np

# Read the CSV file
data = pd.read_csv('rfm_data.csv')

# Choose the number of clusters (K)
num_clusters = 3  # You can adjust this as needed

# Perform KMeans clustering
features = data[['Recency', 'Frequency', 'Monetary']]
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(features)

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with annotations
for i, row in data.iterrows():
    ax.scatter(row['Recency'], row['Frequency'], row['Monetary'], c=row['Cluster'], cmap='Set1', s=50)
    ax.text(row['Recency'], row['Frequency'], row['Monetary'], row['Customer ID'], fontsize=8, ha='center', va='center')

# Plot convex hulls for clusters with sufficient points
min_points_in_cluster = 4  # Minimum number of points to calculate convex hull
cluster_sizes = data.groupby('Cluster').size()
valid_clusters = cluster_sizes[cluster_sizes >= min_points_in_cluster].index

for cluster_id in valid_clusters:
    cluster_points = data[data['Cluster'] == cluster_id][['Recency', 'Frequency', 'Monetary']]
    hull = ConvexHull(cluster_points)
    for simplex in hull.simplices:
        simplex = np.append(simplex, simplex[0])  # Close the loop
        ax.plot(cluster_points.iloc[simplex, 0], cluster_points.iloc[simplex, 1], cluster_points.iloc[simplex, 2], 'k-', alpha=0.5)

ax.set_xlabel('Recency')
ax.set_ylabel('Frequency')
ax.set_zlabel('Monetary')
plt.title('KMeans Clustering: Recency vs Frequency vs Monetary with Convex Hulls')
plt.show()
