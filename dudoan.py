import pandas as pd  # Import the pandas library for data manipulation
from sklearn.model_selection import train_test_split  # Import function to split data into training and testing sets
from sklearn.linear_model import LinearRegression  # Import the Linear Regression model
import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs
# Load sales data into a DataFrame from a CSV file
sales_data = pd.read_csv(r'C:\BTEC\ASM\sale.csv')
# Check and print the columns in the DataFrame to verify data structure
print(sales_data.columns)
# Create a sales amount column if 'product_price' exists; otherwise, set a default price
if 'product_price' in sales_data.columns:
    # Calculate sales amount by multiplying quantity sold by product price
    sales_data['sale_amount'] = sales_data['sale_quantity'] * sales_data['product_price']
else:
    # If 'product_price' is not available, assume a default price of 10 for calculation
    sales_data['sale_amount'] = sales_data['sale_quantity'] * 10
# Prepare features (X) and target variable (y)
X = sales_data[['sale_quantity']]  # Using quantity sold as the feature
y = sales_data['sale_amount']  # Sales amount as the target variable
# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a Linear Regression model
model = LinearRegression()  # Initialize the model
# Train the model using the training data
model.fit(X_train, y_train)
# Make predictions on the test set
predictions = model.predict(X_test)
# Plot the actual sales amounts against the predicted values
plt.figure(figsize=(10, 6))  # Set the figure size for the plot
plt.plot(y_test.values, label='Actual Sales', marker='o')  # Plot actual sales
plt.plot(predictions, label='Predicted Sales', linestyle='--', marker='x')  # Plot predicted sales
plt.legend()  # Show legend for the plot
plt.title('Future Sales Prediction')  # Set the title of the plot
plt.xlabel('Time Index')  # Label for the x-axis
plt.ylabel('Sales Amount')  # Label for the y-axis
plt.grid()  # Add grid lines to the plot
plt.show()  # Display the plot
