import streamlit as st
import City,Country,Product_Vendor
import pandas as pd
df=pd.read_csv('updated_data28.csv')
# Create a dropdown widget
city_names = City.aggregate_city_data_count()
selected_city = st.selectbox('Select a city', city_names)
citydf=City.aggregate_city_data(df,selected_city)

country_names = Country.aggregate_country_data_count()
selected_country = st.selectbox('Select a country', country_names)
countrydf=Country.aggregate_country_data(citydf,selected_country)

vendor_names = Product_Vendor.aggregate_Product_Vendor_data_count()
selected_vendor = st.selectbox('Select a country', vendor_names)
vendordf=Product_Vendor.aggregate_Product_Vendor_data(countrydf,selected_vendor)
# Define a function that gets called when the dropdown changes
def on_dropdown_change(selected_vendor):
    st.write(vendordf)

# Use a button to trigger the autopostback behavior
if st.button('Apply'):
    on_dropdown_change(selected_vendor)
