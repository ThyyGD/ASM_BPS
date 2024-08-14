import pandas as pd
import matplotlib.pyplot as plt
# Load data from CSV files
sales_df = pd.read_csv(r'C:\BTEC\ASM\sale.csv')  # Sales data
customer_df = pd.read_csv(r'C:\BTEC\ASM\Customer.csv')  # Customer data
# Convert the sale_date column to datetime
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
# Extract the month from sale_date
sales_df['month'] = sales_df['sale_date'].dt.to_period('M')
# Group by month and sum the sales amount
monthly_sales = sales_df.groupby('month')['sale_amount'].sum().reset_index()
# Find the month with the highest sales
best_month = monthly_sales.loc[monthly_sales['sale_amount'].idxmax()]
# Create a bar chart for monthly sales
plt.figure(figsize=(10, 6))
plt.bar(monthly_sales['month'].astype(str), monthly_sales['sale_amount'], color='skyblue')
# Set the title and labels
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)
# Add a horizontal line for the highest revenue
plt.axhline(y=best_month['sale_amount'], color='r', linestyle='--', label='Highest Revenue')
# Show legend and grid
plt.legend()
plt.grid(axis='y')
# Display the plot
plt.show()
# Print the month with the highest revenue
print(f"The month with the highest revenue is {best_month['month']} with a revenue of ${best_month['sale_amount']:.2f}.")
