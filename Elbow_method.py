import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load normalized data from CSV file
normalized_file = 'normalized_output.csv'
df_normalized = pd.read_csv(normalized_file)

# Select columns for clustering
columns_for_clustering = ["Recency (days)", "Frequency", "Monetary Value"]

# Elbow method to find the optimal number of clusters
inertia_values = []
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(df_normalized[columns_for_clustering])
    inertia_values.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia_values, marker='o')
plt.title("Elbow Method for Optimal Number of Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.xticks(range(1, 11))
plt.show()




# This is the code which shows the elbow point

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# import numpy as np
#
# # Load normalized data from CSV file
# normalized_file = 'rfm_data.csv'
# df_normalized = pd.read_csv(normalized_file)
#
# # Select columns for clustering
# columns_for_clustering = ["Recency (days)", "Frequency", "Monetary Value"]
#
# # Elbow method to find the optimal number of clusters
# inertia_values = []
# for num_clusters in range(1, 11):
#     kmeans = KMeans(n_clusters=num_clusters, random_state=42)
#     kmeans.fit(df_normalized[columns_for_clustering])
#     inertia_values.append(kmeans.inertia_)
#
# # Calculate the second derivative
# second_derivative = np.gradient(np.gradient(inertia_values))
#
# # Plot the second derivative curve
# plt.figure(figsize=(10, 6))
# plt.plot(range(1, 11), second_derivative, marker='o')  # Adjust range to match the dimension of second_derivative
# plt.title("Second Derivative Method for Elbow Point Detection")
# plt.xlabel("Number of Clusters")
# plt.ylabel("Second Derivative")
# plt.xticks(range(1, 11))
# plt.axvline(x=second_derivative.argmax() + 1, color='r', linestyle='--', label='Elbow Point')
# plt.legend()
# plt.show()