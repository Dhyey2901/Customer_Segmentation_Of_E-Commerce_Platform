import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Read data from CSV file
input_file = 'rfm_data.csv'
df = pd.read_csv(input_file)

# Columns to normalize
columns_to_normalize = ["Recency (days)", "Frequency", "Monetary Value"]

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform columns
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# Save normalized data to CSV file
output_file = 'normalized_output.csv'
df.to_csv(output_file, index=False)

print(f"Normalized data saved to '{output_file}'")
