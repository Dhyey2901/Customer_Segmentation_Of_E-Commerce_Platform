import json

# Read JSON data from a file
with open('data28.json', 'r') as json_file:
    json_data = json.load(json_file)

# Update "Total Price" based on the formula
for entry in json_data:
    order_info = entry.get("Order Information", {})
    total_shipping_price = float(order_info.get("Total Shipping Price", "0.00").replace('$', ''))
    total_tax = float(order_info.get("Total Tax", "0.00").replace('$', ''))
    total_discounts = float(order_info.get("Total Discounts", "0.00").replace('$', ''))

    product_line_items = entry.get("Product Line Items", [])
    total_product_price = sum([
        float(item["Product"]["Price"].replace('$', '')) * item["Product"]["Quantity"]
        for item in product_line_items
    ])

    new_total_price = total_shipping_price + total_tax - total_discounts + total_product_price
    order_info["Total Price"] = f"{new_total_price:.2f}"

# Write the updated JSON data back to the file
with open('updated_data28.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)