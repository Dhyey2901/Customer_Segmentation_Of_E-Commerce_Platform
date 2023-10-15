import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Read the CSV file
data = pd.read_csv('rfm_data.csv')

# Select the columns for clustering
features = data[['Recency', 'Frequency']]

# Choose the number of clusters (K)
num_clusters = 4 # You can adjust this as needed

# Perform KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(features)

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(data=data, x='Recency', y='Frequency', hue='Cluster', palette='Set1')

# Annotate each point with customer ID
for i, row in data.iterrows():
    scatter.annotate(row['Customer ID'], (row['Recency'], row['Frequency']), textcoords="offset points", xytext=(0, 5), ha='center')

plt.title('KMeans Clustering: Recency vs Frequency')
plt.xlabel('Recency')
plt.ylabel('Frequency')
plt.show()
