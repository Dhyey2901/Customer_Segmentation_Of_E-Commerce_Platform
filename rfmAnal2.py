import json
import pandas as pd
from datetime import datetime

# Load JSON data from file
with open("updated_data28.json", "r") as json_file:
    data = json.load(json_file)

# Create a dictionary to store RFM values for each customer
rfm_values = {}

# Process data to calculate RFM values
for order in data:
    customer_id = order["Customer Information"]["Customer ID"]
    created_at = order["Order Information"]["Created At"]
    monetary_value = float(order["Order Information"]["Total Price"].replace("$", ""))
    
    recency = (datetime.now() - datetime.strptime(created_at, "%Y-%m-%d")).days
    frequency = 1
    monetary = monetary_value
    
    if customer_id not in rfm_values:
        rfm_values[customer_id] = {"Recency": recency, "Frequency": frequency, "Monetary": monetary}
    else:
        rfm_values[customer_id]["Recency"] = min(rfm_values[customer_id]["Recency"], recency)
        rfm_values[customer_id]["Frequency"] += 1
        rfm_values[customer_id]["Monetary"] += monetary

# Create a DataFrame from the summarized RFM values
rfm_df = pd.DataFrame(rfm_values).T

# Calculate quantiles and assign scores
quantiles = rfm_df.quantile(q=[0.25, 0.5, 0.75])
rfm_df["R_Score"] = rfm_df["Recency"].apply(lambda x: 1 if x <= quantiles["Recency"].iloc[0] else
                                                      2 if x <= quantiles["Recency"].iloc[1] else
                                                      3 if x <= quantiles["Recency"].iloc[2] else 4)

rfm_df["F_Score"] = rfm_df["Frequency"].apply(lambda x: 1 if x <= quantiles["Frequency"].iloc[0] else
                                                        2 if x <= quantiles["Frequency"].iloc[1] else
                                                        3 if x <= quantiles["Frequency"].iloc[2] else 4)

rfm_df["M_Score"] = rfm_df["Monetary"].apply(lambda x: 1 if x >= quantiles["Monetary"].iloc[0] else
                                                       2 if x >= quantiles["Monetary"].iloc[1] else
                                                       3 if x >= quantiles["Monetary"].iloc[2] else 4)

# Calculate the RFM score by combining R, F, and M scores
rfm_df["RFM_Score"] = rfm_df["R_Score"].astype(str) + rfm_df["F_Score"].astype(str) + rfm_df["M_Score"].astype(str)

# Add "Customer ID" as the first column
rfm_df.insert(0, "Customer ID", rfm_df.index)

# Print the summarized RFM DataFrame
print(rfm_df)

# Save the summarized RFM DataFrame to a CSV file
rfm_df.to_csv("rfm_data.csv", index=False)
