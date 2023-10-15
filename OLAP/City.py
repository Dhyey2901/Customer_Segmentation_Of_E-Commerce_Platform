import pandas as pd
df=pd.read_csv('updated_data28.csv')
def aggregate_city_data(df,target_city):

    city_data = df[df['CustomerInformation_DefaultAddress_city'] == target_city]
    #print(city_data)
    return city_data
import pandas as pd

def aggregate_city_data_count():
    try:
        # Load Excel data into a DataFrame
       

        # Group data by 'City' column and count the number of Orders for each city
        # city_data=df['CustomerInformation_DefaultAddress_city']
        city_counts = df['CustomerInformation_DefaultAddress_city'].value_counts().reset_index()
        city_counts.columns = ['City', 'Number of Orders']
        # print(city_counts['City'])
        return city_counts['City']

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


aggregate_city_data_count()
# print(result)
# if result is not None:
#     print("Number of Orders for Each City:")
#     print(result)
# city=input("Enter the city whose data you want to see.\n")
# aggregate_city_data(city)
