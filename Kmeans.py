import pandas as pd
import matplotlib.pyplot as plt

# Load the RFM data from CSV
rfm_df = pd.read_csv("rfm_data.csv")

# Scatter plot: Recency vs Frequency
plt.figure(figsize=(12, 6))
plt.scatter(rfm_df["Recency (days)"], rfm_df["Frequency"], c=rfm_df["Cluster"], cmap="viridis")
plt.xlabel("Recency (days)")
plt.ylabel("Frequency")
plt.title("Recency vs Frequency Clusters")
plt.colorbar(label="Cluster")
plt.show()

