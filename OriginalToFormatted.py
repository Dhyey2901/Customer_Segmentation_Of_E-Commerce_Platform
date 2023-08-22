import json

# Load the JSON data from a file
with open('Test-Customer - Student.json', 'r') as file:
    data = json.load(file)

formatted_data = []

for item in data:
    customer_journey_summary = {}
    for attribute in item.get('note_attributes', []):
        name = attribute.get('name', '')
        value = attribute.get('value', '')
        if name == 'Campaign':
            customer_journey_summary['Campaign'] = value
        elif name == 'Content':
            customer_journey_summary['Content'] = value
        elif name == 'Medium':
            customer_journey_summary['Medium'] = value
        elif name == 'Source':
            customer_journey_summary['Source'] = value
    
    order_info = {
        "Order Information": {
            "Order ID": item.get('number', ""),
            "Order Number": item.get('order_number', ""),
            "Order Status": item.get('order_status', ""),
            "Payment Gateway": item.get('gateway', ""),
            "Currency": item.get('presentment_currency', ""),
            "Total Price": f"{item['total_price_set']['shop_money'].get('amount', '')} {item.get('presentment_currency', '')}",
            "Total Shipping Price": f"{item['total_shipping_price_set']['shop_money'].get('amount', '')} {item.get('presentment_currency', '')}",
            "Total Tax": f"{item['total_tax_set']['shop_money'].get('amount', '')} {item.get('presentment_currency', '')}",
            "Total Discounts": f"{item['total_discounts_set']['shop_money'].get('amount', '')} {item.get('presentment_currency', '')}",
            "Total Weight": f"{item.get('total_weight', '')} grams",
            "Created At": item.get('processed_at', ""),
            "Updated At": item.get('updated_at', "")
        },
        "Customer Information": {
            "Customer ID": item['customer'].get('id', ""),
            "First Name": item['customer'].get('first_name', ""),
            "Last Name": item['customer'].get('last_name', ""),
            "Email": item['customer'].get('email', ""),
            "Phone": item['customer']['default_address'].get('phone', ""),
            "Default Address": f"{item['customer']['default_address'].get('address1', '')}, {item['customer']['default_address'].get('address2', '')}, {item['customer']['default_address'].get('city', '')}, {item['customer']['default_address'].get('province', '')}, {item['customer']['default_address'].get('country', '')}, {item['customer']['default_address'].get('zip', '')}"
        },
        "Billing and Shipping Address": {
            "First Name": item['shipping_address'].get('first_name', ""),
            "Last Name": item['shipping_address'].get('last_name', ""),
            "Address": f"{item['shipping_address'].get('address1', '')}, {item['shipping_address'].get('address2', '')}, {item['shipping_address'].get('city', '')}, {item['shipping_address'].get('province', '')}, {item['shipping_address'].get('country', '')}, {item['shipping_address'].get('zip', '')}"
        },
        "Product Line Items": [
            {
                "Product": {
                    "Name": product.get('title', ""),
                    "Price": f"{product.get('price', '')} {item.get('presentment_currency', '')}",
                    "Quantity": product.get('quantity', 0),
                    "Vendor": product.get('vendor', ""),
                    "Fulfillment Status": product.get('fulfillment_status', "")
                }
            } for product in item.get('line_items', [])
        ],
        "Fulfillment Details": {
            "Fulfillment ID": item['fulfillments'][0].get('id', "") if item.get('fulfillments') and len(item['fulfillments']) > 0 else "",
            "Status": item['fulfillments'][0].get('status', "") if item.get('fulfillments') and len(item['fulfillments']) > 0 else "",
            "Tracking Company": item['fulfillments'][0].get('tracking_company', "") if item.get('fulfillments') and len(item['fulfillments']) > 0 else "",
            "Tracking Number": item['fulfillments'][0].get('tracking_number', "") if item.get('fulfillments') and len(item['fulfillments']) > 0 else "",
            "Tracking URL": item['fulfillments'][0].get('tracking_url', "") if item.get('fulfillments') and len(item['fulfillments']) > 0 else ""
        },
        "Customer Journey Summary": customer_journey_summary
    }
    formatted_data.append(order_info)

# Save the formatted data as a JSON file
with open('formatted.json', 'w') as file:
    json.dump(formatted_data, file, indent=4)

print("Formatted data saved to 'formatted.json'")
