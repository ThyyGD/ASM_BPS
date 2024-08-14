import pandas as pd

# Read CSV files
customer_df = pd.read_csv(r'C:\BTEC\ASM\Customer.csv')

# Convert customer_id to numeric and coerce errors to NaN
customer_df['customer_id'] = pd.to_numeric(customer_df['customer_id'], errors='coerce')

# Find rows where customer_id is invalid (NaN)
invalid_customer_ids = customer_df[customer_df['customer_id'].isna()]

# Print out the rows with invalid customer_id
print("Rows with invalid customer_id:")
print(invalid_customer_ids)




# Check for null values
# print("Before removing rows with null values:")
# print(customer_df.isnull().sum())
# Remove rows with null values
# customer_df.dropna(inplace=True)
# Check again for null values after removal
# print("\nAfter removing rows with null values:")
# print(customer_df.isnull().sum())



# Check for empty data
#print(customer_df.isnull().sum())
# market_trend_df = pd.read_csv(r'C:\BTEC\ASM\Market_Trend.csv')
# product_detail_df = pd.read_csv(r'C:\BTEC\ASM\product_detail.csv')
# product_group_df = pd.read_csv(r'C:\BTEC\ASM\Product_Group.csv')
# website_access_category_df = pd.read_csv(r'C:\BTEC\ASM\website_access_category.csv')
# sale_df = pd.read_csv(r'C:\BTEC\ASM\\sale.csv')

# print(market_trend_df.isnull().sum())
# print(product_detail_df.isnull().sum())
# print(product_group_df.isnull().sum())
# print(website_access_category_df.isnull().sum())
# print(sale_df.isnull().sum())

