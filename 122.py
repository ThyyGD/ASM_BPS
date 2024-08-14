import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
sales_data = pd.read_csv(r'C:\BTEC\ASM\\sale.csv')

# Convert sale_date to datetime
sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'])

# Group by date and sum the sales amount
daily_sales = sales_data.groupby('sale_date')['sale_amount'].sum().reset_index()

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['sale_date'], daily_sales['sale_amount'], marker='o', color='b')
plt.title('Daily Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
