from collections import defaultdict
from datetime import datetime
import json
import pandas as pd

# Read JSON data from file
with open("updated_data28.json") as json_file:
    data = json.load(json_file)

customer_data = defaultdict(list)

for order in data:
    customer_id = order["Customer Information"]["Customer ID"]
    customer_name = f"{order['Customer Information']['First Name']} {order['Customer Information']['Last Name']}"
    created_at = order["Order Information"]["Created At"]
    monetary_value = float(order["Order Information"]["Total Price"].replace("$", ""))
    
    customer_data[customer_id].append({
        "Customer Name": customer_name,
        "Created At": created_at,
        "Monetary Value": monetary_value
    })

rfm_table = []

for customer_id, orders in customer_data.items():
    orders_sorted = sorted(orders, key=lambda x: x["Created At"], reverse=True)
    
    recency = (datetime.now() - datetime.strptime(orders_sorted[0]["Created At"], "%Y-%m-%d")).days
    frequency = len(orders)
    monetary_value = sum(order["Monetary Value"] for order in orders)
    last_purchase_date = orders_sorted[0]["Created At"]
    customer_name = orders_sorted[0]["Customer Name"]
    
    rfm_table.append({
        "Customer ID": customer_id,
        "Customer Name": customer_name,
        "Recency (days)": recency,
        "Last Purchase Date": last_purchase_date,
        "Frequency": frequency,
        "Monetary Value": monetary_value
    })

# Convert RFM table to DataFrame
rfm_df = pd.DataFrame(rfm_table)

# Print the RFM DataFrame
rfm_df.to_csv('rfm_data.csv', index=False)
print(rfm_df)
