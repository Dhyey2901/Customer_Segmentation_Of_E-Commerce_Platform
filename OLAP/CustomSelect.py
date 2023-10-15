import Product_Vendor
import City
import Country

import pandas as pd
df=pd.read_csv('updated_data28.csv')
city_input=input("Enter the city name you want to search for:")
country_input=input("Enter the country name you want to search for:")
product_vendor_input=input("Enter the product_vendor name you want to search for:")

city=City.aggregate_city_data(df,city_input)
print(city)
country=Country.aggregate_country_data(city,country_input)
print(country)
product_Vendor=Product_Vendor.aggregate_Product_Vendor_data(country,product_vendor_input)
if product_Vendor.isnull==False:
    print(product_Vendor)
    
else:
    print("No such Data Available")