import pandas as pd
df=pd.read_csv('updated_data28.csv')
def aggregate_country_data(df,target_country):

    country_data = df[df['CustomerInformation_DefaultAddress_country_name'] == target_country]
   # print(country_data)
    return country_data
import pandas as pd

def aggregate_country_data_count():
   
       

        # Group data by 'country' column and count the number of Orders for each country
        country_counts = df['CustomerInformation_DefaultAddress_country_name'].value_counts().reset_index()
        country_counts.columns = ['Country', 'Number of Orders']

        return country_counts

  


# result = aggregate_country_data_count()

# if result is not None:
#     print("Number of Orders for Each Country:")
#     print(result)

# country=input("Enter the Country whose data you want to see..\n")
# aggregate_country_data(country)
