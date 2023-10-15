import pandas as pd
df=pd.read_csv('updated_data28.csv')
def aggregate_Product_Vendor_data(df,target_Product_Vendor):
  
        Product_Vendor_data1= df[df['ProductLineItems_0_Product_Vendor']==target_Product_Vendor]
        
        Product_Vendor_data2= df[df['ProductLineItems_1_Product_Vendor']==target_Product_Vendor]
        
        Product_Vendor_data3= df[df['ProductLineItems_2_Product_Vendor']==target_Product_Vendor]
        Product_Vendor_data=pd.concat([Product_Vendor_data1,Product_Vendor_data2,Product_Vendor_data3])
        
        #print(Product_Vendor_data)
        return Product_Vendor_data
        #print(type(Product_Vendor_data))

def aggregate_Product_Vendor_data_count():
    try:
        # Load Excel data into a DataFrame
       

        # Group data by 'Product_Vendor' column and count the number of Orders for each Product_Vendor
        df1 = pd.Series(df['ProductLineItems_0_Product_Vendor'])
        df2 = pd.Series(df['ProductLineItems_1_Product_Vendor'])
        df3 = pd.Series(df['ProductLineItems_2_Product_Vendor'])
        product_vendor_cols=pd.concat([df3,df2,df1],ignore_index=True)
        print(product_vendor_cols)
        Product_Vendor_counts =product_vendor_cols.value_counts().reset_index()
        Product_Vendor_counts.columns = ['Product_Vendor', 'Number of Products bought']

        return Product_Vendor_counts

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

#print(aggregate_Product_Vendor_data(df,"Lilly+Sid"))
#result = aggregate_Product_Vendor_data_count()

# if result is not None:
#     print("Number of product bought from Each Product_Vendor:")
#     print(result)
# product_vendor=input("Enter the Product Vendor whose data you want to see.\n")
# aggregate_Product_Vendor_data(df,product_vendor)

# #,'Product Line Items_1_Product_Vendor','Product Line Items_2_Product_Vendor'