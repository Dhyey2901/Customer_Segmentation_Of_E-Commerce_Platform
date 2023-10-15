import pandas as pd

# Read the data from a CSV file
input_csv_file = 'updated_data28.csv'  # Replace with the actual file path
df = pd.read_csv(input_csv_file)

# Sort the DataFrame by the relevant columns for grouping (e.g., State and City)
df.sort_values(by=['Customer Information_Default Address_country_name', 'Customer Information_Default Address_city'], inplace=True)

# Perform the drill-up operation by filling NaN values in the City column with the State
df['Customer Information_Default Address_city'].fillna(df['Customer Information_Default Address_country_name'], inplace=True)

# Drop duplicate rows based on the State column to keep one row per State
df.drop_duplicates(subset='Customer Information_Default Address_country_name', keep='first', inplace=True)

# Reset the index to have a clean index for the resulting DataFrame
df.reset_index(drop=True, inplace=True)

# Write the result back to a new CSV file
output_csv_file = 'drillup_result.csv'  # Replace with the desired output file path
df.to_csv(output_csv_file, index=False)

print(f"Drill-up operation completed. Result saved to '{output_csv_file}'.")
