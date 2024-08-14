import pandas as pd
import matplotlib.pyplot as plt
# Load data from CSV files
sales_df = pd.read_csv(r'C:\BTEC\ASM\sale.csv')  # Sales data
customer_df = pd.read_csv(r'C:\BTEC\ASM\Customer.csv')  # Customer data
# Merge sales and customer data on customer_id
merged_df = pd.merge(sales_df, customer_df, on='customer_id')
# Group by city and sum the sales amount
city_sales = merged_df.groupby('customer_city')['sale_amount'].sum().reset_index()
# Sort the cities by sales amount in descending order and get the top 10
top_cities = city_sales.sort_values(by='sale_amount', ascending=False).head(10)
# Create a bar chart for the top 10 cities
plt.figure(figsize=(12, 6))
plt.bar(top_cities['customer_city'], top_cities['sale_amount'], color='lightgreen')
# Set the title and labels
plt.title('Top 10 Cities with Highest Revenue')
plt.xlabel('City')
plt.ylabel('Total Revenue')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.tight_layout()
plt.show()

# Print the top cities and their revenue
print(top_cities)
