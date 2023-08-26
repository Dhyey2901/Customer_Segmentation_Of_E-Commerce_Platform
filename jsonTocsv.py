import json
import pandas as pd
import os

# Load the JSON data
with open('updated_data28.json', 'r') as f:
    data = json.load(f)

# Define a function to flatten the nested JSON
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Flatten each order in the JSON data
flattened_orders = [flatten_json(order) for order in data]

# Create a DataFrame from the flattened data
df = pd.DataFrame(flattened_orders)
df.fillna('null', inplace=True)
# Define the CSV file path
csv_file_path = 'output.csv'

# Write the DataFrame to a CSV file
if os.path.exists(csv_file_path):
    # Load the existing CSV file
    existing_df = pd.read_csv(csv_file_path)
    
    # Append the new data to the existing DataFrame
    updated_df = pd.concat([existing_df, df], ignore_index=True)
    
    # Write the updated DataFrame back to the CSV file
    updated_df.to_csv(csv_file_path, index=False)
else:
    # Write the DataFrame to a new CSV file
    df.to_csv(csv_file_path, index=False)
