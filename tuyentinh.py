import pandas as pd

# Load historical sales data
sales_data = pd.read_csv(r'C:\BTEC\ASM\sale.csv')  # Assuming CSV files for simplicity
market_trends = pd.read_csv(r'C:\BTEC\ASM\Market_Trend.csv')
product_details = pd.read_csv(r'C:\BTEC\ASM\product_detail.csv')

# Merge dataframes to create a comprehensive dataset
merged_data = sales_data.merge(product_details, on='product_id').merge(market_trends, on='product_group_id')

# Print the columns of the merged dataset for debugging
print("Merged Data Columns:", merged_data.columns)

# Check for NaN values
print("NaN Values in Merged Data:", merged_data.isnull().sum())

# Example features
# Adjust column names based on what you see in the printed output
features = merged_data[['marketing_spend', 'seasonality', 'economic_indicator']]
target = merged_data['sale_amount']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, r2_score

print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R-squared:", r2_score(y_test, predictions))
