import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('updated_data28.csv')

# Exclude non-numeric columns or columns you don't want to include
# Modify this list based on your specific dataset and analysis goals
excluded_columns = ['Order Information_Order Status', 'Order Information_Payment Gateway','Order Information_Currency']
numeric_data = data.drop(excluded_columns, axis=1)

# Define your distance metric and linkage method
distance_metric = 'euclidean'
linkage_method = 'ward'

# Calculate linkage matrix
linkage_matrix = linkage(numeric_data, method=linkage_method, metric=distance_metric)

# Visualize the dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix)
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.title('Dendrogram')
plt.show()

# Cut the dendrogram to extract clusters
num_clusters = 3  # Adjust this based on your visualization
clusters = fcluster(linkage_matrix, t=num_clusters, criterion='maxclust')

# Assign cluster labels to your data
data['Cluster'] = clusters

# Save the updated data with cluster labels
data.to_csv('updated_data28_with_clusters.csv', index=False)

# You now have your data with cluster labels assigned and saved to a new CSV file
