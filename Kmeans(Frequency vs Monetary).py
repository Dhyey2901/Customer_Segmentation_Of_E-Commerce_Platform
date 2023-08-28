import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Read the CSV file
data = pd.read_csv('rfm_data.csv')

# Select the columns for clustering
features = data[['Frequency', 'Monetary']]

# Choose the number of clusters (K)
num_clusters = 4  # You can adjust this as needed

# Perform KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(features)

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(data=data, x='Frequency', y='Monetary', hue='Cluster', palette='Set1')

# Annotate each point with customer ID
for i, row in data.iterrows():
    scatter.annotate(row['Customer ID'], (row['Frequency'], row['Monetary']), textcoords="offset points", xytext=(0, 5), ha='center')

plt.title('KMeans Clustering: Frequency vs Monetary')
plt.xlabel('Frequency')
plt.ylabel('Monetary')
plt.show()
