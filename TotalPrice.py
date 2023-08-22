import json

with open('D:\OneDrive\Desktop\python files\data28.json', 'r') as json_file:
    json_data = json.load(json_file)

# Insert "Total Shipping Price" attribute if not present
for entry in json_data:
    order_info = entry.get("Order Information", {})
    if "Total Shipping Price" not in order_info:
        order_info["Total Shipping Price"] = "$0.00"

# Insert "Total Tax" attribute if not present
for entry in json_data:
    order_info = entry.get("Order Information", {})
    if "Total Tax" not in order_info:
        order_info["Total Tax"] = "$0.00"

# Insert "Total Discounts" attribute if not present
for entry in json_data:
    order_info = entry.get("Order Information", {})
    if "Total Discounts" not in order_info:
        order_info["Total Discounts"] = "$0.00"

# Write the updated JSON data back to the file
with open('D:\OneDrive\Desktop\python files\updateddata28.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)


